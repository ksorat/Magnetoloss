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
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

dirStub = "/glade/u/home/skareem/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["Hydrogen","Oxygen"]

Ns = len(spcs)

mpDp = []
pMP1 = []
pMP0 = []
msDp = []
pBX = []
mDp = []
LogScl = LogNorm(1,500)


for i in range(Ns):
	#xBin = np.linspace(-180,180,100)
	xBin = np.linspace(-60,60,100)
	yBin = np.linspace(0,30,30)

	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	print("Reading %s"%(fIn))
	print("Species %s"%(Leg[i]))
	isOut = lfmpp.getOut(fIn)
	pid, NumX = lfmpp.countMPX(fIn,isOut)
	R, PhiMP0, LambdaF, Tmp = lfmpp.getSphLoss1st(fIn)
	R,PhiMP1,LambdaL = lfmpp.getSphLoss(fIn)
	PhiBX = lastPhi(fIn)

	pMP0.append(PhiMP0)
	pMP1.append(PhiMP1)
	mpDp.append(PhiMP1-PhiMP0)
	pBX.append(PhiBX)
	msDp.append(PhiBX-PhiMP1)

	mDp.append(PhiBX-PhiMP0)
Nb = 40
N0 = -60; N1 = 120
bins = np.linspace(N0,N1,Nb)
doNorm = True
doLog = False

pMax = 0.05



Nx = 200
Ny = 200
fig = plt.figure(1, figsize=(20,10))
gs = gridspec.GridSpec(2, 2)#,height_ratios=[5,1])
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
for i in range(Ns):
	ax = plt.subplot(gs[i,0])
	plt.hist2d(pMP0[i],mpDp[i],[Nx,Ny],normed=True,norm=LogNorm(1.0e-5,5.0e-3))
	plt.title(Leg[i])
	plt.colorbar()
	plt.axis('scaled')
	plt.xlim([-60,120])
	plt.ylim([-40,80])
	plt.ylabel(r"$\Delta \phi = \phi_{L} - \phi_{F}$",fontsize="x-large")
	plt.xlabel(r"$\phi_{I}$",fontsize="x-large")
#plt.show()
ax = plt.subplot(gs[1,1])
plt.colorbar(orientation="horizontal")
#plt.show()

plt.savefig("DelPhi2D.png")

