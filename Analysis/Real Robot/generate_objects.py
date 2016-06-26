from __future__ import division

#!/usr/bin/env python
import numpy as np
import os
import pickle
import real_participants as rp


def get_map_data(file):
    f = open(map_yaml,'r')
    for line in f:
        if "origin" in line:
            offset_x = float(line.split()[1][1:-1])
            offset_y = float(line.split()[2][:-1])
            print "offsets: ", offset_x, " ", offset_y

        if "resolution" in line:
            scale = float(line.split()[1])
            print "map scale: ", (1/scale)

    f.close()
    return [offset_x,offset_y,scale]


def get_participants(root, participants):
    for folder in os.listdir(root):
        participants.append(root+folder)

    return participants


if __name__ == '__main__':
    dir = os.path.expanduser("~")

    data_source = os.path.join(dir, 'thesis_ws/Data/robot_testing/results/')
    surveys_source = os.path.join(dir, 'thesis_ws/Data/robot_testing/Survey/')

    pre_test = surveys_source + "pretest.csv"
    post_test = surveys_source + "posttest.csv"

    #map_file = os.path.join(dir, 'wip_ws/src/robot_2dnav/maps/map.pgm')
    map_yaml = os.path.join(dir, 'wip_ws/src/robot_2dnav/maps/map.yaml')

    map_data = get_map_data(map_yaml)



    participants_paths = []
    participants_paths = get_participants(data_source, participants_paths)

    pre_data = []
    pre_surv = open(pre_test,'r')
    for line in pre_surv:
        pre_data.append(line.split(","))

    post_data = []
    post_surv = open(post_test,'r')
    for line in post_surv:
        post_data.append(line.split(","))

    print len(participants_paths), participants_paths
    # print len(pre_data), pre_data
    # print len(post_data), post_data
    test_nums = []
    for p in pre_data:
        test_nums.append(p[1])

    participants = []

    for i,p in enumerate(participants_paths[:]):
        print "-----------", i/len(participants_paths[:])*100, " % --------------"
        participants.append(rp.participant(p,pre_data,post_data,map_data))
        print "---------------------------------\n"

    pickle.dump(participants,open("data/participants.p","wb"))