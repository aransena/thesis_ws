# from zeitgeist.datamodel import Subject
#
# from spm1d.stats import anova3rm, anova1rm
# import numpy as np
#
# # Y = [[100,110,120],[105,110,115]]
# # A = [4,5,6]
# # B = [7,8,9]
# # C = [1,2,3]
# # SUBJ = [1,2]
# # F  = anova3rm(Y,A,B,C,SUBJ, equal_var=True)
# # Fi = F.inference(alpha=0.05)
# # Fi.plot()
#
# Y = np.random.randn(9, 101)
# A = np.array([1,1,1, 2,2,2, 3,3,3])
# SUBJ = np.array([1,2,3, 1,2,3, 1,2,3])
# F = anova1rm(Y, A, SUBJ)
# Fi = F.inference(alpha=0.05)
# Fi.plot()


import numpy as np
from matplotlib import pyplot
import spm1d




#(0) Load data:
dataset      = spm1d.data.uv1d.anova3rm.SPM1D_ANOVA3RM_2x2x2()
# dataset      = spm1d.data.uv1d.anova3rm.SPM1D_ANOVA3RM_2x3x4()

Y,A,B,C,SUBJ = dataset.get_data()
print "Y: ", Y
print "A: ", A
print "B: ", B
print "C: ", C
print "SUBJ: ", SUBJ


#(1) Conduct ANOVA:
alpha        = 0.05
FF           = spm1d.stats.anova3rm(Y, A, B, C, SUBJ, equal_var=True)
FFi          = [F.inference(alpha)   for F in FF]


#(2) Plot results:
pyplot.close('all')
titles       = ['Main effect A',
               'Main effect B',
               'Main effect C',
               'Interaction AB',
               'Interaction AC',
               'Interaction BC',
               'Interaction ABC',
]
for i,Fi in enumerate(FFi):
	ax = pyplot.subplot(3,3,i+1)
	Fi.plot()
	ax.text(0.1, 0.85, titles[i], transform=ax.transAxes)
pyplot.show()




