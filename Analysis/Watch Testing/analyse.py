#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
#import os

from scipy.stats import ttest_ind


if __name__ == '__main__':
    participants = pickle.load(open("participants.p", "rb"))
    watch_mans = []
    watch_sas = []
    xbox_mans = []
    xbox_sas = []
    for f in participants:
        watch_mans.append(f.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
        watch_sas.append(f.get_watch_sa_data())
        xbox_mans.append(f.get_xbox_man_data())
        xbox_sas.append(f.get_xbox_sa_data())

    f = open('output.txt', 'w')

    transposed = zip(*watch_mans)
    transposed_w_m = transposed
    #watch_mans_items = lambda
    avg = lambda items: float(sum(items)) / len(items)
    std = lambda items: np.std(items)
    watch_mans_averages = map(avg, transposed)
    watch_mans_stds = map(std, transposed)

    transposed = zip(*watch_sas)
    avg = lambda items: float(sum(items)) / len(items)
    std = lambda items: np.std(items)
    watch_sas_averages = map(avg, transposed)
    watch_sas_stds = map(std, transposed)

    transposed = zip(*xbox_mans)
    transposed_x_m = transposed
    avg = lambda items: float(sum(items)) / len(items)
    std = lambda items: np.std(items)
    xbox_mans_averages = map(avg, transposed)
    xbox_mans_stds = map(std, transposed)

    transposed = zip(*xbox_sas)
    avg = lambda items: float(sum(items)) / len(items)
    std = lambda items: np.std(items)
    xbox_sas_averages = map(avg, transposed)
    xbox_sas_stds = map(std, transposed)

    data = [transposed_w_m,transposed_x_m]

    #print ttest_ind(data[0],data[1])
    #print reduce(lambda x,y: ttest_ind(x,y),data)

    tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]
    for i in range(0,len(transposed_w_m)):
        results = ttest_ind(transposed_w_m[i],transposed_x_m[i])
        print tags[i], "\t\tt-val: ", round(results[0],2), "\t\tp-val: ", round(results[1],2)
    #print watch_xbox_mans_t



    header = "AVERAGES","watch_man","watch_sa","xbox_man","xbox_sa"
    f.write(str(header)[1:-1])
    f.write("\n")

    for i in range(0,len(xbox_mans_averages)):
        output = tags[i],  round(watch_mans_averages[i],3),  \
                 round(watch_sas_averages[i],3),  \
            round(xbox_mans_averages[i],3), round(xbox_sas_averages[i],3)
        f.write(str(output)[1:-1])
        f.write("\n")

    f.write("\n")
    header = "STD_DEVS","watch_man","watch_sa","xbox_man","xbox_sa"
    f.write(str(header)[1:-1])
    f.write("\n")

    for i in range(0,len(xbox_mans_stds)):
        output = tags[i],  round(watch_mans_stds[i],3),  \
                 round(watch_sas_stds[i],3),  \
            round(xbox_mans_stds[i],3), round(xbox_sas_stds[i],3)
        f.write(str(output)[1:-1])
        f.write("\n")


    f.close()