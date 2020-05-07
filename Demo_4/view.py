import open3d as o3d

# both read file, display

def main_view_cloud(path):
    print("\n\nPATH: {}\n\n".format(path))
    cloud = o3d.io.read_point_cloud(path)
    o3d.visualization.draw_geometries([cloud])
    
def main_view_mesh(path):
    print(path)
    mesh = o3d.io.read_triangle_mesh(path)
    o3d.visualization.draw_geometries([mesh])
