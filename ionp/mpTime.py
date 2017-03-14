#Calculate time lost particles spend on open field lines before leaving box
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle


def getTimes(fIn,doTail=False):
	isOut = lfmpp.getOut(fIn,mp=True,tl=doTail)
	t, mpF  = lfmpp.getH5p(fIn,"mp")
	mp = mpF[:,isOut]

	#Last MP crossings
	pid,Tmpx = lfmpp.getH5pFin(fIn,"tCr",Mask=isOut) 

	#First MP crossings
	R, Phi, Lambda, Tmpx0 = lfmpp.getSphLoss1st(fIn)

	#Time of loss from box, time slice index
	tsMP = np.argmax(mp,axis=0)
	#Convert to physical time
	Tbx = t[tsMP]
	if (doTail):
		#Remove particles that leave through tail but never cross MP
		DelT = Tbx-Tmpx
		Tbx = Tbx[DelT>0]
		Tmpx = Tmpx[DelT>0]
		pid = pid[DelT>0]

	return Tmpx,Tmpx0,Tbx,pid

figSize = (8,8)
figQ = 300 #DPI

lfmv.initLatex()
msDataFile = "msIonT.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]
Ns = len(spcs)

aTms = []
aTbar = []

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		aTms = pickle.load(f)
		aTbar = pickle.load(f)
else:
	print("No data file found, calculating")

	for i in range(Ns):
		fIn = RootDir + spcs[i] + "." + fileStub
		print("Reading %s"%(fIn))
		Tmpx, Tmpx0, Tbx,pids = getTimes(fIn,doTail=True)
	
		DelT0 = Tbx-Tmpx0
		Tb = DelT0.mean()
		aTms.append(DelT0)
		aTbar.append(Tb)
		print("Species %s"%(Leg[i]))
		print("\tMin / Max DelT = %d / %d"%(np.amin(DelT0),np.amax(DelT0)) )
		print("\t# particles = %d"%len(DelT0))
		print("\tMax @ %d"%(pids[np.argmax(DelT0)]))
		print("\tMean Tms = %f"%Tb)

	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(aTms,f)
		pickle.dump(aTbar,f)

#Add noise for figure rounding
dT = 2.5
for i in range(2):
	Np = aTms[i].shape[0]
	X = np.random.rand(Np)
	dTms = 2*dT*(X-0.5)
	aTms[i] = aTms[i]+dTms

#Log configuration
pMax = 1.0e-2
pMin = 5.0e-6
alph = 0.75
Nb = 35
T0 = 0; Tf = 1000.0
LW = 2
doNorm = True
doLog = True

#Non-Log
# pMax = 1.0e-2
# pMin = 0
# alph = 0.75
# Nb = 75
# T0 = 0; Tf = 450.0
# LW = 2
# doNorm = True
# doLog = False

bins = np.linspace(T0,Tf,Nb)

fig = plt.figure(figsize=figSize)
#plt.hist(aTms[0],bins,alpha=alph,normed=doNorm,log=doLog)
#plt.hist(aTms[1],bins,alpha=alph,normed=doNorm,log=doLog)
#plt.hist(aTms,bins,normed=doNorm,log=doLog)
lfmv.showDualHist(aTms[0],aTms[1],bins,alph=0.75,Norm=True,Cum=False,LogH=doLog)
plt.legend(Leg)
plt.xlabel("Time in Magnetosheath [s]")
plt.ylabel("Density")
plt.xlim(T0,Tf)
plt.ylim(pMin,pMax)
#plt.axvline(aTbar[0],color='b',linewidth=LW)
#plt.axvline(aTbar[1],color='g',linewidth=LW)

plt.savefig("msTime.png",dpi=figQ)
plt.close()

