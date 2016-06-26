#!/usr/bin/env python
import numpy as np
import rosbag
import os
from geometry_msgs.msg import PoseWithCovarianceStamped


def process_bag(bag_file,map_data):
    origin_offset_x = map_data[0]
    origin_offset_y = map_data[1]
    map_scale = map_data[2]
    bag = rosbag.Bag(bag_file)

    X=[]
    Y=[]
    collisions_X=[]
    collisions_Y=[]
    firstRun = True

    x = 0
    y = 0
    x_prev = 0
    y_prev = 0

    dist_tot = 0
    semi_cnt = 0
    tot_ctl = 0
    for topic, msg, t in bag.read_messages():

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
            if msg.data > 1:
                semi_cnt = semi_cnt + 1
            tot_ctl = tot_ctl+1

    tot_time = bag.get_end_time() - bag.get_start_time()
    bag.close()
    tot_collisions = len(collisions_X)
    if tot_ctl != 0:
        percent_in_sa = (float(semi_cnt)/tot_ctl) * 100
        percent_in_sa = round(percent_in_sa,2)
    else:
        percent_in_sa = 0

    tot_percent_sa = percent_in_sa
    tot_dist = round(dist_tot*map_scale, 2)
    #print "File: " + bag.filename
    #print "Time Taken (s): " +
    #print "Collisions: " +
    #print "% Time in Semi Autonomous: " + str(percent_in_sa), semi_cnt, tot_ctl
    #print "Distance travelled: ", round(dist_tot*map_scale, 2),"m"
    return [tot_dist,tot_time,tot_collisions,tot_percent_sa]

def get_data(path):
    r = open(path,'r')

    dist_tot=0
    time_tot = 0
    stage1Collisions = 0
    stage2Collisions = 0
    stage3Collisions = 0
    timeInAuto_s1 = 0
    timeInAuto_s2 = 0
    timeInAuto_s3 = 0

    first_line=True

    for line in r:
        line = line[1:len(line)-3]
        line = line.split(",")
        line = map(float,line)

        x = line[3]
        y = line[4]
        collisions = line[6]
        auto = line[7]
        stage = line[8]
        time_tot = time_tot+ 1

        if first_line:
            x_prev = x
            y_prev = y
            first_line = False

        dist_tot = dist_tot + np.sqrt(np.power((x-x_prev),2)+np.power((y-y_prev),2))
        x_prev = x
        y_prev = y

        if stage == 0:
            stage1Collisions = collisions
            stage1Time = time_tot
            if auto==1:
                timeInAuto_s1=timeInAuto_s1+1
        elif stage == 1:
            stage2Collisions = collisions - stage1Collisions
            stage2Time= time_tot - stage1Time
            if auto==1:
                timeInAuto_s2=timeInAuto_s2+1
        else:
            stage3Collisions = collisions - stage2Collisions - stage1Collisions
            stage3Time = time_tot - stage1Time - stage2Time
            if auto==1:
                timeInAuto_s3=timeInAuto_s3+1

    return [dist_tot,time_tot,collisions,timeInAuto_s1+timeInAuto_s2+timeInAuto_s3,timeInAuto_s1,timeInAuto_s2,timeInAuto_s3,stage1Time, stage2Time,stage3Time, stage1Collisions, stage2Collisions, stage3Collisions]


class participant:
    def __init__(self,path,pre_data,post_data,map_data):

        self.path = path
        self.test_num = path[::-1][0:3][::-1]
        files=[]
        watch_files=[]
        xbox_files=[]
        phone_files=[]
        tablet_files=[]
        man_files=[]
        sa_files=[]

        #print self.path
        for test_file in os.listdir(self.path):
            print test_file
            files.append(test_file)
            if "watch" in test_file:
                watch_files.append(test_file)
                if "sa" in test_file:
                    self.watch_sa_data = process_bag(self.path+"/"+test_file, map_data)#get_data(self.path+"/"+test_file)
                if "man" in test_file:
                    self.watch_man_data = process_bag(self.path+"/"+test_file, map_data)#get_data(self.path+"/"+test_file)

            if "xbox" in test_file:
                xbox_files.append(test_file)
                if "sa" in test_file:
                    self.xbox_sa_data = process_bag(self.path+"/"+test_file, map_data)#get_data(self.path+"/"+test_file)
                if "man" in test_file:
                    self.xbox_man_data = process_bag(self.path+"/"+test_file, map_data)#get_data(self.path+"/"+test_file)

            if "phone" in test_file:
                phone_files.append(test_file)
                self.phone_data = process_bag(self.path+"/"+test_file, map_data)

            if "tablet" in test_file:
                tablet_files.append(test_file)
                self.tablet_data = process_bag(self.path+"/"+test_file, map_data)

            if "man" in test_file:
                man_files.append(test_file)

            if "sa" in test_file:
                sa_files.append(test_file)

        self.files=files
        self.watch_files = watch_files
        self.xbox_files = xbox_files
        self.phone_files = phone_files
        self.tablet_files = tablet_files
        self.sa_files = sa_files
        self.man_files = man_files
        self.gender = 0

        # survey data
        for line in pre_data:
            if self.test_num in line:
                data = line
                if data[2] == "18-24":
                    self.pre_age_range = 1
                elif data[2] == "25-34":
                    self.pre_age_range = 2
                elif data[2] == "35-44":
                    self.pre_age_range = 3
                #elif data[2] == "45-54" or data[2] == "55-64" or data[2] == "65-74":
                elif data[2] == "45-54":
                    self.pre_age_range = 4
                elif data[2] == "55-64":
                    self.pre_age_range = 5
                elif data[2] == "65-74":
                    self.pre_age_range = 6
                else:
                    self.pre_age_range = 0

                if data[3] == "Male":
                    self.gender = 1
                elif data[3] == "Female":
                    self.gender = 2
                else:
                    self.gender = 0

                if data[4] == "Yes":
                    self.pre_health = 1
                else:
                    self.pre_health = 0

                if data[5] == "I have never really been into video games":
                    self.pre_ever_played = 1
                elif data[5] == "I used to play video games frequently in the past":
                    self.pre_ever_played = 2
                elif data[5] == "I occasionally play video games":
                    self.pre_ever_played = 3
                elif data[5] == "I frequently play video games":
                    self.pre_ever_played = 4
                else:
                    self.pre_ever_played = 0

                if data[6] == "Never":
                    self.pre_how_often = 1
                elif data[6] == "Rarely":
                    self.pre_how_often = 2
                elif data[6] == "1-3 Hours per week":
                    self.pre_how_often = 3
                elif data[6] == "4-10 Hours per week":
                    self.pre_how_often = 4
                elif data[6] == "11+ Hours per week":
                    self.pre_how_often = 5
                else:
                    self.pre_how_often = 0

                self.pre_ability_technology = data[7]
                self.pre_would_be_easy = [data[8],data[9],data[10],data[11],data[12]] # tablet, watch, phone, xbox, pc
                self.pre_trust = data[13]
                self.pre_spatial = data[14][:-2]

        for line in post_data:
            if self.test_num in line:
                data = line
                self.post_sit_stand = data[2] # general
                self.post_rank_pref_man = [data[3],data[4],data[5],data[6]] # phone tablet smartwatch xbox
                self.post_ease_of_use = [data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14]] # watch_man, watch_sa, xbox_man, xbox_sa tablet_man tablet_sa phone_man phone_sa
                self.post_rank_pref_sa = [data[15],data[16],data[17],data[18]] #  tablet smartwatch phone xbox
                self.post_rate_challenges_man = [data[19],data[20],data[21],data[22],data[23]] # toward you,obstacle avoidance, doors, out of view, turning on spot
                self.post_rate_challenges_sa = [data[24],data[25],data[26],data[27],data[28]] # toward you,obstacle avoidance, doors, out of view, turning on spot
                self.post_trust = data[29]
                self.post_comment = data[30][:-2]

    # def get_pre_data(self):
    #     return [self.pre_age_range,
    #         self.pre_gender,
    #         self.pre_health,
    #         self.pre_ever_played,
    #         self.pre_how_often,
    #         self.pre_ability_technology,
    #         self.pre_would_be_easy,
    #         self.pre_trust,
    #         self.pre_spatial]
    #
    # def get_post_data(self):
    #     return [self.post_sit_stand,
    #             self.post_ease_of_use,
    #             self.post_diff_man,
    #             self.post_diff_sa,
    #             self.post_would_be_easy,
    #             self.post_rank_interfaces,
    #             self.post_trust,
    #             self.post_comment]

    def get_path(self):
        return self.path

    def get_test_num(self):
        return self.test_num


    def get_files(self):
        return self.files

    def get_watch_files(self):
        return self.watch_files

    def get_xbox_files(self):
        return self.xbox_files

    def get_man_files(self):
        return self.man_files

    def get_sa_files(self):
        return self.sa_files

    def get_watch_sa_data(self):
        return self.watch_sa_data

    def get_watch_man_data(self):
        return self.watch_man_data

    def get_xbox_sa_data(self):
        return self.xbox_sa_data

    def get_xbox_man_data(self):
        return self.xbox_man_data

    def get_phone_data(self):
        return self.phone_data

    def get_tablet_data(self):
        return self.tablet_data

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.pre_age_range

    def get_game_info(self):
        return [self.pre_ever_played,self.pre_how_often]

    def get_spatial(self):
        return self.pre_spatial

    def get_tech_ability(self):
        return self.pre_ability_technology

