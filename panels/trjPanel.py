#Generates trajectory panel figure

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Wedge

def lastPhi(fIn):
	isOut = lfmpp.getOut(fIn)
	ids,x = lfmpp.getH5pFin(fIn,"x",Mask=isOut)
	ids,y = lfmpp.getH5pFin(fIn,"y",Mask=isOut)
	pBX = np.arctan2(y,x)*180.0/np.pi
	return ids,pBX

def getFld(vtiDir,t,dt=10.0,eqStub="eqSlc"):
	tSlc = np.int(t/dt)
	vtiFile = vtiDir + "/" + eqStub + ".%04d.vti"%(tSlc)

	dBz = lfmv.getVTI_SlcSclr(vtiFile).T
	ori,dx,ex = lfmv.getVTI_Eq(vtiFile)
	xi = ori[0] + np.arange(ex[0],ex[1]+1)*dx[0]
	yi = ori[1] + np.arange(ex[2],ex[3]+1)*dx[1]

	return xi,yi,dBz

def getMPX(h5pFile,IDs):
	Np = len(IDs)
	tSlcs = np.zeros(Np,dtype=np.int)
	for n in range(Np):
		pID = IDs[n]
		t,tCr = lfmpp.getH5pid(h5pFile,"tCr",pID)
		I = (tCr>0).argmax()
		tSlcs[n] = I
	return tSlcs

def getPs(h5pFile,pC,Nk):
	isOut = lfmpp.getOut(h5pFile)
	R, PhiMP0, LambdaF, Tmp = lfmpp.getSphLoss1st(h5pFile)
	ids, PhiBX = lastPhi(h5pFile)

	dPhi = PhiBX-PhiMP0

	Ind = (abs(dPhi)>=pC)
	Ntot = Ind.sum()
	ids = ids[Ind]
	print("Found %d values larger than %3.2f"%(Ntot,pC))
	IndR = np.random.choice(Ntot,Nk,replace=False)
	ids = ids[IndR]
	return ids

def getPBlk(h5pFile,pC,Np):
	#Get Np particles for each of 3 types
	#pI:(0,180), (-15,0),(-180,-15)
	#And have dPhi>=pC
	pIL = [0,-45,-180]
	pIH = [180,0.0,-45]
	Nd = len(pIL)

	pIDs = np.zeros(Np*Nd,dtype=np.int)
	isOut = lfmpp.getOut(h5pFile)
	R, PhiMP0, LambdaF, Tmp = lfmpp.getSphLoss1st(h5pFile)
	ids, PhiBX = lastPhi(h5pFile)
	dPhi = PhiBX-PhiMP0
	

	print(PhiMP0.min(),PhiMP0.max())
	print(dPhi.min(),dPhi.max())
	for d in range(Nd):
		pcd = pC[d]
		if (pC[d]>=0):
			IndPC = (dPhi>=pC[d])
		else:
			IndPC = (dPhi<=pC[d])
		
		IndPI = (PhiMP0 >= pIL[d]) & (PhiMP0 <= pIH[d])
		Ind = IndPC & IndPI
		subIDs = ids[Ind]
		subDP = dPhi[Ind]
		#Pick Np randomly
		Ntot = Ind.sum()
		print("Found %d values w/ dP >= %f, and pI between %f and %f"%(Ntot,pC[d],pIL[d],pIH[d]))
		IndR = np.random.choice(Ntot,Np,replace=False)
		rIDs = subIDs[IndR]
		i0 = d*Np
		i1 = i0+Np
		pIDs[i0:i1] = rIDs
		print(rIDs)
		print(subDP[IndR])
	return pIDs

def getPTop(h5pFile,pId):
	
	t,x = lfmpp.getH5pid(h5pFile,"x",pId)
	t,y = lfmpp.getH5pid(h5pFile,"y",pId)
	
	t,Om = lfmpp.getH5pid(h5pFile,"Om",pId)
	t,Op = lfmpp.getH5pid(h5pFile,"Op",pId)
	Omp = (Om+Op)

	return x,y,Omp

#Particle data
s0 = 0
np.random.seed(seed=31337)
SpcsStub = ["O.100keV"]
SpcsLab = ["O+ 100 keV"]
pC = [90,120,-45.0]

#Nx = 6; Ny = 5
#Nx = 2; Ny = 3
Nx = 3; Ny = 4

Nk = Nx*Ny
DomX = [-15,12]
DomY = [-20,20]

#Figure defaults
figSize = (8,8)
figQ = 300 #DPI

#Plot bounds fields/particles (nT/keV), plot details
fldBds = [-35,35]
Nc = 5
fldCMap = "RdGy_r"
fldOpac = 0.5
pCMap = "cool"
pSize = 10; pMark = 'o'; pLW = 0.5


#Gridspec defaults
hRat = list(4*np.ones(Nx+1))
hRat[0] = 0.2


#Locations
RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data"
vtiDir = RootDir + "/" + "eqSlc"
h5pDir = RootDir + "/" "H5p"

#Spcs = ["H+ 10 keV"]
#h5ps = ["Inj10.All.h5part"]

lfmv.initLatex()

h5p = h5pDir + "/" + SpcsStub[s0] + ".h5part"
figName = SpcsStub[s0] + ".Trjs.png"
titS = "Sampled High-Transit Trajectories for %s "%(SpcsLab[s0])

fig = plt.figure(figsize=figSize,tight_layout=True)
gs = gridspec.GridSpec(Nx+1,Ny,height_ratios=hRat)

#Traj data
#IDs = [1335,301,95834,12593,63464,75685]
#IDs = getPs(h5p,pC,Nk)
#IDs = getPBlk(h5p,pC,Ny)
IDs = [88748,18090,9935,50193,77676,98578,72886,71222,13845,50715,11522,11530]
tSlcs = getMPX(h5p,IDs)

print(IDs)
print(tSlcs)


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

		xi,yi,dBz = getFld(vtiDir,tSlcs[n])
		fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)
		#fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap)
		
		#Add figure label
		subLab = chr(ord('a')+n)+")"
		print(subLab)
		Ax.text(7.5,15,subLab,fontsize="large")
		lfmv.addEarth2D()

		#Now do particles
		xs,ys,zs = getPTop(h5p,IDs[n])

		pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=0,vmax=1,cmap=pCMap,linewidth=pLW)
		
		plt.plot(xs,ys,'w-',linewidth=0.2)
		plt.axis('scaled')
		plt.xlim(DomX); plt.ylim(DomY)
		plt.tick_params(axis='both', which='major', labelsize=6)
		plt.tick_params(axis='both', which='minor', labelsize=4)
		
		n=n+1
	
plt.suptitle(titS,fontsize="large")
#gs.tight_layout(fig)
plt.savefig(figName,dpi=figQ)
plt.close('all')

