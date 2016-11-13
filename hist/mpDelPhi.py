#Calculate histograms of Delta-Phi
#Only bother with ions

import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm

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
		fIn = dirStub + "/" + spcs[i] + "." + fileStub
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


# Nb = 40
# N0 = -60; N1 = 120
# bins = np.linspace(N0,N1,Nb)
# doNorm = True
# doLog = False

# pMax = 0.05
# #Delta-phi MP
# fig = plt.figure(1, figsize=(15,10))
# bins = np.linspace(N0,N1,Nb)
# nxFig = plt.hist(mpDp,bins,normed=doNorm,log=doLog)
# plt.legend(Leg)
# plt.xlim((N0,N1))
# plt.ylim((0,pMax))
# #plt.xlabel(r"$\Delta \phi = \phi_{L} - \phi_{F}$" + "\nAzimuthal Transit Between First/Last MPX",fontsize="x-large")
# plt.xlabel("Azimuthal Transit Between First/Last MPX",fontsize="x-large")
# plt.ylabel('Population',fontsize="x-large")
# plt.savefig("DelPMP.png")
# plt.close('all')

# #Delta-phi MS
# fig = plt.figure(1, figsize=(15,10))
# bins = np.linspace(N0,N1,Nb)
# nxFig = plt.hist(msDp,bins,normed=doNorm,log=doLog)
# plt.legend(Leg)
# plt.xlim((N0,N1))
# plt.ylim((0,pMax))
# plt.xlabel("Azimuthal Transit in Magnetosheath",fontsize="x-large")
# plt.ylabel('Population',fontsize="x-large")
# plt.savefig("DelPMS.png")
# plt.close('all')

# #Delta-phi total
# pMax = 0.03
# #fig = plt.figure(1, figsize=(10,10))
# bins = np.linspace(N0,N1,Nb)
# nxFig = plt.hist(mDp,bins,normed=doNorm,log=doLog)
# plt.legend(Leg)
# plt.xlim((N0,N1))
# plt.ylim((0,pMax))
# plt.xlabel("Azimuthal Transit After First MPX",fontsize="x-large")
# plt.ylabel('Population',fontsize="x-large")
# plt.savefig("TotDelP.png")
# plt.close('all')

# #plt.savefig("MPxDelP.png")


# Nx = 200
# Ny = 200
# fig = plt.figure(1, figsize=(20,10))
# gs = gridspec.GridSpec(2, 2)#,height_ratios=[5,1])
# for i in range(Ns):
# 	ax = plt.subplot(gs[i,0])
# 	plt.hist2d(mpDp[i],msDp[i],[Nx,Ny],normed=True,norm=LogNorm(1.0e-5,5.0e-3))
# 	plt.title(Leg[i])
# 	#plt.colorbar()
# 	plt.axis('scaled')
# 	plt.xlim([-60,120])
# 	plt.ylim([-40,80])
# 	#plt.ylabel(r"$\Delta \phi = \phi_{L} - \phi_{F}$",fontsize="x-large")
# 	#plt.xlabel(r"$\phi_{F}$",fontsize="x-large")
# 	plt.xlabel("Azimuthal Transit Between First/Last MPX",fontsize="large")
# 	plt.ylabel("Azimuthal Transit After Last MPX",fontsize="large")

# #plt.show()
# ax = plt.subplot(gs[1,1])
# plt.colorbar(orientation="horizontal")
# #plt.show()

# plt.savefig("DelPhi2D.png")

