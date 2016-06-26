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

#colours = ['r','g','b','y','m','k','w','r','g','b','y']
colours = ['0.5','0.55','0.6','0.65','0.7','0.75','0.8','0.85']
#colours = ['w','w','r','k','g','w','w','b','y','m']
titles = ["Average Distance Travelled", "Average Time Taken","Average Collisions Incurred"]
hatches = [".",'-','o']
#groups_end = ['_group_0.txt','_group_1.txt','_group_2.txt','_group_3.txt','_group_4.txt']
groups_end = ['_group_0.txt','_group_1.txt','_group_2.txt','_group_3.txt']
group_start = "age" # "game" "age" "spatial"
data_files = map(lambda x: group_start+x, groups_end)
#data_files = ['participants.txt'] # all_files
# group_start = "all"|
#data_files = ['male_participants.txt','female_participants.txt'] # gender_files
# group_start = "gender"
#data_files = ['m_spatial_group_0.txt','m_spatial_group_1.txt','m_spatial_group_2.txt','m_spatial_group_3.txt','m_spatial_group_4.txt','f_spatial_group_0.txt','f_spatial_group_1.txt','f_spatial_group_2.txt','f_spatial_group_3.txt','f_spatial_group_4.txt'] # gender_spatial_files
# group_start = "gender_spatial"

output_folder = group_start+"/"
spacing = [2,2,2,2,2,1.1,2]

k = 6

if __name__ == '__main__':
    data_dir = os.path.join(os.path.expanduser("~"), 'thesis_ws/Analysis/Watch Testing/analysed/')


    groups = []
    for j,row in enumerate(data_rows[0:3]):
        plt.figure(j)
        ax = plt.axes()
        #ax.set_ylabel('Distance Travelled')
        ax.set_xlabel('Groups')

        plt.title(titles[j])

        for i,file in enumerate(data_files):

            raw_data = open(os.path.join(data_dir,file),'r')
            data = []
            for line in raw_data:
                data.append(line.split(",")[:-1])
            #print map(lambda x: float(x), data[dist_tot_avg_row][1:])

            headers = data[0][1:]

            N = len(data[data_rows[j]][1:])

            #ind = map(lambda x: x+width*i,np.arange(0,N*(len(data_files)/2),(len(data_files)/2)))

            ind = map(lambda x: x+width*i,np.arange(0,N*(len(data_files)/spacing[k]),(len(data_files)/spacing[k])))

            try:
                avgs = map(lambda x: float(x), data[data_rows[j]][1:])
                stds = map(lambda x: float(x), data[data_rows[j+3]][1:])
                group = plt.bar(ind,avgs ,width, color = colours[i], yerr = stds,hatch=hatches[0])

            # except:
            #     print j, i
            #     break
                groups.append(group)
            except Exception as e:
                #print e, "j: ",j+3, " len: " ,len(data)
                pass

        #ax.legend((groups[0][0], groups[1][0]), ('Men', 'Women'))
        ax.set_xticks(ind)#+width)
        ax.set_xticklabels(headers)
        img_output = "visualised/" + output_folder + titles[j] + " - manual.png"
        plt.savefig(img_output)
        #plt.show()

