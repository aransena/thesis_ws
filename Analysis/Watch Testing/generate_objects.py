#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import participants as ppants
import prev_participants as prev_ppants


def get_participants(root, participants):
    for folder in os.listdir(root):
        participants.append(root+folder)

    return participants

if __name__ == '__main__':
    dir = os.path.expanduser("~")
    data_source = os.path.join(dir, 'thesis_ws/Data/Watch_Testing/results/')
    surveys_source = os.path.join(dir, 'thesis_ws/Data/Watch_Testing/Survey/')

    pre_test = surveys_source + "pretest.csv"
    post_test = surveys_source + "posttest.csv"

    participants_paths = []

    participants_paths = get_participants(data_source, participants_paths)

    pre_data = []
    pre_surv = open(pre_test,'r')
    for line in pre_surv:
        pre_data.append(line.split(","))

    post_data = []
    post_surv = open(post_test,'r')
    for line in post_surv:
        post_data.append(line.split(","))


    participants = []

    for p in participants_paths:
        participants.append(ppants.participant(p,pre_data,post_data))

    male_participants=[]
    female_participants=[]
    age_groups = [[],[],[],[]]
    game_exp_groups = [[],[],[],[]]


    for participant in participants:
        #print participant.get_test_num()
        if participant.get_gender() == 1:
            male_participants.append(participant)
        if participant.get_gender() == 2:
            female_participants.append(participant)

        age = participant.get_age()
        try:
            age_groups[age-1].append(participant)
        except:
            print "No age_groups! ", participant.get_test_num()

        game_info = participant.get_game_info()
        game_exp = game_info[0]
        game_exp_groups[game_exp-1].append(participant)




    pickle.dump(participants,open("data/participants.p","wb"))
    pickle.dump(male_participants,open("data/male_participants.p","wb"))
    pickle.dump(female_participants,open("data/female_participants.p","wb"))

    # sum = 0
    for i,group in enumerate(age_groups):
        filename = "data/age_group_" + str(i) +".p"
        # sum = sum + len(group)
        pickle.dump(group, open(filename,"wb"))
    # print "SUM: ", sum

    # sum = 0
    for i,group in enumerate(game_exp_groups):
        filename = "data/game_group_" + str(i) +".p"
        # sum = sum + len(group)
        pickle.dump(group, open(filename,"wb"))
    # print "SUM: ", sum