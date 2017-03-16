#Make various pickles for Slava

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
from pyhdf.SD import SD, SDC
import lfmInterp as lfm

#Grab line of constant j, average k=0/k=-1
#Assuming k,j,i ordering
def getLineAvg(X3,jS,xScl=1.0):
	k0 = 0
	k1 = -1
	
	xR = 0.5*xScl*(X3[k0,jS,:] + X3[k1,jS,:])
	return xR
def getLine0(X3,jS,xScl=1.0):
	k0 = 0
	xR = xScl*(X3[k0,jS,:])

#Start ID
id0 = 1070000
dI = 1000 #Jumps in file

NumI = 30 #Use 30 files, 20s * 30 = 10min

Stub = "/glade/p/hao/wiltbemj/SNS/ION/SNS-Bz-5-Vx400-N5-F200/SNS-Bz-5-Vx400-N5-F200_mhd_"

#Constants
Re = 6.38e+8 #Earth radius [cm]
iRe = 1/Re
bScl = 1.0e+5 #Gauss->nT
gamma = 5.0/3.0
Mp = 1.6726219e-27 #kg

BxA = []
ByA = []
BzA = []
Bx0 = []
By0 = []
Bz0 = []
fIns = []

for n in range(NumI):
	fIn = Stub + str(id0+n*dI) + ".hdf"
	fIns.append(fIn)
	#Get data from file

	#Do special things for first
	if (n == 0):
		x3 = iRe*np.double(hdffile.select('X_grid').get())
		y3 = iRe*np.double(hdffile.select('Y_grid').get())
		z3 = iRe*np.double(hdffile.select('Z_grid').get())
		#Coordinates of 2D plane
		ks = 0 #Upper half x-y plane
		xxi = x3[ks,:,:].squeeze()
		yyi = y3[ks,:,:].squeeze()
		rri = np.sqrt(xxi**2.0 + yyi**2.0)
		ppi = np.arctan2(yyi,xxi)
		
		#Find MLT slice 15:00
		pMLT = 45.0
		pi0 = (180/np.pi)*ppi[:,0]
		pc0 = 0.5*(pi0[0:-1] + pi0[1:])
		mltJ = np.abs(pc0-pMLT).argmin()

		#Find radial cell centers at this slice
		Rci = rri[mltJ,:]
		Rc = 0.5*(Rci[0:-1] + Rci[1:])		
	
	#Do things for every slice, get fields	
	BxCC,ByCC,BzCC = lfm.getHDFVec(hdffile,'b')

	#Field lines/scaling
	#0/1 average
	Bx = getLineAvg(BxCC,mltJ,bScl)
	By = getLineAvg(ByCC,mltJ,bScl)
	Bz = getLineAvg(BzCC,mltJ,bScl)

	BxA.append(Bx)
	ByA.append(By)
	BzA.append(Bz)
	#0
	Bx = getLine0(BxCC,mltJ,bScl)
	By = getLine0(ByCC,mltJ,bScl)
	Bz = getLine0(BzCC,mltJ,bScl)
	Bx0.append(Bx)
	By0.append(By)
	Bz0.append(Bz)


#Now done, save to pickle
pklFile = "pkl4Slava.pkl"
with open(pklFile, "wb") as f:
	pickle.dump(fIns,f)
	pickle.dump(Rc  ,f)
	pickle.dump(BxA ,f)
	pickle.dump(ByA ,f)
	pickle.dump(BzA ,f)
	pickle.dump(Bx0 ,f)
	pickle.dump(By0 ,f)
	pickle.dump(Bz0 ,f)

