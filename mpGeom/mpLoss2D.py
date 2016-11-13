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
doTest = True

cAx=[1.0e-6,1.0e-3]
fMax = 0.015

cMap="jet"
Np = 50
Nl = 50

xTk = [-120,-90,-45,0,45,90,120]
xTkLab = ["4:00","Dawn","9:00","Noon","15:00","Dusk","20:00"]


RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"
spcs = ["H","O","e"]
Leg = ["H+","O+","e-"]


if (doFirst):
	Ns = len(spcs)-1
	figStub = figStub + ".1st"
else:
	Ns = len(spcs)
	figSize = (3,9)

lfmv.initLatex()
P0 = -150; P1 = 150
L0 = -60; L1 = 60
pBin = np.linspace(P0,P1,Np)
lBin = np.linspace(L0,L1,Nl)
fig = plt.figure(figSie=figSize)
#fig = plt.figure(figsize=figSize,tight_layout=True)

gs = gridspec.GridSpec(2,Ns,height_ratios=[1,4])

for i in range(Ns):
	
	fIn = RootDir + spcs[i] + "." + fileStub
	figName = figStub + ".png"
	print("Generating %s"%figName)
	if (doTest):
		Phi = np.random.rand(Np)*P1
		Lambda = np.random.rand(Np)*L1
	else:
		if (doFirst):
			R,Phi,Lambda,Tl = lfmpp.getSphLoss1st(fIn)
		else:
			R,Phi,Lambda = lfmpp.getSphLoss(fIn)

	
	
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
	plt.setp(Ax1D.get_xticklabels(),visible=False)
	#Ax1D.yaxis.tick_right()
	#Ax1D.yaxis.set_label_position("right")
	
	Ax2D.set_xlim(P0,P1)
	Ax2D.set_ylim(L0,L1)
	Ax2D.set_xticks(xTk)
	Ax2D.set_xticklabels(xTkLab)
	Ax2D.set_xlabel("Magnetic Local Time")
	
	if (i==0):
		Ax1D.set_ylabel("Fraction")
		Ax2D.set_ylabel("Magnetic Latitude")
	else:
		plt.setp(Ax2D.get_yticklabels(),visible=False)
		plt.setp(Ax1D.get_yticklabels(),visible=False)

#Save
plt.tight_layout()
plt.savefig(figName,dpi=figQ)
plt.close('all')
