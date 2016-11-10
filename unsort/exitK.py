#Calculate histograms of Delta-Phi
#Only bother with ions

import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm

def lastK(fIn):
	isOut = lfmpp.getOut(fIn)
	ids,kev = lfmpp.getH5pFin(fIn,"kev",Mask=isOut)
	return ids,kev
def mpxK(fIn):
	#Get energies at last/first MPX
	isOut = lfmpp.getOut(fIn,mp=True)
	t, kevPT  = lfmpp.getH5p(fIn,"kev")
	#Last MP crossings
	pid,Tmpx = lfmpp.getH5pFin(fIn,"tCr",Mask=isOut) 
	#First MP crossings
	R, Phi, Lambda, Tmpx0 = lfmpp.getSphLoss1st(fIn)
	Np = isOut.sum() #Number of out particles
	mpK	= np.zeros(Np)
	mpK0= np.zeros(Np)
	
	for n in range(Np):
		idn = np.int(pid[n]-1)
		#Time slices of first/last MPX
		ts0 = np.argmin(Tmpx0[n]>=t)
		tsF = np.argmin(Tmpx[n]>=t)
		#print(n,idn,ts0,tsF)
		mpK[n] = kevPT[tsF,idn]
		mpK0[n] = kevPT[ts0,idn]
	return mpK0,mpK
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["Hydrogen","Oxygen"]

Ns = len(spcs)

Kevs = []
KevMP = []
KevMP0 = []
for i in range(Ns):

	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	print("Reading %s"%(fIn))
	print("Species %s"%(Leg[i]))
	ids,ks = lastK(fIn)
	mpk,mpk0 = mpxK(fIn)
	Kevs.append(ks)
	KevMP.append(mpk)
	KevMP0.append(mpk0)

Nb = 20
N0 = 0; N1 = 225
bins = np.linspace(N0,N1,Nb)
doNorm = True
doLog = False

nxFig = plt.hist(Kevs,bins,normed=doNorm,log=doLog)
plt.legend(Leg)
plt.xlim((N0,N1))
plt.xlabel('Energy [keV] @ Escape')
plt.ylabel('Fraction')
#plt.savefig('ExitK.png')

#plt.ylim((0,pMax))
