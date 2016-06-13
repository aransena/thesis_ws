#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os


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


class prev_participant:
    def __init__(self,path):
        self.path = path
        files=[]
        app_files=[]
        xbox_files=[]
        man_files=[]
        sa_files=[]
        print self.path
        for test_file in os.listdir(self.path):
            files.append(test_file)
            if "app" in test_file:
                app_files.append(test_file)
                if "Auto_main" in test_file or "auto_main" in test_file:
                    self.app_sa_data = get_data(self.path+"/"+test_file)
                if "Manual" in test_file or "manual" in test_file:
                    self.app_man_data = get_data(self.path+"/"+test_file)

            if "xBox" in test_file or "xbox" in test_file:
                xbox_files.append(test_file)
                if "Increment" in test_file or "increment" in test_file:
                    self.xbox_sa_data = get_data(self.path+"/"+test_file)
                if "Manual" in test_file or "manual" in test_file:
                    self.xbox_man_data = get_data(self.path+"/"+test_file)

            # if "man" in test_file:
            #     man_files.append(test_file)
            #
            # if "sa" in test_file:
            #     sa_files.append(test_file)

        self.files=files
        self.app_files = app_files
        self.xbox_files = xbox_files
        self.sa_files = sa_files
        self.man_files = man_files
        print len(self.files), len(self.app_files), len(self.xbox_files)

    def get_path(self):
        return self.path

    def get_files(self):
        return self.files

    def get_app_files(self):
        return self.app_files

    def get_xbox_files(self):
        return self.xbox_files

    def get_man_files(self):
        return self.man_files

    def get_sa_files(self):
        return self.sa_files

    def get_app_sa_data(self):
        return self.app_sa_data

    def get_app_man_data(self):
        return self.app_man_data

    def get_xbox_sa_data(self):
        return self.xbox_sa_data

    def get_xbox_man_data(self):
        return self.xbox_man_data
