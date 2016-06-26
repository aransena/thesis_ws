#!/usr/bin/env python
import numpy as np
import pickle
import os

from scipy.stats import ttest_ind, f_oneway

#tags=["dist_tot","time_tot","collisions","timeInAuto"]
#tags=["dist_tot","time_tot","collisions","timeInAuto","timeInAuto_s1",
          # "timeInAuto_s2","timeInAuto_s3","stage1Time", "stage2Time", "stage3Time",
          # "stage1Collisions", "stage2Collisions", "stage3Collisions"]
interfaces = ["watch_man", "watch_sa", "xbox_man", "xbox_sa", "phone", "tablet"]
measures = ["dist_tot", "time_tot", "collisions"]

def get_pickles(root):
    pickles = []
    for file in os.listdir(root):
        pickles.append(root+file)

    return pickles

if __name__ == '__main__':
    dir = os.path.expanduser("~")
    pickle_source = os.path.join(dir, 'thesis_ws/Analysis/Real Robot/data/')
    #pickle_source = os.path.join(dir, 'thesis_ws/Analysis/Watch Testing/data/')
    output_file = os.path.join(os.path.expanduser("~"), 'thesis_ws/Analysis/Watch Testing/age_analysed/analysis.txt')
    #output_file = os.path.join(os.path.expanduser("~"), 'thesis_ws/Analysis/Real Robot/age_analysed/analysis.txt')

    pickles = [os.path.join(pickle_source,"age_group_0.p"),os.path.join(pickle_source,"age_group_1.p"),os.path.join(pickle_source,"age_group_2.p"),os.path.join(pickle_source,"age_group_3.p")]
    groups = []
    for pick in pickles:

        participants = pickle.load(open(pick, "rb"))

        watch_mans = []
        watch_sas = []
        xbox_mans = []
        xbox_sas = []
        phone = []
        tablet = []

        for f in participants:
            #print f.get_test_num()
            watch_mans.append(f.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
            watch_sas.append(f.get_watch_sa_data())
            xbox_mans.append(f.get_xbox_man_data())
            xbox_sas.append(f.get_xbox_sa_data())
            phone.append(f.get_phone_data())
            tablet.append(f.get_tablet_data())
        data = [watch_mans,watch_sas,xbox_mans,xbox_sas,phone,tablet]
        pick_group=[]
        for set in data:
            trans = zip(*set)
            pick_group.append(trans)
        groups.append(pick_group)
        #groups.append(zip(*data))

    # for g in groups[1]:
    #     print np.mean(g[0])
    c = 0
    r = 0
    f = open(output_file,'w')
    print np.mean(groups[1][c][r]) # gender column(interface) row(measure)
    print len(groups[0][c][r]),len(groups[1][c][r])
    for c,inter in enumerate(interfaces):
        f.write(inter)
        f.write("\n")
        for r,meas in enumerate(measures):
            output = str(meas)+str(f_oneway(groups[0][c][r],groups[1][c][r]))
            f.write(output) # alpha = 0.05
            f.write("\n")
        f.write("\n")
