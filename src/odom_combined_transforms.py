#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import PoseWithCovarianceStamped

def callback(data):
    br = tf.TransformBroadcaster()
    position = data.pose.pose.position
    orientation = data.pose.pose.orientation
    br.sendTransform((position.x, position.y, position.z),
                     (orientation.x, orientation.y, orientation.z, orientation.w),
                     rospy.Time.now(),
                     "base_link",
                     "odom_combined")

def listener():
    rospy.init_node('odom_combined_broadcaster')
    rospy.Subscriber('/robot_pose_ekf/odom_combined', PoseWithCovarianceStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
