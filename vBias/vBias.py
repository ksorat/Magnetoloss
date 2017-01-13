#Look for velocity statistics at a given phi in magnetosheath
import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cPickle as pickle
import os
import phiX as px

Root = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"

fIn = Root + "O.100keV.h5part"
vbDataFile = "vbO.pkl"

PhiC = 60
dAlph = 10
doMask = False

if (os.path.isfile(vbDataFile)):
        print("Loading data")
        with open(vbDataFile, "rb") as f:
        	s = pickle.load(f)
        	z = pickle.load(f)
        	Vx = pickle.load(f)
        	Vy = pickle.load(f)
        	Vz = pickle.load(f)
else:
	s,z,Vx,Vy,Vz = px.findCrossings(fIn,PhiC=PhiC)
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(s,f)
		pickle.dump(z,f)
		pickle.dump(Vx,f)
		pickle.dump(Vy,f)
		pickle.dump(Vz,f)


#Convert Cartesian velocities
MagV = np.sqrt(Vx**2.0 + Vy**2.0 + Vz**2.0)
MagVxy = np.sqrt(Vx**2.0 + Vy**2.0)

ph = PhiC*np.pi/180

CAlp = (-Vx*np.sin(ph) + Vy*np.cos(ph))/MagVxy
CAlph = Vz/MagV

alph = np.arccos(CAlph)*180/np.pi
vp = np.arctan2(Vy,Vx)*180/np.pi  + 90
alphP = np.arccos(CAlp)*180/np.pi
Vphi = -np.sin(ph)*Vx + np.cos(ph)*Vy

if (doMask):
	printf("Masking pitch angles, +/- %f"%(dAlph))
	Mask = (alph>=90-dAlph) & (alph<=90+dAlph)
	s = s[Mask]
	z = z[Mask]
	Vz = Vz[Mask]
	Vphi = Vphi[Mask]


