import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm

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
	Np = xeq.shape[0]
	print("Working with %d particles"%(Np))
	for n in range(Np):
		#Accumulate EQXs for time after first crossing
		tCrn = tCr[:,n]
		tSlc1 = tCrn.argmax()
		teqn = tEq[tSlc1:,n]
		ts,Ind = np.unique(teqn,return_index=True)
		#Have unique EQXs
		Neq = Ind.sum()
		if (Neq>0):
			x = xeq[tSlc:,n]
			y = yeq[tSlc:,n]
			x = x[Ind]
			y = y[Ind]
	
			r = np.sqrt(x**2.0 + y**2.0)
			phi = np.arctan2(y,x)
			for i in range(Neq):
				R.append(r[i])
				P.append(phi[i])
	return np.array(R),np.array(P)

figSize = (8,8)
figQ = 300 #DPI

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

Np = 105
Nr = 100
cMap = "viridis"
phiB = d2rad*np.linspace(-120,120,Np+1)
rB = np.linspace(7.5,20,Nr+1)

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

gs = gridspec.GridSpec(2,Ns,height_ratios=[10,1],wspace=0.05)#,bottom=0.05,top=0.99,wspace=0.2,hspace=0.05)

for n in range(Ns):
	Ax = fig.add_subplot(gs[0,n],projection='polar')
	N,a,b = np.histogram2d(Rs[n],Phis[n],[rB,phiB])
	f = N/dV
	print(f.shape)
	Ax.pcolormesh(PP,RR,f,cmap=cMap,shading='flat')

plt.savefig("msRad.png",dpi=figQ)
plt.close('all')

# oR = np.zeros(Np)
# hR = np.zeros(Np)

# phibins = np.linspace(-120,120,Np)
# for i in range(Np-1):
# 	p0 = phibins[i]
# 	p1 = phibins[i+1]
# 	Ind = (Phis[0] >= p0) & (Phis[0]<p1)
# 	hR[i] = Rs[0][Ind].mean()
# 	Ind = (Phis[1] >= p0) & (Phis[1]<p1)
# 	oR[i] = Rs[1][Ind].mean()
# oR[Np-1] = oR[Np-2]
# hR[Np-1] = hR[Np-2]

# oX = oR*np.cos(phibins*np.pi/180)
# oY = oR*np.sin(phibins*np.pi/180)

# hX = hR*np.cos(phibins*np.pi/180)
# hY = hR*np.sin(phibins*np.pi/180)

# plt.plot(oX,oY,'g',hX,hY,'b')
# plt.axis('equal')
# plt.show()

