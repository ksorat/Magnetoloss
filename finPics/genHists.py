#Generate history type figures for paper
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm
from matplotlib.patches import Wedge

#Figures
#1: Polar EQX in sheath
#2: Sheath time
#3: Azimuthal transit
#4: Last MLT MPX 2D
#5: First MLT MPX 2D

doFig1 = False
doFig2 = False
doFig3 = False
doFig4 = False
doFig5 = True

fOuts = ["msRad.png","msTime.png","piVdp.png","mpLoss.png","mpLoss1st.png"]

figSizeFull = (12,12) #For full panel
figSizeHalf = (6,6)


figQ = 300 #DPI

#Default font size info
LabFS = "large"
TitFS = "large"
cbFS = "medium"
LegFS = "large"
dLabFS = "medium"


#Global initialization
lfmv.ppInit()
d2rad = np.pi/180.0

#Start figure making!
#Use pickles when possible
#-------------------------------------------
#Figure 1 (polar EQX)
if (doFig1):
	fOut = fOuts[0]
	msDataFile = "msIonR.pkl"
	spcs = ["H","O"]
	Leg = ["H+","O+"]
	doScl = False
	
	Ns = len(spcs)

	if (os.path.isfile(msDataFile)):
		print("Loading data")
		with open(msDataFile, "rb") as f:
			Phis = pickle.load(f)
			Rs = pickle.load(f)
	else:
		print("No data file found!")

	#Make polar histograms
	figSize = (12,6)

	Np = 200
	Nr = 200
	vNorm = LogNorm(vmin=1.0e-2,vmax=5.0e+0)
	vNormScl = LogNorm(vmin=1.0e-3,vmax=5.0e-1)
	
	cMap = "viridis"
	phiB = d2rad*np.linspace(-160,160,Np+1)
	rB = np.linspace(5,22.5,Nr+1)
	mTks = np.arange(-135,180,45)
	
	print(mTks)

	PP,RR = np.meshgrid(phiB,rB)
	
	phiC = 0.5*(phiB[0:-1] + phiB[1:])
	rC = 0.5*(rB[0:-1] + rB[1:])
	#Get volume elements
	dp = phiB[1]-phiB[0]
	dV = np.zeros((Nr,Np))
	for i in range(Nr):
		for j in range(Np):
			dV[i,j] = rC[i]*dp
	
	fig = plt.figure(figsize=figSize)
	
	gs = gridspec.GridSpec(3,Ns,height_ratios=[20,1,1])
	
	for n in range(Ns):
		Ax = fig.add_subplot(gs[0,n],projection='polar')
		N,a,b = np.histogram2d(Rs[n],Phis[n],[rB,phiB],normed=True)
		f = N/dV
		if (doScl):
			vNorm = vNormScl
			for i in range(Np):
				Fp = f[:,i].sum()
				if (Fp>0):
					f[:,i] = f[:,i]/Fp
					
		Ax.pcolormesh(PP,RR,f,cmap=cMap,shading='flat',norm=vNorm)
		E = plt.Circle((0, 0), 1.0, transform=Ax.transData._b, color="black", alpha=1)
		Ax.add_artist(E)
	
		Ax.set_rlabel_position(210)
		Ax.grid(True)
		lfmv.ax2mlt(Ax,mTks,doX=True,Polar=True)
		plt.xlabel(Leg[n],fontsize=LabFS)

	#Do colorbar
	Ax = fig.add_subplot(gs[-1,:])
	cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
	cb.set_label("Density",fontsize=LabFS)
	
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

#-------------------------------------------
#Figure 2 (magnetosheath time)
if (doFig2):
	fOut = fOuts[1]
	msDataFile = "msIonT.pkl"
	spcs = ["H","O"]
	Leg = ["H+","O+"]
	
	Ns = len(spcs)

	if (os.path.isfile(msDataFile)):
		print("Loading data")
		with open(msDataFile, "rb") as f:
			aTms = pickle.load(f)
			aTbar = pickle.load(f)
	else:
		print("No data file found!")

	#Add noise for figure rounding
	dT = 2.5
	for i in range(2):
		Np = aTms[i].shape[0]
		X = np.random.rand(Np)
		dTms = 2*dT*(X-0.5)
		aTms[i] = aTms[i]+dTms

	pMax = 1.0e-2
	pMin = 5.0e-6
	alph = 0.75

	Nb = 35
	T0 = 0; Tf = 1000.0
	LW = 2
	doNorm = True
	doLog = True

	bins = np.linspace(T0,Tf,Nb)	
	fig = plt.figure(figsize=figSizeHalf)

	lfmv.showDualHist(aTms[0],aTms[1],bins,alph=0.75,Norm=True,Cum=False,LogH=doLog)
	plt.legend(Leg,fontsize=LegFS)
	plt.xlabel("Time in Magnetosheath [s]",fontsize=LabFS)
	plt.ylabel("Density",fontsize=LabFS)
	plt.xlim(T0,Tf)
	plt.ylim(pMin,pMax)

	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

#-------------------------------------------
#Figure 3 (azimuthal transit)
if (doFig3):
	fOut = fOuts[2]
	msDataFile = "msIonDP.pkl"

	spcs = ["H","O"]
	Leg = ["H+","O+"]
	Ns = len(spcs)

	if (os.path.isfile(msDataFile)):
		print("Loading data")
		with open(msDataFile, "rb") as f:
			aDPms = pickle.load(f)
			aP0 = pickle.load(f)
			aPF = pickle.load(f)
	else:
		print("No data file found!")

	#Do Phi_Init vs. DelPhi histogram panel
	doScl = True
	figSizeAT = (12,8)
	cMap = "viridis"
	piB = [-90,120]
	Npi = 150
	Npf = 100
	Np = 200
	
	pfB = [-120,120]
	mTks = [-90,-60,-30,0,30,60,90]
	Ndp = 100
	lLW = 1.5
	PhiI = np.linspace(piB[0],piB[1],Npi)
	PhiF = np.linspace(pfB[0],pfB[1],Npf)
	vNorm = LogNorm(vmin=1.0e-3,vmax=2.5e-1)	

	fig = plt.figure(figsize=figSizeAT)
	gs = gridspec.GridSpec(3,2,height_ratios=[20,1,1],wspace=0.1)#,bottom=0.05,top=0.99,wspace=0.2,hspace=0.05)

	for n in range(2):
		Ax = fig.add_subplot(gs[0,n])
		
		#plt.hist2d(aP0[n],aPF[n],[PhiI,PhiF],normed=True,norm=vNorm,cmap=cMap)
		H,xe,ye = np.histogram2d(aP0[n],aPF[n],[PhiI,PhiF])
		if (doScl):
			for i in range(Npi-1):
				scl = H[i,:].sum()
				if (scl>0):
					H[i,:] = H[i,:]/scl
			
		plt.pcolormesh(PhiI,PhiF,H.T,norm=vNorm,cmap=cMap)
		plt.axis('scaled')
		plt.xlim(piB[0],piB[1])
		plt.ylim(pfB[0],pfB[1])
		
		
		lfmv.ax2mlt(Ax,mTks,doX=True)
		lfmv.ax2mlt(Ax,mTks,doX=False)
	
		#Add several helpful lines
		plt.plot(PhiI,PhiI,'w--'   ,linewidth=lLW)
		plt.plot(PhiI,PhiI+30,'w--',linewidth=lLW)
		plt.plot(PhiI,PhiI+60,'w--',linewidth=lLW)
	
		plt.plot(PhiI,PhiI-30,'w--',linewidth=lLW)
		plt.plot(PhiI,PhiI-60,'w--',linewidth=lLW)
	
	
		plt.hlines(0,piB[0],piB[1],colors='k',linewidth=lLW,linestyles='-')
		plt.vlines(0,pfB[0],pfB[1],colors='k',linewidth=lLW,linestyles='-')
	
		#Add label for drift
		bbox_props = dict(boxstyle="larrow,pad=0.25", fc="white", ec="k", lw=0.5)
		dAr = Ax.text(60,-105,"   Drift   ",ha="center",va="center",size=dLabFS,bbox=bbox_props)
		plt.xlabel("First OCB [MLT]",fontsize=LabFS)
		if (n == 0):
			#plt.ylabel('$\Delta \phi_{ms}$')
			#plt.ylabel('$\phi_{F} [^{\circ}]$')
			plt.ylabel("Last Position [MLT]",fontsize=LabFS)
		else:
			plt.setp(plt.gca().get_yticklabels(),visible=False)
		#plt.tick_params(axis='both', which='major', labelsize="xx-small")	
		plt.title(Leg[n],fontsize=LegFS)
	
	Ax = fig.add_subplot(gs[-1,:])
	cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
	cb.set_label("Density",fontsize=LabFS)	

	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

#-------------------------------------------

#Values for both mpGeoms
Np = 50
Nl = 50

xTk = [-135,-90,-45,0,45,90,135]
spcs = ["H","O","e"]
Leg = ["H+","O+","e-"]
P0 = -150; P1 = 150
L0 = -60; L1 = 60
pBin = np.linspace(P0,P1,Np)
lBin = np.linspace(L0,L1,Nl)
BoxS = ["larrow,pad=0.25","larrow,pad=0.25","rarrow,pad=0.25"]

cMap="inferno"

#Figure 4 mpGeom last
if (doFig4):
	fSizeGeom = (16,5)
	fOut = fOuts[3]
	mpDF = "mpLoss.pkl"
	Ns = 3
	cAx=[1.0e-5,1.0e-3]
	fMax = 0.015
	vNorm = LogNorm(vmin=cAx[0],vmax=cAx[1])

	if (os.path.isfile(mpDF)):
		print("Loading data")
		with open(mpDF, "rb") as f:
			Phis = pickle.load(f)
			Lambdas = pickle.load(f)

	fig = plt.figure(figsize=fSizeGeom,tight_layout=True)
	#wRat = np.ones(Ns+1)
	#wRat[-1] = 0.1

	gs = gridspec.GridSpec(3,Ns,height_ratios=[7.5,20,1])#hspace=0.05,wspace=0.05)

	for i in range(Ns):
		
		Phi = Phis[i]
		Lambda = Lambdas[i]
		
		#1D histogram
		Ax1D = fig.add_subplot(gs[0,i])
		Ax1D.hist(Phi,pBin,color='blue',normed=True)
		
	
		#2D histogram
		Ax2D = fig.add_subplot(gs[1,i])
		Ax2D.hist2d(Phi,Lambda,[pBin,lBin],cmap=cMap,normed=True,norm=vNorm )
	
		#Axes
		#plt.axis('scaled')
		Ax2D.set_aspect('equal')
		Ax1D.set_xlim(P0,P1)
		Ax1D.set_ylim(0,fMax)
		Ax1D.set_xticks(xTk)
		plt.setp(Ax1D.get_xticklabels(),visible=False)
		Ax1D.set_yticks(np.arange(0.003,fMax+1.0e-8,0.003))
		
			
		Ax2D.set_xlim(P0,P1)
		Ax2D.set_ylim(L0,L1)
		Ax2D.set_yticks(np.arange(-40,41,20))
	
		lfmv.ax2mlt(Ax2D,xTk)
		Ax2D.set_xlabel("Magnetic Local Time",fontsize=LabFS)
		Ax2D.text(-120,40,Leg[i],fontsize=TitFS)
		if (i==0):
			plt.setp(Ax1D.get_yticklabels(),visible=False)	
			Ax2D.set_ylabel("Magnetic Latitude [$^{\circ}$]",fontsize=LabFS)
		elif (i==Ns-1):
			Ax1D.set_ylabel("Density",fontsize=LabFS)
			Ax1D.yaxis.tick_right()
			Ax1D.yaxis.set_label_position("right")
			plt.setp(Ax2D.get_yticklabels(),visible=False)
		else:
			plt.setp(Ax2D.get_yticklabels(),visible=False)
			plt.setp(Ax1D.get_yticklabels(),visible=False)
		
		#Add label for drift		
		bbox_props = dict(boxstyle=BoxS[i], fc="white", ec="k", lw=0.5)
		dAr = Ax2D.text(120,-45,"   Drift   ",ha="center",va="center",size=dLabFS,bbox=bbox_props)
	
	Ax = fig.add_subplot(gs[-1,:])
	cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
	cb.set_label("Density",fontsize=cbFS)

	gs.tight_layout(fig)
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

#Figure 5 mpGeom first
if (doFig5):
	fSizeGeom = (10,4.5)
	fOut = fOuts[4]
	mpDF = "mpLoss.1st.pkl"
	Ns = 2
	cAx=[1.0e-5,1.0e-3]
	fMax = 0.015
	vNorm = LogNorm(vmin=cAx[0],vmax=cAx[1])

	if (os.path.isfile(mpDF)):
		print("Loading data")
		with open(mpDF, "rb") as f:
			Phis = pickle.load(f)
			Lambdas = pickle.load(f)

	fig = plt.figure(figsize=fSizeGeom,tight_layout=True)
	#wRat = np.ones(Ns+1)
	#wRat[-1] = 0.1

	gs = gridspec.GridSpec(4,Ns,height_ratios=[7.5,20,1,1],hspace=0.05,wspace=0.05)

	for i in range(Ns):
		
		Phi = Phis[i]
		Lambda = Lambdas[i]
		
		#1D histogram
		Ax1D = fig.add_subplot(gs[0,i])
		Ax1D.hist(Phi,pBin,color='blue',normed=True)
		
	
		#2D histogram
		Ax2D = fig.add_subplot(gs[1,i])
		Ax2D.hist2d(Phi,Lambda,[pBin,lBin],cmap=cMap,normed=True,norm=vNorm )
	
		#Axes
		#plt.axis('scaled')
		Ax2D.set_aspect('equal')
		Ax1D.set_xlim(P0,P1)
		Ax1D.set_ylim(0,fMax)
		Ax1D.set_xticks(xTk)
		plt.setp(Ax1D.get_xticklabels(),visible=False)
		Ax1D.set_yticks(np.arange(0.003,fMax+1.0e-8,0.003))
		
			
		Ax2D.set_xlim(P0,P1)
		Ax2D.set_ylim(L0,L1)
		Ax2D.set_yticks(np.arange(-40,41,20))
	
		lfmv.ax2mlt(Ax2D,xTk)
		Ax2D.set_xlabel("Magnetic Local Time",fontsize=LabFS)
		Ax2D.text(-120,40,Leg[i],fontsize=TitFS)
		if (i==0):
			plt.setp(Ax1D.get_yticklabels(),visible=False)	
			Ax2D.set_ylabel("Magnetic Latitude [$^{\circ}$]",fontsize=LabFS)
		elif (i==Ns-1):
			Ax1D.set_ylabel("Density",fontsize=LabFS)
			Ax1D.yaxis.tick_right()
			Ax1D.yaxis.set_label_position("right")
			plt.setp(Ax2D.get_yticklabels(),visible=False)
		else:
			plt.setp(Ax2D.get_yticklabels(),visible=False)
			plt.setp(Ax1D.get_yticklabels(),visible=False)
		
		#Add label for drift		
		bbox_props = dict(boxstyle=BoxS[i], fc="white", ec="k", lw=0.5)
		dAr = Ax2D.text(120,-45,"   Drift   ",ha="center",va="center",size=dLabFS,bbox=bbox_props)
	
	Ax = fig.add_subplot(gs[-1,:])
	cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
	cb.set_label("Density",fontsize=cbFS)

	gs.tight_layout(fig)
	plt.savefig(fOut,dpi=figQ)
	plt.close('all')
	lfmv.trimFig(fOut)

