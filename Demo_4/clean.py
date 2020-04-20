import open3d as o3d
import shutil
import sys
import os, os.path

def make_cloud(num, folder): 
    dep="{}_depth_registered.png".format(num)
    col="{}_rgb.jpg".format(num)
    print(dep)
    print(col)

    camera = o3d.camera.PinholeCameraIntrinsic()


    # new params
    camera.set_intrinsics(640, 480, 594.21, 591.04, 339.5, 242.7) # best
    #camera.set_intrinsics(640, 480, 366.193,366.193,256.684,207.085) # test # mid-tier
    # old params
    #camera.set_intrinsics(640, 480, 3.6413, 3.9029, 263.852, 225.717) # width, height, fx, fy, cx, cy # worst

    print("{}/{}".format(folder, dep))
    print("{}/{}".format(folder, col))

    depth_raw = o3d.io.read_image("{}/{}".format(folder, dep))
    color_raw = o3d.io.read_image("{}/{}".format(folder, col))

    # make image
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, depth_trunc=3.0,
        convert_rgb_to_intensity=False)
    print(rgbd_image)

    # make cloud
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, camera)

    # Flip it, save it, bop it, twist it...
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.io.write_point_cloud("{}/clouds/{}_cloud.ply".format(folder, num), pcd)

def main_clean(d):
    directory = d
    print(directory)
    i = 1
    n_clouds = len([len(r) for r in os.listdir(directory) if os.path.isfile(os.path.join(directory, r))]) / 2
    print("CLOUDS = {}\n".format(n_clouds))

    if not os.path.exists("{}/clouds".format(directory)):
        os.mkdir("{}/clouds".format(directory))
    else:    
        shutil.rmtree("{}/clouds".format(directory))
        os.makedirs("{}/clouds".format(directory))

    print("\nDirectory '{}/clouds' Created \n".format(directory))

    voxel_s = 0.01

    for x in range(n_clouds):

        # read and downsample
        f_name = "{}/clouds/{}_cloud.ply".format(directory, x+1)

        make_cloud(x+1, directory)
        
        cloud = o3d.io.read_point_cloud(f_name)

        # stat inliers
        cl, ind = cloud.remove_statistical_outlier(nb_neighbors=35, std_ratio=4.0)
        inlier_cloud = cloud.select_down_sample(ind)
        outlier_cloud = cloud.select_down_sample(ind, invert=True)
        
        f_name = "{}/clouds/{}_cloud.ply".format(directory, x+1)
        o3d.io.write_point_cloud(f_name, inlier_cloud)
        
        print("Saved cloud: clouds/{}.ply".format(directory, x+1))
        print("\nShowing outliers (red) and inliers: ")

        # paint outliers in red
        outlier_cloud.paint_uniform_color([1, 0, 0])
        o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    
    print("\n\nDone!")

main_clean("test")
