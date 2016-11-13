import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec

#Figure defaults
figSize = (8,8)
figQ = 300 #DPI
figStub = "mpLoss"
doFirst = False
cAx=[1.0e-6,1.0e-3]
cMap="jet"
Np = 50
Nl = 50

xTk = [-90,-45,0,45,90]
xTkLab = ["Dawn","9:00","Noon","15:00","Dusk"]


RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"
spcs = ["H","O","e"]
Leg = ["H+","O+","e-"]


if (doFirst):
	Ns = len(spcs)-1
	figStub = figStub + ".1st"
else:
	Ns = len(spcs)

lfmv.initLatex()
P0 = -180; P1 = 180
L0 = -60; L1 = 60
pBin = np.linspace(P0,P1,Np)
lBin = np.linspace(L0,L1,Nl)

for i in range(Ns):
	fIn = RootDir + spcs[i] + "." + fileStub
	figName = figStub + "." + spcs[i] + ".png"
	if (doFirst):
		R,Phi,Lambda,Tl = lfmpp.getSphLoss1st(fIn)
	else:
		R,Phi,Lambda = lfmpp.getSphLoss(fIn)
	#fig = plt.figure(figsize=figSize,tight_layout=True)
	fig = plt.figure()
	plt.axis('scaled')
	gs = gridspec.GridSpec(2,1,height_ratios=[1,4])

	#1D histogram
	Ax1D = fig.add_subplot(gs[0,0])
	Ax1D.hist(Phi,pBin,color='blue',normed=True)
	plt.setp(Ax1D.get_xticklabels(),visible=False)
	Ax1D.set_xlim(P0,P1)

	#2D histogram
	Ax2D = fig.add_subplot(gs[1,0])
	Ax2D.hist2d(Phi,Lambda,[pBin,lBin],cmap=cMap,normed=True,norm=LogNorm(vmin=cAx[0],vmax=cAx[1]) )
	Ax2D.set_xlim(P0,P1)
	Ax2D.set_ylim(L0,L1)
	#Ax2D.set_xticks(xTk)
	#Ax2D.set_xticklabels(xTkLab)

	#Save
	plt.savefig(figName,dpi=figQ)
	plt.close('all')
