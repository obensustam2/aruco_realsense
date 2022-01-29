# ArUco marker 3D position and orientation calculation with Realsense D435 camera

## To create ArUco marker
Go to -> https://chev.me/arucogen/ 
```bash
Dictionary: Original ArUco
Marker ID: 33
```

## To install necessary packages
```bash
sudo apt-get install ros-melodic-realsense2-camera*
sudo apt-get install ros-melodic-aruco-ros*
```


## To start realsense and ArUco marker 3D pose detection
```bash
roslaunch aruco_realsense realsense.launch
roslaunch aruco_realsense single.launch
```

## To echo coming data
```bash
rostopic echo /aruco_single/pose
```