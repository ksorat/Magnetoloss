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

lfmv.ppInit()
msDataFile = "msIonDP.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]
Ns = len(spcs)

aDPms = []
aP0 = []
aPF = []

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		aDPms = pickle.load(f)
		aP0 = pickle.load(f)
		aPF = pickle.load(f)
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
		aPF.append(PhiBX)
		
	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(aDPms,f)
		pickle.dump(aP0,f)
		pickle.dump(aPF,f)

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
cMap = "viridis"
piB = [-120,120]
Np = 100
dpB = [-90,150]
pfB = [-120,120]

Ndp = 100
PhiI = np.linspace(piB[0],piB[1],Np)
DelPhi = np.linspace(dpB[0],dpB[1],Np)
PhiF = np.linspace(pfB[0],pfB[1],Np)

vNorm = LogNorm(vmin=5.0e-6,vmax=5.0e-4)

figSize = (8,4.5)
fig = plt.figure(figsize=figSize)

gs = gridspec.GridSpec(2,2,height_ratios=[20,1])#,bottom=0.05,top=0.99,wspace=0.2,hspace=0.05)

for n in range(2):
	Ax = fig.add_subplot(gs[0,n])
	#plt.hist2d(aP0[n],aDPms[n],[PhiI,DelPhi],normed=True,norm=vNorm,cmap=cMap)
	plt.hist2d(aP0[n],aPF[n],[PhiI,PhiF],normed=True,norm=vNorm,cmap=cMap)
	plt.axis('scaled')
	plt.xlim(piB[0],piB[1])
	plt.ylim(pfB[0],pfB[1])
	#plt.ylim(dpB[0],dpB[1])
	
	lfmv.ax2mlt(Ax,np.arange(-120,121,60),doX=True)
	lfmv.ax2mlt(Ax,np.arange(-120,121,60),doX=False)
	#plt.xlabel('$\phi_{mp} [^{\circ}]$')
	plt.xlabel("Magnetosheath First Contact [MLT]")
	if (n == 0):
		#plt.ylabel('$\Delta \phi_{ms}$')
		#plt.ylabel('$\phi_{F} [^{\circ}]$')
		plt.ylabel("Last Position [MLT]")
	else:
		plt.setp(plt.gca().get_yticklabels(),visible=False)
	plt.tick_params(axis='both', which='major', labelsize=6)	
	plt.title(Leg[n])

Ax = fig.add_subplot(gs[1,:])
cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
cb.set_label("Density")

plt.savefig("piVdp.png",dpi=figQ)
plt.close('all')