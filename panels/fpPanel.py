#Generates panel figure from eq-VTIs and H5p file
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Wedge

def getFld(vtiDir,t,dt=10.0,eqStub="eqSlc"):
	tSlc = np.int(t/dt)
	vtiFile = vtiDir + "/" + eqStub + ".%04d.vti"%(tSlc)

	dBz = lfmv.getVTI_SlcSclr(vtiFile).T
	ori,dx,ex = lfmv.getVTI_Eq(vtiFile)
	xi = ori[0] + np.arange(ex[0],ex[1]+1)*dx[0]
	yi = ori[1] + np.arange(ex[2],ex[3]+1)*dx[1]

	return xi,yi,dBz

def getPs(h5pDir,h5pStub,t,dt=10.0):
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

Spcs = ["H+","O+","e-"]
h5ps = ["H.100keV.h5part","O.100keV.h5part","e.100keV.h5part"]
Ts = [500,1000,2500,3500]

figSize = (11,12)

figQ = 300 #DPI
figName = "fpPanel.png"

#Plot bounds fields/particles (nT/keV), plot details
fldBds = [-35,35]
fldCMap = "RdGy_r"
fldOpac = 0.5
fldDomX = [-15,13]
fldDomY = [-20,20]

pBds = [50,150]
pCMap = "cool"
pSize = 2; pMark = 'o'; pLW = 0.2

#Locations
RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data"
vtiDir = RootDir + "/" + "eqSlc"
h5pDir = RootDir + "/" "H5p"

#Do figures
lfmv.initLatex()
fig = plt.figure(figsize=figSize)#,tight_layout=True)

Ns = len(Spcs)
Nt = len(Ts)

gs = gridspec.GridSpec(Ns+2,Nt,height_ratios=[1,1,1,0.1,0.075],hspace=0.1,wspace=0.1)#,bottom=0.05)

for t in range(Nt):
	xi,yi,dBz = getFld(vtiDir,Ts[t])
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
			plt.title("T = %d [s]"%Ts[t])

		if (s==0 and t==0):
			#Add initial condition wedge
			icW = Wedge(0,10,140,220,width=5,fill=False,ec='springgreen',linewidth=0.75)
			Ax.add_artist(icW)

		fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)
		
		lfmv.addEarth2D()

		#Now do particles
		xs,ys,zs = getPs(h5pDir,h5ps[s],Ts[t])
		pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=pBds[0],vmax=pBds[1],cmap=pCMap,linewidth=pLW)
		plt.axis('scaled')
		plt.xlim(fldDomX); plt.ylim(fldDomY)
		
AxC1 = fig.add_subplot(gs[-1,0:2])
vNorm1 = mpl.colors.Normalize(vmin=fldBds[0],vmax=fldBds[1])
cb1 = mpl.colorbar.ColorbarBase(AxC1,cmap=fldCMap,norm=vNorm1,orientation='horizontal')
cb1.set_label("Residual Vertical Field [nT]",fontsize='small')

AxC2 = fig.add_subplot(gs[-1,2:4])
vNorm2 = mpl.colors.Normalize(vmin=pBds[0],vmax=pBds[1])
cb2 = mpl.colorbar.ColorbarBase(AxC2,cmap=pCMap,norm=vNorm2,orientation='horizontal')
cb2.set_label("Particle Energy [keV]",fontsize='small')

plt.savefig(figName,dpi=figQ)

