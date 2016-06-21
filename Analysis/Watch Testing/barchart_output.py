#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
import os

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]

# dist_tot_avg_row = 1
# time_tot_avg_row = 2
# coll_tot_avg_row = 3
#
# dist_tot_std_row = 16
# time_tot_std_row = 17
# coll_tot_std_row = 18
# man_data_cols = [1,3]
# sa_data_cols = [2,4]

data_rows = [1,2,3,16,17,18]


width = 0.35

colours = ['r','g','b','y','m','k']
titles = ["Average Distance Travelled", "Average Time Taken","Average Collisions Incurred"]

all_files = ['participants.txt']
game_files = ['game_group_0.txt','game_group_1.txt','game_group_2.txt','game_group_3.txt']
gender_files = ['male_participants.txt','female_participants.txt']
age_files = ['age_group_0.txt','age_group_1.txt','age_group_2.txt','age_group_3.txt']

output_folders = ["all/", "game_groups/", "age_groups/", "gender/"]
data_files = [all_files,game_files,age_files,gender_files]
k = 2

if __name__ == '__main__':
    data_dir = os.path.join(os.path.expanduser("~"), 'thesis_ws/Analysis/Watch Testing/analysed/')


    groups = []
    for j,row in enumerate(data_rows[0:3]):
        plt.figure(j)
        ax = plt.axes()
        #ax.set_ylabel('Distance Travelled')
        ax.set_xlabel('Groups')

        plt.title(titles[j])

        for i,file in enumerate(data_files[k]):

            raw_data = open(os.path.join(data_dir,file),'r')
            data = []
            for line in raw_data:
                data.append(line.split(",")[:-1])
            #print map(lambda x: float(x), data[dist_tot_avg_row][1:])

            headers = data[0][1:]

            N = len(data[data_rows[j]][1:])

            ind = map(lambda x: x+width*i,np.arange(0,N*(len(data_files)/2),(len(data_files)/2)))
            #ind = np.arange(0,N)+width
            print ind
            # try:
            group = plt.bar(ind, map(lambda x: float(x), data[data_rows[j]][1:]),width, color = colours[i])#, yerr = stds[i],hatch=".")

            # except:
            #     print j, i
            #     break
            groups.append(group)

        #ax.legend((groups[0][0], groups[1][0]), ('Men', 'Women'))
        ax.set_xticks(ind)#+width)
        ax.set_xticklabels(headers)
        img_output = "visualised/"+output_folders[k]+titles[j]+" - manual.png"
        plt.savefig(img_output)
        #plt.show()

