# Test Data
Data to be used for testing, and the scripts it was obtained from. If you want to run it yourself you'll need the kinect. 
```
python capture.py directory_name
```

View saved pcd data using Open3D's viewer using this script:

```
python viewer.py <dirName> <fileName>
```<br/>

Only Scripts are uploaded here. Data was uploaded to cloud here:
[Link To Data](https://mailroosevelt-my.sharepoint.com/:f:/g/personal/dharris36_mail_roosevelt_edu/ErB37MXVl35Ahrh11bWukLoB9OIH3YBIQwgMpU5SfGslkg?e=xtG7bL) <br/> 

## room_data
Contains random test data obtained from my living room.

## register_couch
All snapshots are of same object for use in registration testing

## register_table
All snapshots are of same object for use in registration testing

## 360
Data obtained from 360 room snapshot rotations taken from center of room, only rotating kinect counter clock-wise

### x_cloud.pcd
Point cloud data format for captured snapshot
### x_depth_pretty.png
Depth image scaled for easier viewing
### x_depth_raw.png
Raw depth image taken from freenect
### x_depth_registered.png
Depth image aligned to RGB image
### x_overlayed_registered
Aligned depth image overlayed on RGB image to show alignment
### x_overlayed_unregistered
Misaligned Depth/RGB images to show difference between raw data and RGB data
### x_rgb.png
Color image taken from kinect's rgb camera
### raw_depth_x.npy
Raw depth array saved as numpy array file. We have been working with raw depth format thus far to convert to real-world xyz coords.
### registered_depth_x.npy 
Aligned depth array (in MM) saved as numpy array file. Since alignment returns depth in mm instead of the raw data, converting this array to real-world xyz coords is our problem. <br/> <br/> 

To use in testing:

```
import numpy as np

# load array
data = np.load('data.npy')
# print array
print(data)
```<br/>
