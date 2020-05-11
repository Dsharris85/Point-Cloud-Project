import open3d as o3d

# both read file, display

def main_view_cloud(path):
    cloud = o3d.io.read_point_cloud(path)
    cloud.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
    o3d.visualization.draw_geometries([cloud])
    
def main_view_mesh(path):
    mesh = o3d.io.read_triangle_mesh(path)
    mesh.transform([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]])
    o3d.visualization.draw_geometries([mesh])
