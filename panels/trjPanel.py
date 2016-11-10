#Generates trajectory panel figure

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

def getPTop(h5pFile,pId):
	
	t,x = lfmpp.getH5pid(h5pFile,"x",pId)
	t,y = lfmpp.getH5pid(h5pFile,"y",pId)
	
	t,Om = lfmpp.getH5pid(h5pFile,"Om",pId)
	t,Op = lfmpp.getH5pid(h5pFile,"Op",pId)
	Omp = (Om+Op)

	return x,y,Omp

#Particle data
s0 = 0
SpcsStub = ["O.100kev"]
SpcsLab = ["O+ 100 keV"]
KStubs = [10,25,50]
Kcs = [50,100,200]

#Traj data
IDs = [1335,301,95834,12593,63464,75685]

#Nx = 6; Ny = 5
Nx = 3; Ny = 2
DomX = [-15,12]
DomY = [-20,20]

#Field data
tSlc = 250

#Figure defaults
figSize = (10,10)
figQ = 300 #DPI

#Plot bounds fields/particles (nT/keV), plot details
fldBds = [-35,35]
Nc = 5
fldCMap = "RdGy_r"
fldOpac = 0.5
pCMap = "cool"
pSize = 10; pMark = 'o'; pLW = 1


#Gridspec defaults
hRat = list(4*np.ones(Nx+1))
hRat[0] = 0.25


#Locations
RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data"
vtiDir = RootDir + "/" + "eqSlc"
h5pDir = RootDir + "/" "H5p"

#Spcs = ["H+ 10 keV"]
#h5ps = ["Inj10.All.h5part"]

Nk = len(IDs)
lfmv.initLatex()
xi,yi,dBz = getFld(vtiDir,tSlc)

h5p = h5pDir + "/" + SpcsStub[s0] + ".h5part"
figName = SpcsStub[s0] + ".Trjs.png"
titS = "Sampled High-Transit Trajectories for %s "%(SpcsLab[s0])

fig = plt.figure(figsize=figSize,tight_layout=True)
gs = gridspec.GridSpec(Nx+1,Ny)

n = 0
for i in range(1,Nx+1):
	for j in range(Ny):
		
		Ax = fig.add_subplot(gs[i,j])

		if (i == Nx):
			plt.xlabel("GSM-X [Re]",fontsize="small")
		else:
			plt.setp(Ax.get_xticklabels(),visible=False)
		if (j == 0):
			plt.ylabel("GSM-Y [Re]",fontsize="small")
		else:
			plt.setp(Ax.get_yticklabels(),visible=False)


		fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)
		#fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap)
		#plt.contour(xi,yi,dBz,Bv,cmap=fldCMap)
		lfmv.addEarth2D()

		#Now do particles
		xs,ys,zs = getPTop(h5p,IDs[n])

		pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=0,vmax=1,cmap=pCMap,linewidth=pLW)
		#Leg = ["ID %d\nK = %3.2f (keV)"%(pIds[n],zs.max())]
		#plt.legend(Leg,loc="lower left",fontsize="xx-small",scatterpoints=1,markerscale=0,markerfirst=False,frameon=False)

		plt.plot(xs,ys,'w-',linewidth=0.2)
		plt.axis('scaled')
		plt.xlim(DomX); plt.ylim(DomY)
		plt.tick_params(axis='both', which='major', labelsize=6)
		plt.tick_params(axis='both', which='minor', labelsize=4)
		
		n=n+1
	
plt.suptitle(titS,fontsize="large")
gs.tight_layout(fig)
plt.savefig(figName,dpi=figQ)
plt.close('all')

