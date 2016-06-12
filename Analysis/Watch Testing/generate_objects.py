#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import participants as ppants


def get_participants(root, participants):
    for folder in os.listdir(root):
        participants.append(root+folder)

    return participants

if __name__ == '__main__':
    dir = os.path.expanduser("~")
    data_source = os.path.join(dir, 'thesis_ws/Watch_Testing/results/')

    participants_paths = []
    participants_paths = get_participants(data_source, participants_paths)
    participants = []
    for p in participants_paths:
        participants.append(ppants.participant(p))

    pickle.dump(participants,open("participants.p","wb"))


