#Calculate histograms of Delta-Phi
#Only bother with ions

import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

subVTI = True

dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["Hydrogen","Oxygen"]
fOut = "OxyDelP.h5part"
K = 5
i = 1 #Oxygen
      

fIn = dirStub + "/" + spcs[i] + "." + fileStub
print("Reading %s"%(fIn))
print("Species %s"%(Leg[i]))
t,ids = lfmpp.getH5p(fIn,"id")

isOut = lfmpp.getOut(fIn)
pid, NumX = lfmpp.countMPX(fIn,isOut)
R, PhiF, LambdaF, Tmp = lfmpp.getSphLoss1st(fIn)
R,PhiL,LambdaL = lfmpp.getSphLoss(fIn)
DelPhi = PhiL-PhiF

isOut[isOut] = (DelPhi)>60
Mask = isOut

id0 = ids[0,Mask]
Np = Mask.sum()

print(Np)
print(K)
if (Np<K):
	K = Np
if (subVTI):
	lfmpp.subH5p(fIn,Mask,K,fOut=fOut,xEq=False)
# else:
# 	for n in range(Np):
# 		plt.plot(xP[:,n],yP[:,n])	
# 		plt.axis('equal')
# 	lfmv.addEarth2D()
# 	plt.show()
