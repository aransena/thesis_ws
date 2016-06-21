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
    participants_source = os.path.join(dir, 'thesis_ws/Analysis/Watch Testing/data/participants.p')
    participants = pickle.load(open(participants_source, "rb"))


    male_participants=[]
    female_participants=[]
    age_groups = [[],[],[],[]]
    game_exp_groups = [[],[],[],[]]
    spatial_groups = [[],[],[],[],[]]
    m_spatial_groups = [[],[],[],[],[]]
    f_spatial_groups = [[],[],[],[],[]]
    tech_groups = [[],[],[],[],[]]


    for participant in participants:
        #print participant.get_test_num()
        if participant.get_gender() == 1:
            male_participants.append(participant)
            m_spatial_groups[int(participant.get_spatial())-1].append(participant)
        if participant.get_gender() == 2:
            female_participants.append(participant)
            f_spatial_groups[int(participant.get_spatial())-1].append(participant)

        age = participant.get_age()
        try:
            age_groups[age-1].append(participant)
        except:
            print "No age! ", participant.get_test_num()

        game_info = participant.get_game_info()
        game_exp = game_info[0]
        game_exp_groups[game_exp-1].append(participant)
        ind = int(participant.get_spatial())-1
        spatial_groups[ind].append(participant)
        ind = int(participant.get_tech_ability())-1
        tech_groups[ind].append(participant)


    #pickle.dump(participants,open("data/participants.p","wb"))
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

    for i,group in enumerate(spatial_groups):
        filename = "data/spatial_group_" + str(i) +".p"
        # sum = sum + len(group)
        pickle.dump(group, open(filename,"wb"))

    for i,group in enumerate(m_spatial_groups):
        filename = "data/m_spatial_group_" + str(i) +".p"
        # sum = sum + len(group)
        pickle.dump(group, open(filename,"wb"))

    for i,group in enumerate(f_spatial_groups):
        filename = "data/f_spatial_group_" + str(i) +".p"
        # sum = sum + len(group)
        pickle.dump(group, open(filename,"wb"))

    for i,group in enumerate(tech_groups):
        filename = "data/tech_group_" + str(i) +".p"
        # sum = sum + len(group)
        pickle.dump(group, open(filename,"wb"))