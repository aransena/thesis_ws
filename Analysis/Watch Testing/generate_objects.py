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
    post_test = surveys_source + "post_test.csv"

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

    for participant in participants:
        print participant.get_test_num()
        if participant.get_gender() == 1:
            male_participants.append(participant)
        if participant.get_gender() == 2:
            female_participants.append(participant)


    print len(female_participants), len(male_participants)

    pickle.dump(participants,open("participants.p","wb"))
    pickle.dump(male_participants,open("male_participants.p","wb"))
    pickle.dump(female_participants,open("female_participants.p","wb"))


