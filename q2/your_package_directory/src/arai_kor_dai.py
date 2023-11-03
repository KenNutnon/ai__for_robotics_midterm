#!/usr/bin/env python3
import rospy
from your_package_directory.srv import DataTrigger
from std_msgs.msg import String

class MidtermQ2:
    def __init__(self):
        self.active_topic = False
        self.data_pub = rospy.Publisher(f"/data", String, queue_size=1)
        start_srv = rospy.Service(f"/start", DataTrigger, self.start_callback)
        stop_srv = rospy.Service(f"/stop", DataTrigger, self.stop_callback)
        self.is_kill = False

    def start_callback(self, req):
        res = False
        if req.name != '' and req.std_id != 0:
            res = True
        self.active_topic = True
        return res

    def stop_callback(self, req):
        res = False
        if req.name != '' and req.std_id != 0:
            res = True
        self.active_topic = False
        return res

def main():
    rospy.init_node('midterm_q2', anonymous=True)
    q2 = MidtermQ2()
    rospy.loginfo('init midterm_q2')
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        if q2.active_topic:
            q2.data_pub.publish('Nutchanon Nonthapiboon')

if __name__ == '__main__':
    main()
