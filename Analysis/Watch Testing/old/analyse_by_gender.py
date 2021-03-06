#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
#import os

from scipy.stats import ttest_ind

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]


def analysis(f,data):
    avgs = []
    stds = []
    transposed_sets = []

    for set in data:
        transposed = zip(*set)
        transposed_sets.append(transposed)
        avg = lambda items: float(sum(items)) / len(items)
        std = lambda items: np.std(items)
        avgs.append(map(avg, transposed))
        stds.append(map(std, transposed))
        print transposed


    header = ["AVERAGES","watch_man","watch_sa","xbox_man","xbox_sa"]
    map(lambda x: f.write(x + ", "), header)
    f.write("\n")

    for i in range(0,len(avgs[0])):
        data = map(lambda x: round(x,3),zip(*avgs)[i])
        output = tags[i] + ", " + str(data)[1:-1]
        output = str(output)
        f.write(output)#[1:-1])
        f.write("\n")


    header = ["STD_DEVS","watch_man","watch_sa","xbox_man","xbox_sa"]
    map(lambda x: f.write(x + ", "), header)
    f.write("\n")
    for i in range(0,len(stds[0])):
        data = map(lambda x: round(x,3),zip(*stds)[i])
        output = tags[i] + ", " + str(data)[1:-1]
        output = str(output)
        f.write(output)
        f.write("\n")
    f.write("\n\n")

    header = ["STATS watch_man v xbox_man", "t-val", "p-val", "corr"]
    map(lambda x: f.write(x + ", "), header)
    f.write("\n")
    for i in range(0,len(transposed_sets[0])):
        results = ttest_ind(transposed_sets[0][i],transposed_sets[2][i])
        corr = np.corrcoef(transposed_sets[0][i],transposed_sets[2][i])[0][1]
        output = tags[i] + ", " + str(round(results[0],3)) + ", " + str(round(results[1],3)) + ", " + str(round(corr,3))
        f.write(output)
        f.write("\n")


    f.write("\n")
    header = ["STATS watch_sa v xbox_sa", "t-val", "p-val"]
    map(lambda x: f.write(x + ", "), header)
    f.write("\n")
    for i in range(0,len(transposed_sets[0])):
        results = ttest_ind(transposed_sets[1][i],transposed_sets[3][i])
        corr = np.corrcoef(transposed_sets[1][i],transposed_sets[3][i])[0][1]
        output = tags[i] + ", " + str(round(results[0],3)) + ", " + str(round(results[1],3)) + ", " + str(round(corr,3))
        f.write(output)
        f.write("\n")

    f.close()


if __name__ == '__main__':
    f_participants = pickle.load(open("female_participants.p", "rb"))
    m_participants = pickle.load(open("male_participants.p", "rb"))

    f_watch_mans = []
    f_watch_sas = []
    f_xbox_mans = []
    f_xbox_sas = []
    for f in f_participants:
        f_watch_mans.append(f.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
        f_watch_sas.append(f.get_watch_sa_data())
        f_xbox_mans.append(f.get_xbox_man_data())
        f_xbox_sas.append(f.get_xbox_sa_data())
    f_data = [f_watch_mans,f_watch_sas,f_xbox_mans,f_xbox_sas]

    m_watch_mans = []
    m_watch_sas = []
    m_xbox_mans = []
    m_xbox_sas = []
    for f in m_participants:
        m_watch_mans.append(f.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
        m_watch_sas.append(f.get_watch_sa_data())
        m_xbox_mans.append(f.get_xbox_man_data())
        m_xbox_sas.append(f.get_xbox_sa_data())
    m_data = [m_watch_mans,m_watch_sas,m_xbox_mans,m_xbox_sas]

    m_f = open('m_output.txt', 'w')
    f_f = open('f_output.txt','w')


    analysis(m_f,m_data)
    analysis(f_f,f_data)


    # transposed = zip(*watch_mans)
    # transposed_w_m = transposed
    # #watch_mans_items = lambda
    # avg = lambda items: float(sum(items)) / len(items)
    # std = lambda items: np.std(items)
    # watch_mans_averages = map(avg, transposed)
    # watch_mans_stds = map(std, transposed)
    #
    # transposed = zip(*watch_sas)
    # transposed_w_sa = transposed
    # avg = lambda items: float(sum(items)) / len(items)
    # std = lambda items: np.std(items)
    # watch_sas_averages = map(avg, transposed)
    # watch_sas_stds = map(std, transposed)
    #
    # transposed = zip(*xbox_mans)
    # transposed_x_m = transposed
    # avg = lambda items: float(sum(items)) / len(items)
    # std = lambda items: np.std(items)
    # xbox_mans_averages = map(avg, transposed)
    # xbox_mans_stds = map(std, transposed)
    #
    # transposed = zip(*xbox_sas)
    # transposed_x_sa = transposed
    # avg = lambda items: float(sum(items)) / len(items)
    # std = lambda items: np.std(items)
    # xbox_sas_averages = map(avg, transposed)
    # xbox_sas_stds = map(std, transposed)
    #
    # data = [transposed_w_m,transposed_x_m]

    #print ttest_ind(data[0],data[1])
    #print reduce(lambda x,y: ttest_ind(x,y),data)


    #print watch_xbox_mans_t

    # header = "AVERAGES","watch_man","watch_sa","xbox_man","xbox_sa"
    # f.write(str(header)[1:-1])
    # f.write("\n")
    #
    # for i in range(0,len(xbox_mans_averages)):
    #     output = tags[i],  round(watch_mans_averages[i],3),  \
    #              round(watch_sas_averages[i],3),  \
    #         round(xbox_mans_averages[i],3), round(xbox_sas_averages[i],3)
    #     f.write(str(output)[1:-1])
    #     f.write("\n")
    #
    # f.write("\n")
    # header = "STD_DEVS","watch_man","watch_sa","xbox_man","xbox_sa"
    # f.write(str(header)[1:-1])
    # f.write("\n")
    #
    # for i in range(0,len(xbox_mans_stds)):
    #     output = tags[i],  round(watch_mans_stds[i],3),  \
    #              round(watch_sas_stds[i],3),  \
    #         round(xbox_mans_stds[i],3), round(xbox_sas_stds[i],3)
    #     f.write(str(output)[1:-1])
    #     f.write("\n")

