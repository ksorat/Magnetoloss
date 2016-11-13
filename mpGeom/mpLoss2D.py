import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#Figure defaults
figSize = (10,10)
figQ = 300 #DPI
figStub = "mpLoss"
doFirst = False
cAx=[1.0e-6,1.0e-3]
cMap="jet"
Np = 50
Nl = 50

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

pBin = np.linspace(-180,180,Np)
lBin = np.linspace(-60,60,Nl)

for i in range(Ns):
	fIn = RootDir + spcs[i] + "." + fileStub
	figName = figStub + "." + spcs[i] + ".png"
	if (doFirst):
		R,Phi,Lambda,Tl = lfmpp.getSphLoss1st(fIn)
	else:
		R,Phi,Lambda = lfmpp.getSphLoss(fIn)
	fig = plt.figure(figsize=figSize,tight_layout=True)
	gs = gridspec.GridSpec(2,1,height_ratios=[1,1])

	#1D histogram
	Ax1D = fig.add_subplot(gs[0,0])
	Ax1D.hist(Phi,Lambda,pBin,color='blue',normed=True)

	#2D histogram
	Ax2D = fig.add_subplot(gs[1,0])
	Ax2D.hist2d(Phi,Lambda,[pBin,lBin],cmap=cMap,normed=True,norm=LogNorm(vmin=cAx[0],vmax=cAx[1]) )
	plt.savefig(figName,dpi=figQ)
	plt.close('all')
