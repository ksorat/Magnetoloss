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


def getLastEQX(fIn):
	isOut = lfmpp.getOut(fIn)
	ids,xeq = lfmpp.getH5pFin(fIn,"xeq",Mask=isOut)
	ids,yeq = lfmpp.getH5pFin(fIn,"yeq",Mask=isOut)
	return xeq,yeq

#Return list of EQXs for particles in sheath
def getEQXs(fIn):
	isOut = lfmpp.getOut(fIn)
	t,xeq = lfmpp.getH5p(fIn,"xeq",Mask=isOut)
	t,yeq = lfmpp.getH5p(fIn,"yeq",Mask=isOut)
	t,tCr = lfmpp.getH5p(fIn,"tCr",Mask=isOut)
	t,tEq = lfmpp.getH5p(fIn,"Teq",Mask=isOut)

	R = []
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
	
			r = np.sqrt(x**2.0 + y**2.0)
			phi = np.arctan2(y,x)
			for i in range(Neq):
				R.append(r[i])
				P.append(phi[i])
	return np.array(R),np.array(P)

lfmv.ppInit()
msDataFile = "msIonR.pkl"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["H+","O+"]

Ns = len(spcs)
iXeq = []
iYeq = []
Phis = []
Rs = []

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		Phis = pickle.load(f)
		Rs = pickle.load(f)
else:
	print("No data file found, calculating")

	for i in range(Ns):
		fIn = RootDir + spcs[i] + "." + fileStub
		print("Reading %s"%(fIn))
		print("Species %s"%(Leg[i]))
		R,p = getEQXs(fIn)
		print(R.shape)
		# xeq,yeq = getLastEQX(fIn)
		# iXeq.append(xeq)
		# iYeq.append(yeq)
		# p = np.arctan2(yeq,xeq)*180/np.pi
		# R = np.sqrt(xeq**2.0 + yeq**2.0)
		Phis.append(p)
		Rs.append(R)

	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(Phis,f)
		pickle.dump(Rs,f)

d2rad = np.pi/180.0

#Make polar histograms
figSize = (8,5)
figQ = 300 #DPI

Np = 200
Nr = 200
vNorm = LogNorm(vmin=1.0e-2,vmax=5e-0)
cMap = "viridis"
phiB = d2rad*np.linspace(-160,160,Np+1)
rB = np.linspace(5,22.5,Nr+1)
mTks = np.arange(-135,180,45)
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

gs = gridspec.GridSpec(2,Ns,height_ratios=[25,1])#,bottom=0.05,top=0.99,wspace=0.2,hspace=0.05)

for n in range(Ns):
	Ax = fig.add_subplot(gs[0,n],projection='polar')
	N,a,b = np.histogram2d(Rs[n],Phis[n],[rB,phiB],normed=True)
	f = N/dV
	
	Ax.pcolormesh(PP,RR,f,cmap=cMap,shading='flat',norm=vNorm)
	E = plt.Circle((0, 0), 1.0, transform=Ax.transData._b, color="blue", alpha=0.85)
	Ax.add_artist(E)

	Ax.set_rlabel_position(210)
	Ax.grid(True)
	lfmv.ax2mlt(Ax,mTks,doX=True,Polar=True)
	#print(Ax.get_xticks())
	#print(Ax.get_xticklabels())
	plt.xlabel(Leg[n])
	plt.tick_params(axis='both', which='major', labelsize="x-small")	
#Do colorbar
Ax = fig.add_subplot(gs[1,:])
cb = mpl.colorbar.ColorbarBase(Ax,cmap=cMap,norm=vNorm,orientation='horizontal')
cb.set_label("Density",fontsize="small")

plt.savefig("msRad.png",dpi=figQ)
plt.close('all')


