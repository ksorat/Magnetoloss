import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib.gridspec as gridspec
from scipy import ndimage

#Figure defaults
#figSize = (8,8)
figQ = 300 #DPI


figStub = "lCrit"

cAx=[1.0e-5,1.0e-3]

fMax = 0.015

cMap="viridis"
Np = 50
Nl = 50

xTk = [-135,-90,-45,0,45,90,135]

pSlcs = [0,30,45,60,75,90]

fIn = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/O.100keV.h5part"

lfmv.ppInit()
P0 = -150; P1 = 150
L0 = -60; L1 = 60
pBin = np.linspace(P0,P1,Np)
pC = 0.5*(pBin[0:-1] + pBin[1:])
lBin = np.linspace(L0,L1,Nl)
lC = 0.5*(lBin[0:-1] + lBin[1:])

R,Phi,Lambda = lfmpp.getSphLoss(fIn)
X,pI,lI = np.histogram2d(Phi,Lambda,[pBin,lBin])

Xs = ndimage.filters.gaussian_filter(X,1,mode='nearest')

nS = len(pSlcs)
for i in range(nS):
	pS = pSlcs[i]
	dP = np.abs(pC-pS)
	I = np.abs(pC-pS).argmin()
	labS = "Phi = %d"%(pS)
	plt.plot(lC,Xs[I,:],label=labS)
	Ic = Xs[I,:].argmax()
	print("@ Phi = %d, LamC = %f"%(pS,lC[Ic]))

plt.legend()
plt.savefig("lamCrit.png")
plt.close('all')

