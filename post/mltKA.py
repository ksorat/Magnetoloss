#Generate figures of mlt of last OCB versus K/alpha for ions

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm

def getXKA(fIn):
	isOut = lfmpp.getOut(fIn,mp=True)

	#Get spherical coordinates of last MP Xing
	R,Phi,Lambda = lfmpp.getSphLoss(fIn)

	#Get time index of last MP crossing
	t,tMP = lfmpp.getH5p(fIn,"tCr",Mask=isOut)

	tsMP = np.argmax(tMP,axis=0)
	#Use these slices to find values at last X'ing
	t,Kt  = lfmpp.getH5p(fIn,"kev",Mask=isOut)
	t,Vxt = lfmpp.getH5p(fIn,"vx",Mask=isOut)
	t,Vyt = lfmpp.getH5p(fIn,"vy",Mask=isOut)
	t,Vzt = lfmpp.getH5p(fIn,"vz",Mask=isOut)


	Np = Kt.shape[1]
	K = np.zeros(Np)
	A = np.zeros(Np)

	for i in range(Np):
		tsi = tsMP[i]
		vxi = Vxt[tsi,i]
		vyi = Vyt[tsi,i]
		vzi = Vzt[tsi,i]
		vmag = np.sqrt(vxi**2.0+vyi**2.0+vzi**2.0)

		K[i] = Kt[tsi,i]
		A[i] = np.arccos(vzi/vmag)*180/np.pi

	mlt = Phi
	return mlt,K,A


lfmv.ppInit()
msDataFile = "mpKA.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]
Ns = len(spcs)

mpMLT = []
mpK   = []
mpA   = []

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		mpMLT = pickle.load(f)
		mpK   = pickle.load(f)
		mpA   = pickle.load(f)
else:
	print("No data file found, calculating")

	for i in range(Ns):
		fIn = RootDir + spcs[i] + "." + fileStub
		print("Reading %s"%(fIn))

		mlt,K,A = getXKA(fIn)

		mpMLT.append(mlt)
		mpK.append(K)
		mpA.append(A)

	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(mpMLT,f)
		pickle.dump(mpK,f)
		pickle.dump(mpA,f)


Nplt = 2
fSz = 14
figSize = (10,10)
figQ = 300 #DPI

Nxb = 100
mTks = [-120,-90,-60,-30,0,30,60,90,120]

Xb = np.linspace(-135,135,Nxb)
Xlab = "Last OCB MLT"
cMap = "viridis"
doNorm = False

for i in range(Nplt):
	fig = plt.figure(1,figsize=figSize)
	if (i==0):
		#Do K plot
		Nk = 40
		Ylab = "Energy [keV]"
		titS = "Energy at Last OCB"
		fOut = "mltK.png"
		Yb = np.linspace(1,200,Nk)
		mpY = mpK
		vNorm = LogNorm(1.0,5.0e+2)
	if (i==1):
		#Do alpha plot
		Na = 40
		Ylab = "Pitch Angle"
		titS = "Pitch Angle at Last OCB"
		fOut = "mltA.png"
		Yb = np.linspace(0,180,Na)
		mpY = mpA
		vNorm = LogNorm(1.0,1.0e+2)
	gs = gridspec.GridSpec(3, 1,height_ratios=[15,15,1])
	for s in range(Ns):
		Ax = fig.add_subplot(gs[s,0])
		plt.hist2d(mpMLT[s],mpY[s],[Xb,Yb],norm=vNorm,cmap=cMap)
		lfmv.ax2mlt(Ax,mTks,doX=True)

		plt.ylabel(Ylab)
		Ax.text(-120,150,Leg[s],fontsize=fSz)
	Ax = fig.add_subplot(gs[-1,0])
	cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
	cb.set_label("Counts",fontsize="small")
	plt.suptitle(titS)
	plt.savefig(fOut)
	plt.close('all')
