import os
import pcl
import sys
import shutil
import random
import numpy as np
import pcl.pcl_visualization

def main():

    # File i/o -- Folder name
    if (len(sys.argv) > 1):
        directory = sys.argv[1]
    else:
        print("Need a dirName argument... Exiting")
        exit()

    n_clouds = len([len(r) for r in os.listdir(directory) if os.path.isfile(os.path.join(directory, r))])
 
    # file handling
    if not os.path.exists("{}/smooth".format(directory)):
            print("Made Directory: {}/smooth".format(directory))
            os.mkdir("{}/smooth".format(directory))
    else:    
        shutil.rmtree("{}/smooth".format(directory))
        os.makedirs("{}/smooth".format(directory))
        print("Re-made Directory: {}/smooth".format(directory))

    print("Clouds to process: {}\n".format(n_clouds))
    
    # process each cloud
    for x in range(n_clouds):

        f_name = "{}/inliers/{}.pcd".format(directory, x+1)

        cloud = pcl.load(f_name)
        print('cloud(size) = ' + str(cloud.size))

        tree = cloud.make_kdtree()
        mls = cloud.make_moving_least_squares()

        mls.set_Compute_Normals(True)
        mls.set_polynomial_fit(True)
        mls.set_Search_Method(tree)
        mls.set_search_radius(0.03)

        print('set parameters & processing...')

        mls_points = mls.process()
                
        print('cloud(size) = ' + str(mls_points.size))
        f_name2 = "{}/smooth/{}.pcd".format(directory, x+1)

        pcl.save_PointNormal(mls_points, f_name2)
        print("Processed and saved!\n")        

        # display for last one
        if(x+1 == n_clouds):
            normals = pcl.load(f_name2)

            viewer = pcl.pcl_visualization.PCLVisualizering('CLOUD')
            viewer2 = pcl.pcl_visualization.PCLVisualizering('RESAMPLED')
            pccolor = pcl.pcl_visualization.PointCloudColorHandleringCustom(
                cloud, 255, 255, 255)
            kpcolor = pcl.pcl_visualization.PointCloudColorHandleringCustom(
                normals, 255, 255, 255)

            viewer.AddPointCloud_ColorHandler(cloud, pccolor)
            viewer2.AddPointCloud_ColorHandler(normals, kpcolor, b'normals')

            v = True
            while v:
                v = not(viewer.WasStopped())
                viewer.SpinOnce()   
                
                v2 = not(viewer.WasStopped())
                viewer2.SpinOnce()  
    

if __name__ == "__main__":
    main()
