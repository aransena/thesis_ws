#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

from scipy.stats import ttest_ind

tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          "stage1Collisions", "stage2Collisions", "stage3Collisions"]
def get_pickles(root):
    pickles = []
    for file in os.listdir(root):
        pickles.append(root+file)

    return pickles

if __name__ == '__main__':
    dir = os.path.expanduser("~")
    pickle_source = os.path.join(dir, 'thesis_ws/Analysis/Watch Testing/data/')
    pickles = get_pickles(pickle_source)

    for pick in pickles:
        participants = pickle.load(open(pick, "rb"))
        watch_mans = []
        watch_sas = []
        xbox_mans = []
        xbox_sas = []
        for f in participants:
            watch_mans.append(f.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
            watch_sas.append(f.get_watch_sa_data())
            xbox_mans.append(f.get_xbox_man_data())
            xbox_sas.append(f.get_xbox_sa_data())
        data = [watch_mans,watch_sas,xbox_mans,xbox_sas]

        pick_name = os.path.split(pick)[1]
        output_dir = os.path.join(os.path.expanduser("~"), 'thesis_ws/Analysis/Watch Testing/analysed/')
        output_file = os.path.join(output_dir,pick_name[:-1]+"txt")
        #output_file = "output.txt"
        f = open(output_file, 'w')

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
            output = tags[i] + ", " + str(data)[1:-1] + ", "
            output = str(output)
            f.write(output)#[1:-1])
            f.write("\n")

        f.write("\n")

        header = ["STD_DEVS","watch_man","watch_sa","xbox_man","xbox_sa"]
        map(lambda x: f.write(x + ", "), header)
        f.write("\n")
        for i in range(0,len(stds[0])):
            data = map(lambda x: round(x,3),zip(*stds)[i])
            output = tags[i] + ", " + str(data)[1:-1]  + ", "
            output = str(output)
            f.write(output)
            f.write("\n")
        f.write("\n")

        header = ["STATS watch_man v xbox_man", "t-val", "p-val", "corr"]
        map(lambda x: f.write(x + ", "), header)
        f.write("\n")
        for i in range(0,len(transposed_sets[0])):
            results = ttest_ind(transposed_sets[0][i],transposed_sets[2][i])
            corr = np.corrcoef(transposed_sets[0][i],transposed_sets[2][i])[0][1]
            output = tags[i] + ", " + str(round(results[0],3)) + ", " + str(round(results[1],3)) + ", " + str(round(corr,3)) + ", "
            f.write(output)
            f.write("\n")


        f.write("\n")
        header = ["STATS watch_sa v xbox_sa", "t-val", "p-val"]
        map(lambda x: f.write(x + ", "), header)
        f.write("\n")
        for i in range(0,len(transposed_sets[0])):
            results = ttest_ind(transposed_sets[1][i],transposed_sets[3][i])
            corr = np.corrcoef(transposed_sets[1][i],transposed_sets[3][i])[0][1]
            output = tags[i] + ", " + str(round(results[0],3)) + ", " + str(round(results[1],3)) + ", " + str(round(corr,3)) + ", "
            f.write(output)
            f.write("\n")

        f.close()