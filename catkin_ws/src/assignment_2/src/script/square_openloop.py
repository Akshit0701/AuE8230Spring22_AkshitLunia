#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from cmath import pi 
import time
import math

     
def move():
    
    # Starts a new node
    rospy.init_node('assignment2_ws', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    print("Let's move your robot")

    #Given Task requirements for square loop
    lin_vel = 0.2
    ang_vel = 0.2
    distance = 2

    #Setting all other velocities to zero
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    
    while not rospy.is_shutdown():

        current_distance=0
        current_angle=0
        side_no=0

        #Loop to move the turtle in square
        #Since a squaare has 4 sides and our side_no counter starts from 0, the loop goes from 0 to 3
        while(side_no < 3) :

            #Setting the current time for distance calculus
            t0 = rospy.Time.now().to_sec()
            print("Straight line motion begins")
            #Loop to move the turtle in a straight line
            #rospy.Rate(10).sleep()
            while(current_distance < float(distance)):
                #Assign the appropriate velocities
                vel_msg.linear.x = abs(lin_vel)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = 0
                #Publish the velocities
                velocity_publisher.publish(vel_msg)
                #Takes actual time to velocity calculus
                t1=rospy.Time.now().to_sec()
                #Calculate current_distance with respect to time and velocity
                current_distance = lin_vel*(t1-t0)

            #Since the robot still has a linear velocity at the end of the loop, we need to force stop the robot
            #We do so by publishing the velocity as 0
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0         
            velocity_publisher.publish(vel_msg)
            print("Distance travelled:", current_distance)
            print("Straight line motion ends, turning will begin")
            time.sleep(1.5) #Pause for 1.5sec
            
            t0 = rospy.Time.now().to_sec()
            
            #Loop rotate turtle by 90 deg
            #rospy.Rate(10).sleep()
            while(current_angle < float(pi/2)) :
            	#Assign the appropriate velocities
            	vel_msg.linear.x = 0
            	vel_msg.linear.y = 0
            	vel_msg.linear.z = 0
            	vel_msg.angular.z = ang_vel
            	vel_msg.angular.x = 0
            	vel_msg.angular.y = 0
            	#Publish the velocities
            	velocity_publisher.publish(vel_msg)
            	t2=rospy.Time.now().to_sec()
            	#Calculate current_angle with respect to time and velocity
            	current_angle = ang_vel*(t2-t0)

            #Since the robot still has a angular velocity at the end of the loop, we need to force stop the robot
            #We do so by publishing the angular velocity as 0
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0 
            velocity_publisher.publish(vel_msg)
            print("Angle rotated by:", math.degrees(current_angle))
            print("Turning ends")
            time.sleep(1.5) #Pause for 1.5sec
            
            side_no=side_no+1
            current_distance=0
            current_angle=0


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass