voice = None


from geometry_msgs.msg import Twist
import rospy
import time
rospy.init_node('get_center', anonymous=True)
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel_msg = Twist()
import roslib
import rospy
from kidbright_tpu.msg import tpu_object
from kidbright_tpu.msg import tpu_objects
from std_msgs.msg import String
import rosnode
import subprocess
import time
import os
ros_nodes = rosnode.get_node_names()
if not '/wake_class_wait' in ros_nodes:
	command='rosrun kidbright_tpu wakeword_classify.py _terminate:=False _model:=/home/pi/kbclientNew/nectec-client/dist/Admin_bewy/audios/model.h5 label_file:=/home/pi/kbclientNew/nectec-client/dist/Admin_bewy/audios/label_map.pkl _nframe:=8'
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	time.sleep(10)
while not rospy.is_shutdown():
  voice = rospy.wait_for_message('/inference', String, timeout=4).data
  if voice == 'Go':
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.linear.x = 0.1
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    time.sleep(1)
  elif voice == 'background':
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
  elif voice == 'Right':
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.linear.x = 0
    vel_msg.angular.z = -0.4
    velocity_publisher.publish(vel_msg)
    time.sleep(1)
  elif voice == 'back':
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.linear.x = -0.1
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    time.sleep(1)
  elif voice == 'Left':
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0.4
    velocity_publisher.publish(vel_msg)
    time.sleep(1)
  else:
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
