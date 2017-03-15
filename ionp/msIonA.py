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

#Return list of EQXs for particles in sheath
def getEQXs(fIn):
	isOut = lfmpp.getOut(fIn)
	t,xeq = lfmpp.getH5p(fIn,"xeq",Mask=isOut)
	t,yeq = lfmpp.getH5p(fIn,"yeq",Mask=isOut)
	t,tCr = lfmpp.getH5p(fIn,"tCr",Mask=isOut)
	t,tEq = lfmpp.getH5p(fIn,"Teq",Mask=isOut)
	t,Vx  = lfmpp.getH5p(fIn,"vx",Mask=isOut)
	t,Vy  = lfmpp.getH5p(fIn,"vy",Mask=isOut)
	t,Vz  = lfmpp.getH5p(fIn,"vz",Mask=isOut)

	Vmag = np.sqrt(Vx**2.0+Vy**2.0+Vz**2.0)

	A = []
	P = []
	Np = xeq.shape[1]
	print("Working with %d particles"%(Np))
	for n in range(Np):
		#Accumulate EQXs for time after first crossing
		tCrn = tCr[:,n]
		tSlc1 = tCrn.argmax()
		teqn = tEq[tSlc1:,n]
		ts,Ind = np.unique(teqn,return_index=True)
		#Have unique EQXs
		Neq = len(Ind)
		if (Neq>0):
			x = xeq[tSlc1:,n]
			y = yeq[tSlc1:,n]
			x = x[Ind]
			y = y[Ind]
			vm = Vmag[tSlc:,n]
			vm = vm[Ind]
			vzn = Vz[tSlc:,n]
			vzn = vzn[Ind]


			als = np.arccos(vzn/vm)*180.0/np.pi
			r = np.sqrt(x**2.0 + y**2.0)
			phi = np.arctan2(y,x)
			for i in range(Neq):
				A.append(als[i])
				P.append(phi[i])
	return np.array(A),np.array(P)

lfmv.ppInit()
msDataFile = "msIonA.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]

Ns = len(spcs)
Phis = []
As = []

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		Phis = pickle.load(f)
		As = pickle.load(f)
else:
	print("No data file found, calculating")

	for i in range(Ns):
		fIn = RootDir + spcs[i] + "." + fileStub
		print("Reading %s"%(fIn))
		print("Species %s"%(Leg[i]))
		Al,p = getEQXs(fIn)
		print(A.shape)

		Phis.append(p)
		As.append(Al)