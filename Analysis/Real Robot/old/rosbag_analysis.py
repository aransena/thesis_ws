#!/usr/bin/env python
from __future__ import division
import rosbag
from geometry_msgs.msg import PoseWithCovarianceStamped
#from nav_msgs.msg import OccupancyGrid
import matplotlib.pyplot as plt
import Tkinter as tk
import tkFileDialog

import numpy as np
import os
from scipy.misc import imread


dir = os.path.expanduser("~")
print "DIR: ", dir
root = tk.Tk()
root.withdraw()

map_file = os.path.join(dir, 'wip_ws/src/robot_2dnav/maps/map.pgm')
map_yaml = os.path.join(dir, 'wip_ws/src/robot_2dnav/maps/map.yaml')
#map_file = os.path.join(dir,'/opt/ros/indigo/share/turtlebot_gazebo/maps/playground.pgm')
#map_yaml = os.path.join(dir,'/opt/ros/indigo/share/turtlebot_gazebo/maps/playground.yaml')

origin_offset_x = 0
origin_offset_y = 0
map_scale = 0
print "\n---------------\n"
f = open(map_yaml,'r')
for line in f:
    if "origin" in line:
        origin_offset_x = float(line.split()[1][1:-1])
        origin_offset_y = float(line.split()[2][:-1])
        print "offsets: ", origin_offset_x, " ", origin_offset_y

    if "resolution" in line:
        map_scale = float(line.split()[1])
        print "map scale: ", (1/map_scale)

f.close()

#bag = rosbag.Bag('503_phone.bag')
bag_file = tkFileDialog.askopenfilename(initialdir="/home/aransena/survey_ws/robot_testing")
bag = rosbag.Bag(bag_file)

print "\n---------------\n"
print bag
print "\n---------------\n"
X=[]
Y=[]
collisions_X=[]
collisions_Y=[]
#map = OccupancyGrid()
firstRun = True

x = 0
y = 0
x_prev = 0
y_prev = 0

dist_tot = 0
#origin_offset_x = -6.89999
#origin_offset_y = -5.89999
semi_cnt = 0
tot_ctl = 0
for topic, msg, t in bag.read_messages():
#for topic, msg, t in bag.read_messages(topics=['amcl_pose']):
    #if topic =="/map":
    #    map = msg

    if topic == "/amcl_pose":#print topic
        point = PoseWithCovarianceStamped()
        point = msg
        x = (point.pose.pose.position.x - origin_offset_x)*(1/map_scale)
        y = (point.pose.pose.position.y - origin_offset_y)*(1/map_scale)
        if(firstRun==True):
            x_prev = x
            y_prev = y
            firstRun = False
        X.append(x)
        Y.append(y)
        dist_tot = dist_tot + np.sqrt(np.power((x-x_prev),2)+np.power((y-y_prev),2))
        x_prev = x
        y_prev = y

    if topic == "/nri_system/collision":#print topic
        collisions_X.append(x)
        collisions_Y.append(y)

    if topic == "/nri_system/control_level":
        #print msg
        if msg.data > 1:
            semi_cnt = semi_cnt + 1
        tot_ctl = tot_ctl+1

print "File: " + bag.filename
print "Time Taken (s): " + str(bag.get_end_time() - bag.get_start_time())
print "Collisions: " + str(len(collisions_X))
if tot_ctl != 0:
    percent_in_sa = (semi_cnt/tot_ctl) * 100
    percent_in_sa = round(percent_in_sa,2)
    print "% Time in Semi Autonomous: " + str(percent_in_sa)

bag.close()

print "Distance travelled: ", round(dist_tot*map_scale, 2),"m"
#X = X*1000
#Y = Y*1000

img = imread(map_file)


plt.figure(1)
img =np.flipud(img)
y1=img.shape[0]
x1=img.shape[1]
plt.imshow(img,zorder=0,origin='lower', extent=[0,x1,0,y1],cmap=plt.cm.gray)
plt.plot(X,Y)
plt.plot(collisions_X,collisions_Y,'ro')
plt.show()
