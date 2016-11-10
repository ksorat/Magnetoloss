import argparse
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

fIn = '/Users/soratka1/Work/magnetoloss/synth/e.100keV.h5part'
#fIn = '/Users/soratka1/Work/magnetoloss/debug/e.100keV.h5part'

aCut = 80
pCut = 10
lCut = 30
lCut0 = 5
pid, alph0 = lfmpp.getPitch(fIn)
Rf,Pf,Lf = lfmpp.getSphLoss(fIn,inMask=(alph0>aCut))

Out = lfmpp.getOut(fIn)
Out = Out & (alph0>aCut)
ids = pid[Out]
#hiLat = (np.abs(Lf) > lCut) & (np.abs(Pf) < pCut)
hiLat = (np.abs(Lf) < lCut0) & (np.abs(Pf) < pCut)


#Ri,Pi,Li = lfmpp.getSphLoss(fIn,inMask=(alph0<aCut))

print("Found %d high-lat electrons"%(hiLat.sum()))

pIds = ids[hiLat]
print(pIds)
Np = len(pIds)

t,x = lfmv.getH5p(fIn,"x")
t,y = lfmv.getH5p(fIn,"y")
t,z = lfmv.getH5p(fIn,"z")
t,ids = lfmv.getH5p(fIn,"id")
id0 = ids[0,:]
Out[Out] = (np.abs(Lf) < lCut0) & (np.abs(Pf) < pCut)
Mask = Out

K = 5
lfmpp.subH5p(fIn,Mask,K)

# fig = plt.figure()
# ax = fig.gca(projection='3d')
# lfmv.addEarth(ax)
# p0 = 0
# pFin = 100000
# for n in range(Np):
# 	pid = pIds[n]
# 	isP = (id0 == pid)
# 	loc = isP.argmax()
# 	print(loc)
# 	xp = x[:,loc]
# 	yp = y[:,loc]
# 	zp = z[:,loc]
# 	cp = ids[:,loc]
# 	sct3d = ax.scatter(xp,yp,zp,c=cp,cmap=plt.get_cmap("cool"),vmin=p0,vmax=pFin)

# lfmv.axEqual3d(ax)
# plt.colorbar(sct3d)
# plt.show()
