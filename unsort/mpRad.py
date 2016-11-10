import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm

def getLastEQX(fIn):
	isOut = lfmpp.getOut(fIn)
	ids,xeq = lfmpp.getH5pFin(fIn,"xeq",Mask=isOut)
	ids,yeq = lfmpp.getH5pFin(fIn,"yeq",Mask=isOut)
	return xeq,yeq

mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'

dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O"]
Leg = ["Hydrogen","Oxygen"]

Ns = len(spcs)
iXeq = []
iYeq = []
Phis = []
Rs = []

for i in range(Ns):
	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	print("Reading %s"%(fIn))
	print("Species %s"%(Leg[i]))
	xeq,yeq = getLastEQX(fIn)
	iXeq.append(xeq)
	iYeq.append(yeq)
	p = np.arctan2(yeq,xeq)*180/np.pi
	R = np.sqrt(xeq**2.0 + yeq**2.0)
	Phis.append(p)
	Rs.append(R)

Np = 50
oR = np.zeros(Np)
hR = np.zeros(Np)

phibins = np.linspace(-120,120,Np)
for i in range(Np-1):
	p0 = phibins[i]
	p1 = phibins[i+1]
	Ind = (Phis[0] >= p0) & (Phis[0]<p1)
	hR[i] = Rs[0][Ind].mean()
	Ind = (Phis[1] >= p0) & (Phis[1]<p1)
	oR[i] = Rs[1][Ind].mean()
oR[Np-1] = oR[Np-2]
hR[Np-1] = hR[Np-2]

oX = oR*np.cos(phibins*np.pi/180)
oY = oR*np.sin(phibins*np.pi/180)

hX = hR*np.cos(phibins*np.pi/180)
hY = hR*np.sin(phibins*np.pi/180)

plt.plot(oX,oY,'g',hX,hY,'b')
plt.axis('equal')
plt.show()

