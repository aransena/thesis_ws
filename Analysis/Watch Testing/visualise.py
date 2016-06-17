#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]

data_indx = []
data=[]
if __name__ == '__main__':
    raw_data = open("output_wprev2.txt",'r')

    for i, line in enumerate(raw_data):
        if "Manual Averages" in line:
            data_indx.append(i)
        elif "Semi Auto Averages" in line:
            data_indx.append(i)
        elif "Manual STD" in line:
            data_indx.append(i)
        elif "Semi Auto STD" in line:
            data_indx.append(i)
        elif "AVERAGES" in line:
            data_indx.append(i)
        elif "STD" in line:
            data_indx.append(i)

        data.append(line.split(","))

    if len(data_indx) == 2:
        avgs = []
        for line in data[data_indx[0]+1:data_indx[0]+len(tags)]:
            avgs.append(map(lambda i: float(i),line[1:]))

        stds = []
        for line in data[data_indx[1]+1:data_indx[1]+len(tags)]:
            stds.append(map(lambda i: float(i),line[1:]))
        #
        # vgs, stds

        headers = data[data_indx[0]]
        for i, line in enumerate(avgs):
            #plt.figure()
            fig, ax = plt.subplots()

            N = len(avgs[i])
            ind = np.arange(N)
            width = 0.35
            bars = ax.bar(ind, avgs[i],width, color = '0.9', yerr = stds[i],hatch=".")

            # patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
            # for bar,pattern in zip(bars,patterns):
            #     bar.set_hatch(pattern)

            ax.set_ylabel(tags[i])
            ax.set_title(str(headers[0]) + ": " + tags[i])
            ax.set_xticks(ind+width/2)
            ax.set_xticklabels(headers[1:])
            plt.ylim(0,1.1*(max(avgs[i])+max(stds[i])))
            plt.xlim([min(ind) - 0.2, max(ind) + 0.5])
            plt.savefig("images/"+str(headers[0]) + "_" + tags[i])
            plt.show()

    else:
        # ata
        avgs = []
        for i in range(0,3):
            avg =[]
            for line in data[data_indx[i]+1:data_indx[i]+len(tags)]:
                avg.append(map(lambda j: float(j),line[1:]))
            avgs.append(avg)

        man_avgs = avgs[0]
        man_stds = avgs[2]
        sa_avgs = avgs[1]
        sa_stds = avgs[3]


        for line in data[data_indx[3]+1:data_indx[3]+len(tags)]:
            sa_stds.append(map(lambda i: float(i),line[1:]))

        # an_avgs
        for i, line in enumerate(man_avgs):
            #plt.figure()
            fig, ax = plt.subplots()

            N = len(man_avgs[i])
            ind = np.arange(N)
            width = 0.35

            #en(man_avgs), len(man_stds), len(ind)

            bars = ax.bar(ind, man_avgs[i],width, color = '0.9', yerr = man_stds[i],hatch=".")

            headers = data[data_indx[0]]

            ax.set_ylabel(tags[i])

            ax.set_title(str(headers[0]) + ": " + tags[i])
            ax.set_xticks(ind+width/2)
            ax.set_xticklabels(headers[1:])

            plt.ylim(0,1.1*(max(man_avgs[i])+max(man_stds[i])))

            plt.xlim([min(ind) - 0.2, max(ind) + 0.5])
            plt.savefig("images/manual/"+str(headers[0]) + "_" + tags[i])
           # plt.show()
            plt.close()

        for i, line in enumerate(sa_avgs):
            #plt.figure()
            fig, ax = plt.subplots()

            N = len(sa_avgs[i])
            ind = np.arange(N)
            width = 0.35

            #en(sa_avgs), len(sa_stds), len(ind)

            bars = ax.bar(ind, sa_avgs[i],width, color = '0.9', yerr = sa_stds[i],hatch=".")



            # patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
            # for bar,pattern in zip(bars,patterns):
            #     bar.set_hatch(pattern)
            headers = data[data_indx[1]]

            ax.set_ylabel(tags[i])
            ax.set_title(str(headers[0]) + ": " + tags[i])
            ax.set_xticks(ind+width/2)
            ax.set_xticklabels(headers[1:])

            plt.ylim(0,1.1*(max(sa_avgs[i])+max(sa_stds[i])))


            plt.xlim([min(ind) - 0.2, max(ind) + 0.5])
            plt.savefig("images/sa/"+str(headers[0]) + "_" + tags[i])
           # plt.show()
            plt.close()