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
    prev_data_source = os.path.join(dir, 'thesis_ws/Data/Watch_Testing/prev_results/')
    prev_participants_paths = []

    prev_participants_paths = get_participants(prev_data_source, prev_participants_paths)

    prev_participants = []

    for p in prev_participants_paths:
        prev_participants.append(prev_ppants.prev_participant(p))

    pickle.dump(prev_participants,open("prev_participants.p","wb"))


