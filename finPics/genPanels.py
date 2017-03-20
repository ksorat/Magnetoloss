#Generate all the panel figures for paper

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Wedge
from matplotlib.lines import Line2D

#Figures
#1: Main Panel
#2: KHI Panel
#3: Rewind Panel
#4: O+ trajectories
#5: Loss over time figure

doFig1 = False
doFig2 = False
doFig3 = False
doFig4 = True
doFig5 = True

fOuts = ["fpPanel.png","khiPanel.png","rewePanel.png","OTrjs.png","LossT.png"]

figSizeFull = (12,12) #For full panel
figSizeHalf = (6,6)

figQ = 300 #DPI

#Some global color info
fldBds = [-35,35]
fldCMap = "RdGy_r"
fldOpac = 0.5

pBds = [50,150]
pCMap = "cool"
pSize = 2; pMark = 'o'; pLW = 0.2

#Default font size info
LabFS = "large"
TitFS = "large"
cbFS = "medium"
LegFS = "large"

#Some global file info
#Locations
RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data"
vtiDir = RootDir + "/" + "eqSlc"
h5pDir = RootDir + "/" "H5p"

#Global initialization
lfmv.ppInit()
def getFld(vtiDir,t,dt=10.0,eqStub="eqSlc",tSlc=None):
        if (tSlc is None):
                tSlc = np.int(t/dt)

        vtiFile = vtiDir + "/" + eqStub + ".%04d.vti"%(tSlc)
        print("Reading %s"%vtiFile)

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


#Start figure making!
#-------------------------------------------

#Figure 1 (main panel figure)
if (doFig1):
	fOut = fOuts[0]

	#Stub info/times to plot
	Spcs = ["H+","O+","e-"]
	h5ps = ["H.100keV.h5part","O.100keV.h5part","e.100keV.h5part"]
	Ts = [500,1000,2500,3500]
	fldDomX = [-15,13]
	fldDomY = [-20,20]
	HRs = [1,1,1,0.1,0.075]
	Ns = len(Spcs)
	Nt = len(Ts)
	
	fig = plt.figure(figsize=figSizeFull)#,tight_layout=True)
	gs = gridspec.GridSpec(Ns+2,Nt,height_ratios=HRs,hspace=0.1,wspace=0.1)#,bottom=0.05)

	wedgeLW = 1.5
	for t in range(Nt):
		xi,yi,dBz = getFld(vtiDir,Ts[t])
		for s in range(Ns):
			
			Ax = fig.add_subplot(gs[s,t])
			if (t == 0):
				plt.ylabel(Spcs[s],fontsize=LabFS)
			elif (t == Nt-1):
				plt.ylabel("GSM-Y [Re]",fontsize=LabFS)
				Ax.yaxis.tick_right()
				Ax.yaxis.set_label_position("right")
			else:
				plt.setp(Ax.get_yticklabels(),visible=False)
	
	
			if (s < Ns-1):
				plt.setp(Ax.get_xticklabels(),visible=False)
			else:
				plt.xlabel('GSM-X [Re]',fontsize=LabFS)
			if (s == 0):
				plt.title("T = %d [s]"%Ts[t],fontsize=TitFS)
	
			if (s==0 and t==0):
				#Add initial condition wedge
				icW = Wedge(0,10,140,220,width=5,fill=False,ec='springgreen',linewidth=wedgeLW)
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
	cb1.set_label("Residual Vertical Field [nT]",fontsize=cbFS)
	
	AxC2 = fig.add_subplot(gs[-1,2:4])
	vNorm2 = mpl.colors.Normalize(vmin=pBds[0],vmax=pBds[1])
	cb2 = mpl.colorbar.ColorbarBase(AxC2,cmap=pCMap,norm=vNorm2,orientation='horizontal')
	cb2.set_label("Particle Energy [keV]",fontsize=cbFS)
	
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

#-------------------------------------------
#Figure 2 (KHI panel figure)
if (doFig2):
	fOut = fOuts[1]
	Spcs = ["H+","e-"]
	h5ps = ["H.100keV.h5part","e.100keV.h5part"]
	fldDomX = [-5,10]
	Mrk = [-60,60] #Which lines to mark
	RMax = 20
	RMin = 1.05
	lLW = 1.5
	Ts = 3100 #Time to use for data

	#Setup pic
	fig = plt.figure(figsize=figSizeFull)#,tight_layout=True)
	gs = gridspec.GridSpec(1,2,hspace=0.1,wspace=0.1)

	#Get field data and then loop over species
	Ns = len(Spcs)
	#Get field data
	xi,yi,dBz = getFld(vtiDir,Ts)
	radScl = np.pi/180.0

	for s in range(Ns):
		Ax = fig.add_subplot(gs[0,s])


		#Make line
		Phi = radScl*Mrk[s]
		p0 = (RMin*np.cos(Phi),RMin*np.sin(Phi))
		p1 = (RMax*np.cos(Phi),RMax*np.sin(Phi))
		khiLine = [p0,p1]
		(ln_xs, ln_ys) = zip(*khiLine)

		#Now do KHI marker
		Ax.add_line(Line2D(ln_xs,ln_ys,linewidth=lLW,color='springgreen'))

		#Fields
		fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud')

		#Particles
		xs,ys,zs = getPs(h5pDir,h5ps[s],Ts)
		pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=pBds[0],vmax=pBds[1],cmap=pCMap,linewidth=pLW)

		#Extra
		lfmv.addEarth2D()
		plt.axis('scaled')
		if (s==0):
			fldDomY = [-15,0]
			plt.ylabel('GSM-Y [Re]',fontsize=LabFS)
		else:
			fldDomY = [0,15]
			plt.ylabel('GSM-Y [Re]',fontsize=LabFS)
			Ax.yaxis.tick_right()
			Ax.yaxis.set_label_position("right")

		plt.xlim(fldDomX)
		plt.ylim(fldDomY)
		plt.xlabel('GSM-X [Re]',fontsize=LabFS)
		
		plt.title(Spcs[s],fontsize=TitFS)

	#Finish up
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)
#-------------------------------------------
#Figure 3 (Rewind panel figure)
if (doFig3):
	fOut = fOuts[2]
	figSizeRew = (12,4) #For full panel

	xRootDir = os.path.expanduser('~') + "/Work/Magnetoloss/rewe" #Data
	xvtiDir = xRootDir + "/" + "eqSlc"
	xh5pDir = xRootDir + "/" "H5p"

	Spcs = ["$K_{0} = 50$ [keV]","$K_{0} = 100$ [keV]"]
	h5ps = ["eRewind.50keV.h5part","eRewind.100keV.h5part"]
	Nt = 5
	T0 = 3750
	dT = 75
	fldDomX = [-10,10]
	fldDomY = [5,20]

	#Times to plot
	Ts = np.zeros(Nt,dtype=np.int)
	Ts = T0-dT*np.arange(Nt)

	#Time slices to use
	Tslcs = (0.5*(T0-Ts) ).astype(int)
	print(Tslcs)
	Ns = len(Spcs)
	Nt = Nt

	fig = plt.figure(figsize=figSizeRew)#,tight_layout=True)
	gs = gridspec.GridSpec(Ns,Nt,hspace=0.1,wspace=0.1)#,bottom=0.05)

	for t in range(Nt):
		xi,yi,dBz = getFld(xvtiDir,Ts[t],tSlc=Tslcs[t])
		for s in range(Ns):
			Ax = fig.add_subplot(gs[s,t])

			if (t == 0):
				plt.ylabel(Spcs[s],fontsize=LabFS)
			elif (t == Nt-1):
				plt.ylabel("GSM-Y [Re]",fontsize=LabFS)
				Ax.yaxis.tick_right()
				Ax.yaxis.set_label_position("right")
			else:
				plt.setp(Ax.get_yticklabels(),visible=False)

			if (s < Ns-1):
				plt.setp(Ax.get_xticklabels(),visible=False)
			else:
				plt.xlabel('GSM-X [Re]',fontsize=LabFS)
			if (s == 0):
				plt.title("T = %d [s]"%(Ts[t]-T0),fontsize=TitFS)

			#Now do plots
			fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)
			lfmv.addEarth2D()

			#Now do particles
			xs,ys,zs = getPs(xh5pDir,h5ps[s],Ts[t],tSlc=Tslcs[t])
			pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=pBds[0],vmax=pBds[1],cmap=pCMap,linewidth=pLW)

			#Bounds
			plt.axis('scaled')
			plt.xlim(fldDomX); plt.ylim(fldDomY)

	#Finish up
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)
#-------------------------------------------
#Figure 4 (O+ trajectory figures)
def getPTop(h5pFile,pId):
	
	t,x = lfmpp.getH5pid(h5pFile,"x",pId)
	t,y = lfmpp.getH5pid(h5pFile,"y",pId)
	
	t,Om = lfmpp.getH5pid(h5pFile,"Om",pId)
	t,Op = lfmpp.getH5pid(h5pFile,"Op",pId)
	Omp = (Om+Op)

	return x,y,Omp

def getMPX(h5pFile,IDs):
	Np = len(IDs)
	tSlcs = np.zeros(Np,dtype=np.int)
	for n in range(Np):
		pID = IDs[n]
		t,tCr = lfmpp.getH5pid(h5pFile,"tCr",pID)
		I = (tCr>0).argmax()
		tSlcs[n] = I
	return tSlcs

if (doFig4):
	fOut = fOuts[3]
	h5pFile = h5pDir + "/" + "O.100keV.h5part"
	lLw = 0.25
	Nx = 3; Ny = 4
	Nk = Nx*Ny
	DomX = [-15,12]
	DomY = [-20,20]

	#IDs calculated elsewhere
	IDs = [88748,18090,9935,50193,77676,98578,72886,71222,13845,50715,11522,11530]
	tSlcs = getMPX(h5pFile,IDs)

	#Gridspec defaults
	hRat = list(4*np.ones(Nx+1))
	hRat[0] = 0.2

	fig = plt.figure(figsize=figSizeFull)#,tight_layout=True)
	gs = gridspec.GridSpec(Nx+1,Ny,height_ratios=hRat)

	n = 0
	for i in range(1,Nx+1):
		for j in range(Ny):
			
			Ax = fig.add_subplot(gs[i,j])
	
			if (i == Nx):
				plt.xlabel("GSM-X [Re]",fontsize=LabFS)
			else:
				plt.setp(Ax.get_xticklabels(),visible=False)
			if (j == 0):
				plt.ylabel("GSM-Y [Re]",fontsize=LabFS)
			else:
				plt.setp(Ax.get_yticklabels(),visible=False)
	
			xi,yi,dBz = getFld(vtiDir,tSlcs[n])
			fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)

			#Add figure label
			subLab = chr(ord('a')+n)+")"
			print(subLab)
			Ax.text(7.5,15,subLab,fontsize=LabFS)
			lfmv.addEarth2D()
	
			#Now do particles
			xs,ys,zs = getPTop(h5pFile,IDs[n])
	
			pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=0,vmax=1,cmap=pCMap,linewidth=pLW)
			
			plt.plot(xs,ys,'w-',linewidth=lLw)
			plt.axis('scaled')
			plt.xlim(DomX); plt.ylim(DomY)

			n = n+1
	#Finish up
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

#-------------------------------------------
#Figure 5, loss over time
if (doFig5):
	fOut = fOuts[4]

	fileStub = "100keV.h5part"
	
	spcs = ["H","O","e"]
	Leg = ["H+","O+","e-"]
	fig = plt.figure(figsize=figSizeHalf)
	Ns = len(spcs)

	for i in range(Ns):
		fIn = h5pDir + "/" + spcs[i] + "." + fileStub
		t,mpTp = lfmpp.getH5p(fIn,"mp")
		Np = mpTp.shape[1]
		mpT = mpTp.sum(axis=1)
		print(Np)
		plt.plot(t,mpT/Np)	
	plt.legend(Leg,loc='lower right',fontsize=LegFS)
	plt.xlabel('Time [s]',fontsize=LabFS)
	plt.ylabel('Cumulative Loss Fraction',fontsize=LabFS)

	#Finish up
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)
