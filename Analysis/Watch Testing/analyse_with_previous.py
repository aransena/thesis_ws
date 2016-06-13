#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
#import os

from scipy.stats import ttest_ind

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]

if __name__ == '__main__':
    participants = pickle.load(open("participants.p", "rb"))
    prev_participants = pickle.load(open("prev_participants.p", "rb"))

    watch_mans = []
    watch_sas = []
    xbox_mans = []
    xbox_sas = []
    prev_xbox_mans = []
    prev_xbox_sas = []
    app_mans = []
    app_sas = []

    for f in participants:
        watch_mans.append(f.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
        watch_sas.append(f.get_watch_sa_data())
        xbox_mans.append(f.get_xbox_man_data())
        xbox_sas.append(f.get_xbox_sa_data())

    for f in prev_participants:
        app_mans.append(f.get_app_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
        app_sas.append(f.get_app_sa_data())
        prev_xbox_mans.append(f.get_xbox_man_data())
        prev_xbox_sas.append(f.get_xbox_sa_data())

    data = [watch_mans,watch_sas,xbox_mans,xbox_sas, prev_xbox_mans,prev_xbox_sas, app_mans, app_sas]

    f = open('output.txt', 'w')
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



    header = ["AVERAGES","watch_man","watch_sa","xbox_man","xbox_sa", "prev_xbox_mans", "prev_xbox_sas", "app_mans", "app_sas"]
    map(lambda x: f.write(x + ", "), header)
    f.write("\n")

    for i in range(0,len(avgs[0])):
        data = map(lambda x: round(x,3),zip(*avgs)[i])
        output = tags[i] + ", " + str(data)[1:-1]
        output = str(output)
        f.write(output)#[1:-1])
        f.write("\n")
    f.write("\n\n")

    header = ["STD_DEVS","watch_man","watch_sa","xbox_man","xbox_sa", "prev_xbox_mans", "prev_xbox_sas", "app_mans", "app_sas"]
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

