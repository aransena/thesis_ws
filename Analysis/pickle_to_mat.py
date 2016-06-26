import numpy, scipy.io
import pickle
try:
    import simplejson as json
except ImportError:
    import json


source_p = "/home/aransena/thesis_ws/Analysis/Watch Testing/data/participants.p"
#source_p = "/home/aransena/thesis_ws/Analysis/Real Robot/data/participants.p"

p_data=pickle.load( open( source_p, "rb" ) )
m_data = {}
j_data=[]
watch_man_d = []
watch_sa_d = []
xbox_man_d = []
xbox_sa_d = []
phone_sa_d = []
tablet_sa_d = []
test_d = []
gender_d = []
age_d=[]
game_d=[]
spatial_d=[]
tech_d=[]

for p in p_data:
    print p.get_test_num(), p.get_xbox_man_data()
    d = {}
    #d['watch_man'] = p.get_watch_man_data()  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
    watch_man_d.append(p.get_watch_man_data())  # , f.get_watch_sa_data(),f.get_xbox_man_data(), f.get_xbox_sa_data()
    watch_sa_d.append(p.get_watch_sa_data())
    xbox_man_d.append(p.get_xbox_man_data())
    xbox_sa_d.append(p.get_xbox_sa_data())
    phone_sa_d.append(p.get_phone_data())
    tablet_sa_d.append(p.get_tablet_data())
    #d['test_num'] = p.get_test_num()
    test_d.append(p.get_test_num())
    gender_d.append(p.get_gender())
    age_d.append(p.get_age())
    game_d.append(p.get_game_info())
    spatial_d.append(p.get_spatial())
    tech_d.append(p.get_tech_ability())


    ##j_data.append(d)

#data = []
#data=m_data
m_data['test_num'] = numpy.array(test_d)
m_data['watch_man'] = numpy.array(watch_man_d)
m_data['watch_sa'] = numpy.array(watch_sa_d)
m_data['xbox_man'] = numpy.array(xbox_man_d)
m_data['xbox_sa'] = numpy.array(xbox_sa_d)
m_data['phone_sa'] = numpy.array(phone_sa_d)
m_data['tablet_sa'] = numpy.array(tablet_sa_d)
m_data['gender'] = numpy.array(gender_d)
m_data['age'] = numpy.array(age_d)
print m_data['age']
m_data['game'] = numpy.array(game_d)
m_data['tech'] = numpy.array(tech_d)
m_data['spatial'] = numpy.array(spatial_d)


scipy.io.savemat('/home/aransena/thesis_ws/Analysis/matlab_files/watch_participants.mat', mdict=m_data)
#scipy.io.savemat('/home/aransena/thesis_ws/Analysis/matlab_files/robot_participants.mat', mdict=m_data)

#with open('/home/aransena/thesis_ws/Analysis/matlab_files/watch_participants.json', 'w') as f:
 #       json.dump(j_data, f)
