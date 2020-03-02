# Demo 3
This demo is a first attempt at a basic pipeline for our process. Simple start at going from raw depth data to registered point clouds

## The Pipeline
Contains four python files used for gathering, cleaning, and combining the data. Still much to do though...

### 1.) Getting Data - Save to .pcd
First we need data. We aquire .pcd scans from "get_data.py" where we are able to see a live visualization of the raw data to help us. While running, press the 'SPACE' key to pause the window for a better view. To take a scan and save it to a .pcd, press the 'S' key. So far, I get the best results when scanning by sequentially scanning the scene with about half of the scan being from the last scan kept in the next to ensure we have keypoints to register later. When you have captured the clouds you'd like, simply close the window to end the program.

#### Run

Run script using below syntax, with 'directory_name' being a directory that will be created for the data. Be sure to use this same directory for each script.

```
python get_data.py directory_name
```

### 2.) Clean Data - Downsample and De-Noise

Once we have our clouds, we downsample them and try to remove any unwanted noise. Current settings give okay results, but please play with the values to see what works best. 

#### Run

Run script using same syntax as before, keeping the directory name as the same

```
python clean_data.py directory_name
```

### 3.) Smooth cloud - Estimate Normals
Here we try to further clean the data by resampling for a smoother look. This is the only portion which uses PCL, and I plan to convert this into a open3d equivolent to fit with the other modules better and decrease dependencies.

#### Run

Run script using same syntax as before, keeping the directory name as the same

```
python smooth_data.py directory_name
```

### 4.) Register Clouds - Global registration and ICP Refinement

At this point we should have at least semi-workable data, and 
#### Run

Run script using same syntax as before, keeping the directory name as the same

```
python combine_data.py directory_name
```

## Some Helpful Open3D links: 
[General Point Clouds](http://www.open3d.org/docs/release/tutorial/Basic/pointcloud.html) <br/> [Visualization](http://www.open3d.org/docs/release/tutorial/Basic/visualization.html) <br/> [ICP](http://www.open3d.org/docs/release/tutorial/Basic/icp_registration.html) <br/> [Noise Removal](http://www.open3d.org/docs/release/tutorial/Advanced/pointcloud_outlier_removal.html) <br/> [Global Registration](http://www.open3d.org/docs/release/tutorial/Advanced/global_registration.html) <br/> [Multiway Registration](http://www.open3d.org/docs/release/tutorial/Advanced/multiway_registration.html) <br/>

In the folder 'Screenshots' there are some images of what i've been able to do so far with this. Definitely needs help but I think this is a good direction to take.
<br/>
The other 'test' folders just contain test data for reference
