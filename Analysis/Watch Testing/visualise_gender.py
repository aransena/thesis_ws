#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]

m_data_indx = []
m_data=[]

f_data_indx = []
f_data=[]
if __name__ == '__main__':
    m_file = open("m_output.txt",'r')
    f_file = open("f_output.txt",'r')

    for i, line in enumerate(m_file):
        if "Manual Averages" in line:
            m_data_indx.append(i)
        elif "Semi Auto Averages" in line:
            m_data_indx.append(i)
        elif "Manual STD" in line:
            m_data_indx.append(i)
        elif "Semi Auto STD" in line:
            m_data_indx.append(i)
        elif "AVERAGES" in line:
            m_data_indx.append(i)
        elif "STD" in line:
            m_data_indx.append(i)

        m_data.append(line.split(","))

    for i, line in enumerate(f_file):
        if "Manual Averages" in line:
            f_data_indx.append(i)
        elif "Semi Auto Averages" in line:
            f_data_indx.append(i)
        elif "Manual STD" in line:
            f_data_indx.append(i)
        elif "Semi Auto STD" in line:
            f_data_indx.append(i)
        elif "AVERAGES" in line:
            f_data_indx.append(i)
        elif "STD" in line:
            f_data_indx.append(i)

        f_data.append(line.split(","))

    if len(m_data_indx) == 2 and len(f_data_indx) == 2:
        m_avgs = []
        f_avgs = []
        for line in m_data[m_data_indx[0]+1:m_data_indx[0]+len(tags)]:
            m_avgs.append(map(lambda i: float(i),line[1:]))

        for line in f_data[f_data_indx[0]+1:f_data_indx[0]+len(tags)]:
            f_avgs.append(map(lambda i: float(i),line[1:]))

        m_stds = []
        f_stds = []
        for line in m_data[m_data_indx[1]+1:m_data_indx[1]+len(tags)]:
            m_stds.append(map(lambda i: float(i),line[1:]))

        for line in f_data[f_data_indx[1]+1:f_data_indx[1]+len(tags)]:
            f_stds.append(map(lambda i: float(i),line[1:]))
        #
        # vgs, stds

        headers = m_data[m_data_indx[0]]
        for i, line in enumerate(m_avgs):
            #plt.figure()
            fig, ax = plt.subplots()

            N = len(m_avgs[i])
            ind = np.arange(N)
            width = 0.35
            bars = ax.bar(ind, m_avgs[i],width, color = 'b', yerr = m_stds[i],hatch=".")
            bars2 = ax.bar(ind+width, f_avgs[i],width, color = 'r', yerr = m_stds[i],hatch=".")


            ax.set_ylabel(tags[i])
            ax.set_title(str(headers[0]) + ": " + tags[i])
            ax.set_xticks(ind+width/2)
            ax.set_xticklabels(headers[1:])
            plt.ylim(0,1.1*(max(m_avgs[i])+max(m_stds[i])))
            plt.xlim([min(ind) - 0.2, max(ind) + 0.8])
            plt.savefig("images/gender/"+str(headers[0]) + "_" + tags[i])
            plt.show()

    else:
        # ata
        man_avgs = []
        for line in m_data[m_data_indx[0]+1:m_data_indx[0]+len(tags)]:
            man_avgs.append(map(lambda i: float(i),line[1:]))

        man_stds = []
        for line in m_data[m_data_indx[2]+1:m_data_indx[2]+len(tags)]:
            man_stds.append(map(lambda i: float(i),line[1:]))

        sa_avgs = []
        for line in m_data[m_data_indx[1]+1:m_data_indx[1]+len(tags)]:
            sa_avgs.append(map(lambda i: float(i),line[1:]))

        sa_stds = []
        # ata[data_indx[3]:data_indx[3]+len(tags)]

        for line in m_data[m_data_indx[3]+1:m_data_indx[3]+len(tags)]:
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



            # patterns = ('-', '+', 'x', '\\', '*', 'o', 'O', '.')
            # for bar,pattern in zip(bars,patterns):
            #     bar.set_hatch(pattern)
            headers = m_data[m_data_indx[0]]

            ax.set_ylabel(tags[i])

            ax.set_title(str(headers[0]) + ": " + tags[i])
            ax.set_xticks(ind+width/2)
            ax.set_xticklabels(headers[1:])

            plt.ylim(0,1.1*(max(man_avgs[i])+max(man_stds[i])))

            plt.xlim([min(ind) - 0.2, max(ind) + 0.5])
            plt.savefig("images/gender/manual/"+str(headers[0]) + "_" + tags[i])
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
            headers = m_data[m_data_indx[1]]

            ax.set_ylabel(tags[i])
            ax.set_title(str(headers[0]) + ": " + tags[i])
            ax.set_xticks(ind+width/2)
            ax.set_xticklabels(headers[1:])

            plt.ylim(0,1.1*(max(sa_avgs[i])+max(sa_stds[i])))


            plt.xlim([min(ind) - 0.2, max(ind) + 0.5])
            plt.savefig("images/gender/sa/"+str(headers[0]) + "_" + tags[i])
           # plt.show()
            plt.close()