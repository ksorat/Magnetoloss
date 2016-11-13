#Calculate histograms of Delta-Phi
#Only bother with ions

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle

def lastPhi(fIn):
	isOut = lfmpp.getOut(fIn)
	ids,x = lfmpp.getH5pFin(fIn,"x",Mask=isOut)
	ids,y = lfmpp.getH5pFin(fIn,"y",Mask=isOut)
	pBX = np.arctan2(y,x)*180.0/np.pi
	return pBX

lfmv.initLatex()
msDataFile = "msIonDP.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]
Ns = len(spcs)

aDPms = []

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		aDPms = pickle.load(f)
else:
	print("No data file found, calculating")

	for i in range(Ns):
		fIn = RootDir + spcs[i] + "." + fileStub
		print("Reading %s"%(fIn))
		print("Species %s"%(Leg[i]))
	
		isOut = lfmpp.getOut(fIn)
		R, PhiMP0, LambdaF, Tmp = lfmpp.getSphLoss1st(fIn)
		PhiBX = lastPhi(fIn)
		DelP = PhiBX-PhiMP0
		aDPms.append(DelP)

	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(aDPms,f)

pMax = 0.05
Nb = 40
N0 = -60; N1 = 120
bins = np.linspace(N0,N1,Nb)
doNorm = True
doLog = False

dpFig = plt.hist(aDPms,bins,normed=doNorm,log=doLog)
plt.legend(Leg)
plt.xlabel("Azimuthal Transit in Magnetosheath [$^{\circ}$]")
plt.ylabel("Density")
plt.ylim(0,pMax)

plt.savefig("msDelP.png")
plt.close()
