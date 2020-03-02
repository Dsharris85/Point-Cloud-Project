import sys
import shutil
import os, os.path
import open3d as o3d

def main():

    i = 1
    voxel_s = 0.01

    # File i/o -- Folder name
    if (len(sys.argv) > 1):
        directory = sys.argv[1]
    else:
        print "Need a dirName argument... Exiting"
        exit()

    n_clouds = len([len(r) for r in os.listdir(directory) if os.path.isfile(os.path.join(directory, r))])

    # file handling
    if not os.path.exists("{}/inliers".format(directory)):
        os.mkdir("{}/inliers".format(directory))
        print "\nDirectory '{}/inliers' Created \n".format(directory)
    else:    
        shutil.rmtree("{}/inliers".format(directory))
        os.makedirs("{}/inliers".format(directory))
        print "\nDirectory '{}/inliers' Re-created \n".format(directory)

    for x in range(n_clouds):

        # read and downsample
        f_name = "{}/{}.pcd".format(directory, x+1)
        pcd = o3d.io.read_point_cloud(f_name)
        voxel_down_pcd = pcd.voxel_down_sample(voxel_size = voxel_s)

        print '\nDownsampled {} to a voxel size of {}\n'.format(f_name, voxel_s)

        # stat inliers
        cl, ind = voxel_down_pcd.remove_statistical_outlier(nb_neighbors=30, std_ratio=2.0)
        inlier_cloud = voxel_down_pcd.select_down_sample(ind)
        outlier_cloud = voxel_down_pcd.select_down_sample(ind, invert=True)

        # experimented with radial outliers too. left in to try both or 1, and then play with values    
        '''
        # save and load or else error
        o3d.io.write_point_cloud("temp.pcd", inlier_cloud)
        pcd = o3d.io.read_point_cloud("temp.pcd")

        # radius outliers - for larger 'floaters'
        cl, ind = pcd.remove_radius_outlier(nb_points=10, radius=1.0)
        inlier_cloud2 = pcd.select_down_sample(ind)

        # save file
        f_name = "{}/inliers/{}.pcd".format(directory, x+1)
        o3d.io.write_point_cloud(f_name, inlier_cloud)

        print "Saved {}".format(f_name)
        '''

        # write final cloud after downsampling and removing noise
        f_name = "{}/inliers/{}.pcd".format(directory, x+1)
        o3d.io.write_point_cloud(f_name, inlier_cloud)
        print("Saved cloud: inliers/{}.pcd".format(directory, x+1))

        # display last one
        if (x == n_clouds - 1):
            print("\nShowing outliers (red) and inliers (gray): ")

            outlier_cloud.paint_uniform_color([1, 0, 0])
            inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
            o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])

    print "\n\nDone!"

if __name__ == "__main__":
    main()
