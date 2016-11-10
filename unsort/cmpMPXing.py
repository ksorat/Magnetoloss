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
	H = H/Np
	H = np.ma.masked_where(H==0,H)
	return xedges,yedges,H
dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O","e"]
cMap="jet"

Nb = 50
Ns = len(spcs)
fig = plt.figure(1, figsize=(10, 10))
cMin = 1.0e-5
cMax = 1.0e-2

cNorm = LogNorm(vmin=cMin,vmax=cMax)

for i in range(Ns-1):
	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	Rf,Pf,Lf = lfmpp.getSphLoss(fIn)
	Ri,Pi,Li,Tmp = lfmpp.getSphLoss1st(fIn)
	Np = 2*i+1
	plt.subplot(Ns-1,2,Np)
	#plt.hist2d(Pi,Li,[xbins,ybins],cmap=cMap,normed=True,norm=LogNorm())
	xe,ye,Hi = h2d(Pi,Li,Nb)
	plt.pcolormesh(xe,ye,Hi,norm=cNorm)
	cbar=plt.colorbar()
	plt.xlim( (-180,180) )
	plt.ylim( (-90,90) )
	plt.subplot(Ns,2,Np+1)
	#plt.hist2d(Pf,Lf,[xbins,ybins],cmap=cMap,normed=True,norm=LogNorm())
	xe,ye,Hf = h2d(Pf,Lf,Nb)
	plt.pcolormesh(xe,ye,Hf,norm=cNorm)
	cbar=plt.colorbar()
	plt.xlim( (-180,180) )
	plt.ylim( (-90,90) )


plt.suptitle("MP Losses: H,O,e (Rows) / Initial, Final (Cols)")
plt.savefig("mpLoss.TCmp.png")
plt.show()