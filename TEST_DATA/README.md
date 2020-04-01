# Test Data
Data to be used for testing, and the scripts it was obtained from. If you want to run it yourself you'll need the kinect. 
```
python capture.py <dirName>
```

View saved pcd data using Open3D's viewer using this script:
```
python viewer.py <dirName> <fileName>
```
Only Scripts are uploaded here. Data was uploaded to cloud here: <br/>
[Here it is](https://mailroosevelt-my.sharepoint.com/:f:/g/personal/dharris36_mail_roosevelt_edu/ErB37MXVl35Ahrh11bWukLoB9OIH3YBIQwgMpU5SfGslkg?e=xtG7bL) <br/> 

### room_data
Contains random test data obtained from my living room.
### register_couch
All snapshots are of same object for use in registration testing
### register_table
All snapshots are of same object for use in registration testing
### 360
Data obtained from 360 room snapshot rotations taken from center of room, only rotating kinect counter clock-wise

## File Layout

**x_cloud.pcd** <br/>
Point cloud data format for captured snapshot <br/>
**x_depth_pretty.png** <br/>
Depth image scaled for easier viewing <br/>
**x_depth_raw.png** <br/>
Raw depth image taken from freenect <br/>
**x_depth_registered.png** <br/>
Depth image aligned to RGB image <br/>
**x_overlayed_registered** <br/>
Aligned depth image overlayed on RGB image to show alignment <br/>
**x_overlayed_unregistered** <br/>
Misaligned Depth/RGB images to show difference between raw data and RGB data <br/>
**x_rgb.png** <br/>
Color image taken from kinect's rgb camera <br/>
**raw_depth_x.npy** <br/>
Raw depth array saved as numpy array file. We have been working with raw depth format thus far to convert to real-world xyz coords. <br/>
**registered_depth_x.npy** <br/>
Aligned depth array (in MM) saved as numpy array file. Since alignment returns depth in mm instead of the raw data, converting this array to real-world xyz coords is our problem. <br/> 

To use in testing:

```
import numpy as np

# load array
data = np.load('data.npy')
# print array
print(data)
```
