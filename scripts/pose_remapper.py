#!/usr/bin/env python
from tokenize import String
import rospy
import math
from std_msgs.msg import Float32
from geometry_msgs.msg import Vector3, Quaternion, PoseStamped, PoseWithCovarianceStamped
from tf.transformations import euler_from_quaternion

new_pose = PoseStamped()
yaw_degree = 0

def pose_callback(data):
    global yaw_degree
    euler = euler_from_quaternion([data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w])
    yaw_radian = euler[2]
    yaw_degree = math.degrees(yaw_radian)

def talker():
    global yaw_degree
    rospy.init_node('imu_converter', anonymous=True)
    rospy.Subscriber('/aruco_single/pose', PoseStamped, pose_callback)
    pub_yaw = rospy.Publisher('/aruco_single/yaw', Float32, queue_size=10)
    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        pub_yaw.publish(yaw_degree)
        rospy.loginfo(yaw_degree)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
