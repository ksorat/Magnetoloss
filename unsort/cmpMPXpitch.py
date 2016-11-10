import argparse
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

def h2d(x,y,Nb):
        Np = len(x)
        H,xedges,yedges = np.histogram2d(x,y,bins=Nb)
        H = np.rot90(H)
        H = np.flipud(H)
        #H = H/Np
        H = np.ma.masked_where(H==0,H)
        return xedges,yedges,H

dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O","e"]
cMap="jet"
xbins = 50
ybins = 50
Nb = 50

Ns = len(spcs)
fig = plt.figure(1, figsize=(10, 10))
aCut = 80
cMin = 1; cMax = 200
cNorm = LogNorm(vmin=cMin,vmax=cMax)

for i in range(Ns):
	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	pid, alph0 = lfmpp.getPitch(fIn)

	Rf,Pf,Lf = lfmpp.getSphLoss(fIn,inMask=(alph0>=aCut))
	Ri,Pi,Li = lfmpp.getSphLoss(fIn,inMask=(alph0<aCut))
	
	Np = 2*i+1
	plt.subplot(Ns,2,Np)
	xe,ye,Hi = h2d(Pi,Li,Nb)
	plt.pcolormesh(xe,ye,Hi,norm=cNorm)
	cbar = plt.colorbar()
	plt.xlim( (-180,180) )
	plt.ylim( (-60,60) )

	plt.subplot(Ns,2,Np+1)
	#plt.hist2d(Pf,Lf,[xbins,ybins],cmap=cMap,normed=False,cmin=0,cmax=200)
	xe,ye,Hf = h2d(Pf,Lf,Nb)
	plt.pcolormesh(xe,ye,Hf,norm=cNorm)
	cbar = plt.colorbar()
	plt.xlim( (-180,180) )
	plt.ylim( (-60,60) )


plt.suptitle("MP Losses: H,O,e (Rows) / A<80, A>=80 (Cols)")
plt.savefig("mpLoss.alphCmp.png")
plt.show()