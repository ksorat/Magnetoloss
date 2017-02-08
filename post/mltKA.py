#Generate figures of mlt of last OCB versus K/alpha for ions

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle

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

figSize = (8,8)
figQ = 300 #DPI

lfmv.initLatex()
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

