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

#doCalc = True
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

pMax = 0.01
Nb = 45
T0 = 0; Tf = 600
LW = 2
doNorm = True
doLog = False
bins = np.linspace(T0,Tf,Nb)
dtFig = plt.hist(aTms,bins,normed=doNorm,log=doLog)
plt.legend(Leg)
plt.xlabel("Time in Magnetosheat [s]")
plt.ylabel("Density")
plt.ylim(0,pMax)
plt.axvline(aTbar[0],color='b',linewidth=LW)
plt.axvline(aTbar[1],color='g',linewidth=LW)

plt.savefig("DelTms.png")
plt.close()


# #Sheath time 


# #Time on MP
# Nb = 50
# T0 = 0; Tf = 350
# doNorm = True
# doLog = False
# pMax = 0.015
# bins = np.linspace(T0,Tf,Nb)
# dtFig = plt.hist(aDelTmp[0:2],bins,normed=doNorm,log=doLog)
# plt.legend(Leg)
# plt.xlabel("Time between first and last MPX [s]")
# plt.ylabel("Fraction")
# plt.ylim(0,pMax)
# plt.savefig("DelTmp.png")
# plt.close()

# #2D histogram of time

# Nb = 40
# xBin = np.linspace(0,350,Nb)
# yBin = np.linspace(0,250,Nb)
# for s in range(2):
# 	plt.hist2d(aDelTmp[s],aDelT[s],[xBin,yBin],normed=True,norm=LogNorm(1.0e-6,5e-4))#(1.0e-6,1.0e-2))
# 	plt.xlim(0,350)
# 	plt.ylim(0,250)
# 	plt.axis('scaled')
# 	plt.xlabel('Between First/Last MPX [s]')
# 	plt.ylabel('After Last MPX [s]')
# 	plt.colorbar()
# 	plt.savefig("DelT2D.%s.png"%spcs[s])
# 	plt.close('all')
