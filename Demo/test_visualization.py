import pcl
import pcl.pcl_visualization
import sys

def main():
    # PCL Visualizer to view the pointcloud    
    viewer = pcl.pcl_visualization.PCLVisualizering()
   
    # File i/o
    if (len(sys.argv) > 1):
        cloud = pcl.load(sys.argv[1])
    else:
        cloud = pcl.load("square.pcd")    
    '''
    # K-D Tree
    tree = cloud.make_kdtree()
    mls = cloud.make_moving_least_squares()

    mls.set_Compute_Normals(True)
    mls.set_polynomial_fit(True)
    mls.set_Search_Method(tree)
    mls.set_search_radius(0.05)
    mls_points = mls.process()
    pcl.save_PointNormal(mls_points, 'mls_test.pcd')
    #cloud2 = mls_points
    '''
    # Display Text
    hello = "Hello World!"
    viewer.AddText(str.encode(hello),10,50,bytes(1),0)
    size = "Cloud Size = " + str(cloud.size)
    viewer.AddText(str.encode(size),10,20, bytes(2),0)

    # Viewer 
    viewer.AddPointCloud(cloud, bytes(0))
    viewer.SetPointCloudRenderingProperties(pcl.pcl_visualization.PCLVISUALIZER_POINT_SIZE, 1.5, bytes(0))
    color = pcl.pcl_visualization.PointCloudColorHandleringCustom(cloud,255,255,255)
    viewer.AddPointCloud_ColorHandler(cloud,color,bytes(1),0)

    # Start/Stop
    viewer.Spin()
    viewer.RemovePointCloud(bytes(0), 0)

if __name__ == "__main__":
    main()
