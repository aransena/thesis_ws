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


    pickle.dump(participants,open("data/participants.p","wb"))
