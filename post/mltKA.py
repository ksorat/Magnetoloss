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

	#Get time index of last MP crossing
	t,tMP = lfmpp.getH5p(fIn,"tCr")
	tMP = tMP[:,isOut]

	tsMP = np.argmax(tMP,axis=0)
	#Use these slices to find values at last X'ing
	t,Kt = lfmpp.getH5p(fIn,"kev")
	Kt = Kt[:,isOut]

	mlt = tsMP
	K = 0
	A = 0
	return mlt,Kt,A
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

	#for i in range(Ns):
	for i in [1]:	
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

