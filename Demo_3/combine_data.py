import os
import sys
import copy
import numpy as np
import open3d as o3d

# show results - source and target cloud, target transformation, draw = true/false
def draw_registration_result(source, target, transformation, draw):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)

    final_cloud = (source_temp + target_temp)

    o3d.io.write_point_cloud("{}/combined.pcd".format(dirName), final_cloud)

    if (draw): o3d.visualization.draw_geometries([source_temp, target_temp])

# process to register
def preprocess_point_cloud(pcd, voxel_size):
    print(":: Downsample with a voxel size %.3f." % voxel_size)
    pcd_down = pcd.voxel_down_sample(voxel_size)

    radius_normal = voxel_size * 2
    print(":: Estimate normal with search radius %.3f." % radius_normal)
    pcd_down.estimate_normals(
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_normal, max_nn=30))

    radius_feature = voxel_size * 5
    print(":: Compute FPFH feature with search radius %.3f." % radius_feature)
    pcd_fpfh = o3d.registration.compute_fpfh_feature(
        pcd_down,
        o3d.geometry.KDTreeSearchParamHybrid(radius=radius_feature, max_nn=100))
    return pcd_down, pcd_fpfh

# init
def prepare_dataset(voxel_size, source_path, target_path):
    print(":: Load two point clouds and disturb initial pose.")
    source = o3d.io.read_point_cloud("{}/{}.pcd".format(dirName, source_path))
    target = o3d.io.read_point_cloud("{}/{}.pcd".format(dirName, target_path))

    trans_init = np.asarray([[0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0],
                             [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
    source.transform(trans_init)


    source_down, source_fpfh = preprocess_point_cloud(source, voxel_size)
    target_down, target_fpfh = preprocess_point_cloud(target, voxel_size)
    return source, target, source_down, target_down, source_fpfh, target_fpfh

# where the magic happens
def execute_global_registration(source_down, target_down, source_fpfh,
                                target_fpfh, voxel_size):
    distance_threshold = voxel_size * 1.5
    print(":: RANSAC registration on downsampled point clouds.")
    print("   Since the downsampling voxel size is %.3f," % voxel_size)
    print("   we use a liberal distance threshold %.3f." % distance_threshold)

    result = o3d.registration.registration_ransac_based_on_feature_matching(
        source_down, target_down, source_fpfh, target_fpfh, distance_threshold,
        o3d.registration.TransformationEstimationPointToPoint(False), 4, [
            o3d.registration.CorrespondenceCheckerBasedOnEdgeLength(0.9),
            o3d.registration.CorrespondenceCheckerBasedOnDistance(
                distance_threshold)
        ], o3d.registration.RANSACConvergenceCriteria(4000000, 500))
    return result

# final refinement using ICP
def refine_registration(source, target, source_fpfh, target_fpfh, voxel_size):
    distance_threshold = voxel_size * 0.4
    print(":: Point-to-plane ICP registration is applied on original point")
    print("   clouds to refine the alignment. This time we use a strict")
    print("   distance threshold %.3f." % distance_threshold)

    source_d = source.voxel_down_sample(voxel_size)
    target_d = target.voxel_down_sample(voxel_size)

    source_d.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 2, max_nn=30))
    target_d.estimate_normals(o3d.geometry.KDTreeSearchParamHybrid(radius=voxel_size * 2, max_nn=30))

    result = o3d.registration.registration_icp(source_d, target_d, distance_threshold, result_ransac.transformation, o3d.registration.TransformationEstimationPointToPlane())
        
    return result


if __name__ == "__main__":

    dirName = ''    
    
    # means 5cm for the dataset
    voxel_size = 0.05  
    draw = True

    # File i/o -- Folder name
    if (len(sys.argv) > 1):
        dirName = sys.argv[1]
    else:
        print("Need a dirName argument... Exiting") 
        exit()

    n_clouds = sum([len(files) for r, d, files in os.walk('{}/smooth'.format(dirName))])

    print("Clouds to register: {}\n".format(n_clouds))
    
    # doing i-1 cloud registrations (3 clouds = compare 1 & 2, compare (1&2) & 3)
    for i in range(n_clouds - 1):

        print("i = {}".format(i))

        if (i == n_clouds - 1): 
            break
        elif(i == 0): # first one takes 1.pcd, 2.pcd
            source, target, source_down, target_down, source_fpfh, target_fpfh = prepare_dataset(voxel_size, i+1, i+2)
        else: # rest of iterations take combined.pcd, i+2.pcd
            source, target, source_down, target_down, source_fpfh, target_fpfh = prepare_dataset(voxel_size, "combined", i+2)

        # global registration
        result_ransac = execute_global_registration(source_down, target_down,
                                                    source_fpfh, target_fpfh,
                                                    voxel_size)

        print(result_ransac)

        # registration refinement
        result_icp = refine_registration(source, target, source_fpfh, target_fpfh,
                                         voxel_size)
        print(result_icp)

        # displays each pair of registrations - change draw to false to not do this
        draw_registration_result(source, target, result_icp.transformation, draw)

        if(i == 0):
            print("\n\nCombined Clouds: {} + {}".format(i+1, i+2))
        else:
            print("\n\nCombined Clouds: {} + {}".format("combined", i+2))
        
        print("#" * 100) 
        print       
