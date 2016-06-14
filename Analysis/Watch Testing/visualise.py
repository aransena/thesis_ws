#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]


if __name__ == '__main__':
    raw_data = open("output.txt",'r')
    data_indx = []
    data=[]
    for i, line in enumerate(raw_data):
        if "AVERAGES" in line:
            data_indx.append(i)
        if "STD" in line:
            data_indx.append(i)
        data.append(line.split(","))

    avgs = []
    for line in data[data_indx[0]+1:data_indx[0]+len(tags)]:
        avgs.append(map(lambda i: float(i),line[1:]))

    stds = []
    for line in data[data_indx[1]+1:data_indx[1]+len(tags)]:
        stds.append(map(lambda i: float(i),line[1:]))

    print avgs, stds

    headers = data[data_indx[0]]
    for i, line in enumerate(avgs):
        #plt.figure()
        fig, ax = plt.subplots()
        N = len(avgs[i])
        ind = np.arange(N)
        width = 0.35
        ax.bar(ind, avgs[i],width, color = '0.75', yerr = stds[i])
        ax.set_ylabel(tags[i])
        ax.set_title(str(headers[0]) + ": " + tags[i])
        ax.set_xticks(ind+width/2)
        ax.set_xticklabels(headers[1:])
        plt.ylim(0,1.1*(max(avgs[i])+max(stds[i])))
        plt.xlim([min(ind) - 0.2, max(ind) + 0.5])
        plt.show()

    #
    # N = 5
    # menMeans = (20, 35, 30, 35, 27)
    # menStd = (2, 3, 4, 1, 2)
    #
    # #ind = np.arange(N)  # the x locations for the groups
    # #width = 0.35       # the width of the bars
    #
    # #fig, ax = plt.subplots()
    # rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)
    #
    # womenMeans = (25, 32, 34, 20, 25)
    # womenStd = (3, 5, 2, 3, 3)
    # rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)
    #
    # add some text for labels, title and axes ticks
    # ax.set_ylabel('Scores')
    # ax.set_title('Scores by group and gender')
    # ax.set_xticks(ind + width)
    # ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
    #
    # ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    #
    #
    # def autolabel(rects):
    #     attach some text labels
    #     for rect in rects:
    #         height = rect.get_height()
    #         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
    #                 '%d' % int(height),
    #                 ha='center', va='bottom')

    # autolabel(rects1)
    # autolabel(rects2)

    ##plt.show()