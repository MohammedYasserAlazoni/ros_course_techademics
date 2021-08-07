#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16

def talker () :
    pub = rospy.Publisher ('number',Int16 ,queue_size=10)
    rospy.init_node('talker' , anonymous=False)
    rate=rospy.Rate(5)
    number = 0
    while not rospy.is_shutdown ():
        number += 1
        rospy.loginfo(rospy.get_time())
        pub.publish(number)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInitException:
        pass