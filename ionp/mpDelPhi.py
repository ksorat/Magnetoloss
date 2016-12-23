#Calculate histograms of Delta-Phi
#Only bother with ions

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm

def lastPhi(fIn):
	isOut = lfmpp.getOut(fIn)
	ids,x = lfmpp.getH5pFin(fIn,"x",Mask=isOut)
	ids,y = lfmpp.getH5pFin(fIn,"y",Mask=isOut)
	pBX = np.arctan2(y,x)*180.0/np.pi
	return pBX

figSize = (8,8)
figQ = 300 #DPI

lfmv.initLatex()
msDataFile = "msIonDP.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]
Ns = len(spcs)

aDPms = []
aP0 = []
if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		aDPms = pickle.load(f)
		aP0 = pickle.load(f)
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
		aP0.append(PhiMP0)
		
	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(aDPms,f)
		pickle.dump(aP0,f)

# pMax = 0.025
# Nb = 40
# N0 = -60; N1 = 120
# bins = np.linspace(N0,N1,Nb)

pMax = 0.025
pMin = 1.0e-5
Nb = 30
N0 = -100; N1 = 160
bins = np.linspace(N0,N1,Nb)

doNorm = True
doLog = True

fig = plt.figure(figsize=figSize)
plt.hist(aDPms,bins,normed=doNorm,log=doLog)
plt.legend(Leg)
plt.xlabel("Azimuthal Transit in Magnetosheath [$^{\circ}$]")
plt.ylabel("Density")
plt.xlim(N0,N1)
plt.ylim(pMin,pMax)

plt.savefig("msDelP.png",dpi=figQ)
plt.close('all')

#Do Phi_Init vs. DelPhi histogram panel
cMap = "summer"
PhiI = np.linspace(-180,180,100)
DelPhi = np.linspace(-90,160,100)
vNorm = LogNorm(vmin=1.0e-5,vmax=1.0e-2)

fig = plt.figure(figsize=figSize)
gs = gridspec.GridSpec(1,3,width_ratios=[5,5,1])

for n in range(2):
	Ax = fig.add_subplot(gs[n])
	plt.hist2d(aP0[n],aDPms[n],[PhiI,DelPhi],normed=True,norm=vNorm,cmap=cMap)
	plt.axis('scaled')

Ax = fig.add_subplot(gs[n+1])
cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='vertical')

plt.savefig("piVdp.png",dpi=figQ)
plt.close('all')