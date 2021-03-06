#Generates panel figure from eq-VTIs and H5p file
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Wedge

def getFld(vtiDir,t,dt=10.0,eqStub="eqSlc",tSlc=None):
	if (tSlc is None):
		tSlc = np.int(t/dt)

	vtiFile = vtiDir + "/" + eqStub + ".%04d.vti"%(tSlc)

	dBz = lfmv.getVTI_SlcSclr(vtiFile).T
	ori,dx,ex = lfmv.getVTI_Eq(vtiFile)
	xi = ori[0] + np.arange(ex[0],ex[1]+1)*dx[0]
	yi = ori[1] + np.arange(ex[2],ex[3]+1)*dx[1]

	return xi,yi,dBz

def getPs(h5pDir,h5pStub,t,dt=10.0,tSlc=None):
	if (tSlc is None):
		tSlc = np.int(t/dt)
	h5pFile = h5pDir + "/" + h5pStub
	t,xeq = lfmpp.getH5pT(h5pFile,"xeq",tSlc)
	t,yeq = lfmpp.getH5pT(h5pFile,"yeq",tSlc)
	t,kev = lfmpp.getH5pT(h5pFile,"kev",tSlc)

	t,mp = lfmpp.getH5pT(h5pFile,"mp",tSlc)
	t,tl = lfmpp.getH5pT(h5pFile,"tl",tSlc)
	t,atm = lfmpp.getH5pT(h5pFile,"atm",tSlc)

	In = (atm+tl+mp) < 0.5
	xeq = xeq[In]
	yeq = yeq[In]
	kev = kev[In]
	
	return xeq,yeq,kev

Spcs = ["e-"]
h5ps = ["eRewind.100keV.h5part"]
h5ps = ["eRewind.50keV.h5part"]

figName = "rewePanel.png"
doFig = True
Nt = 5
T0 = 3750
dT = 75
dT = 125

Ts = np.zeros(Nt,dtype=np.int)
Ts = T0-dT*np.arange(Nt)

figSize = (10,2.5)
figQ = 300 #DPI

#Plot bounds fields/particles (nT/keV), plot details
fldBds = [-35,35]
fldCMap = "RdGy_r"
fldOpac = 0.5
fldDomX = [-10,10]
fldDomY = [5,20]

pBds = [50,150]
pCMap = "cool"
pSize = 2; pMark = 'o'; pLW = 0.2

#Slices
Tslcs = (0.5*(T0-Ts) ).astype(int)

#Locations
RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/rewe" #Data
vtiDir = RootDir + "/" + "eqSlc"
h5pDir = RootDir + "/" "H5p"

#Do figures
lfmv.initLatex()
fig = plt.figure(figsize=figSize)

Ns = len(Spcs)

gs = gridspec.GridSpec(Ns,Nt,left=0.05,right=0.95)

for t in range(Nt):
	if (doFig): xi,yi,dBz = getFld(vtiDir,Ts[t],tSlc=Tslcs[t])
	for s in range(Ns):
		
		Ax = fig.add_subplot(gs[s,t])
		if (t == 0):
			plt.ylabel(Spcs[s],fontsize="large")
		elif (t == Nt-1):
			plt.ylabel("GSM-Y [Re]")
			Ax.yaxis.tick_right()
			Ax.yaxis.set_label_position("right")
		else:
			plt.setp(Ax.get_yticklabels(),visible=False)


		if (s < Ns-1):
			plt.setp(Ax.get_xticklabels(),visible=False)
		else:
			plt.xlabel('GSM-X [Re]')
		if (s == 0):
			plt.title("T = %d [s]"%(Ts[t]-T0))

		if (doFig): fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)
		
		lfmv.addEarth2D()

		#Now do particles
		if (doFig):
			xs,ys,zs = getPs(h5pDir,h5ps[s],Ts[t],tSlc=Tslcs[t])
			pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=pBds[0],vmax=pBds[1],cmap=pCMap,linewidth=pLW)
		plt.axis('scaled')
		plt.xlim(fldDomX); plt.ylim(fldDomY)
		
plt.savefig(figName,dpi=figQ)

