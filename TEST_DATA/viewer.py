import sys
import open3d as o3d

if (len(sys.argv) > 2):
    dirName = sys.argv[1]
    fileName = sys.argv[2]
else:
    print("\nGive a new directory name... Exiting")
    exit() 

pcd = o3d.io.read_point_cloud("{}/{}".format(dirName, fileName))
o3d.visualization.draw_geometries([pcd])
