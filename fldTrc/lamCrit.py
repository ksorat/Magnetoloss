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


figStub = "lCrit"

cAx=[1.0e-5,1.0e-3]

fMax = 0.015

cMap="viridis"
Np = 50
Nl = 50

xTk = [-135,-90,-45,0,45,90,135]


fIn = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/O.100keV.h5part"

lfmv.ppInit()
P0 = -150; P1 = 150
L0 = -60; L1 = 60
pBin = np.linspace(P0,P1,Np)
lBin = np.linspace(L0,L1,Nl)

R,Phi,Lambda = lfmpp.getSphLoss(fIn)
X,pI,lI,Im = plt.hist2d(Phi,Lambda,[pBin,lBin],cmap=cMap,normed=True,norm=LogNorm(vmin=cAx[0],vmax=cAx[1]) )
plt.close('all')

