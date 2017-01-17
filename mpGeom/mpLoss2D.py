import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec

#Figure defaults
#figSize = (8,8)
figQ = 300 #DPI


figStub = "mpLoss"
doFirst = False
doTest = False

cAx=[1.0e-6,1.0e-3]
cAx=[1.0e-5,1.0e-3]

fMax = 0.015

cMap="viridis"
Np = 50
Nl = 50

xTk = [-135,-90,-45,0,45,90,135]
#xTkLab = ["4:00","Dawn","9:00","Noon","15:00","Dusk","20:00"]


RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"
spcs = ["H","O","e"]
Leg = ["H+","O+","e-"]


if (doFirst):
	Ns = len(spcs)-1
	figStub = figStub + ".1st"
	figSize = (12,4)
	fSz = "large"
else:
	Ns = len(spcs)
	figSize = (18,4)
	fSz = "x-large"
mpDF = figStub+".pkl"

if (os.path.isfile(mpDF)):
	print("Loading data")
	with open(mpDF, "rb") as f:
		Phis = pickle.load(f)
		Lambdas = pickle.load(f)

else:
	print("No data file found, calculating")
	Phis = []
	Lambdas = []

	for i in range(Ns):
		
		fIn = RootDir + spcs[i] + "." + fileStub
		if (doTest):
			Phi = np.random.rand(Np)*P1
			Lambda = np.random.rand(Np)*L1
		else:
			if (doFirst):
				R,Phi,Lambda,Tl = lfmpp.getSphLoss1st(fIn)
			else:
				R,Phi,Lambda = lfmpp.getSphLoss(fIn)
		Phis.append(Phi)
		Lambdas.append(Lambda)

	print("Writing pickle")
	with open(mpDF, "wb") as f:
		pickle.dump(Phis,f)
		pickle.dump(Lambdas,f)

lfmv.ppInit()
P0 = -150; P1 = 150
L0 = -60; L1 = 60
pBin = np.linspace(P0,P1,Np)
lBin = np.linspace(L0,L1,Nl)
fig = plt.figure(figsize=figSize)


gs = gridspec.GridSpec(2,Ns,height_ratios=[1,1.5],hspace=0.05,wspace=0.05)

figName = figStub + ".png"
print("Generating %s"%figName)

for i in range(Ns):
	
	Phi = Phis[i]
	Lambda = Lambdas[i]
	
	#1D histogram
	Ax1D = fig.add_subplot(gs[0,i])
	Ax1D.hist(Phi,pBin,color='blue',normed=True)
	

	#2D histogram
	Ax2D = fig.add_subplot(gs[1,i])
	Ax2D.hist2d(Phi,Lambda,[pBin,lBin],cmap=cMap,normed=True,norm=LogNorm(vmin=cAx[0],vmax=cAx[1]) )

	#Axes
	plt.axis('scaled')
	Ax1D.set_xlim(P0,P1)
	Ax1D.set_ylim(0,fMax)
	Ax1D.set_xticks(xTk)
	plt.setp(Ax1D.get_xticklabels(),visible=False)
	Ax1D.set_yticks(np.arange(0.003,fMax+1.0e-8,0.003))
	

	#Ax1D.yaxis.tick_right()
	#Ax1D.yaxis.set_label_position("right")
	
	Ax2D.set_xlim(P0,P1)
	Ax2D.set_ylim(L0,L1)
	Ax2D.set_yticks(np.arange(-40,41,20))

	#Ax2D.set_xticks(xTk)
	#Ax2D.set_xticklabels(xTkLab)
	lfmv.ax2mlt(Ax2D,xTk)
	Ax2D.set_xlabel("Magnetic Local Time")
	Ax2D.text(-120,40,Leg[i],fontsize=fSz)
	if (i==0):
		Ax1D.set_ylabel("Density")
		Ax2D.set_ylabel("Magnetic Latitude [$^{\circ}$]")
	else:
		plt.setp(Ax2D.get_yticklabels(),visible=False)
		plt.setp(Ax1D.get_yticklabels(),visible=False)

#Save
plt.savefig(figName,dpi=figQ)
plt.close('all')
