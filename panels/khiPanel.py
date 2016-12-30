#Generates panel figure from eq-VTIs and H5p file
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Wedge
import matplotlib.lines as lines
 from matplotlib.lines import Line2D
 

def getFld(vtiDir,t,dt=10.0,eqStub="eqSlc"):
	tSlc = np.int(t/dt)
	vtiFile = vtiDir + "/" + eqStub + ".%04d.vti"%(tSlc)

	dBz = lfmv.getVTI_SlcSclr(vtiFile).T
	ori,dx,ex = lfmv.getVTI_Eq(vtiFile)
	xi = ori[0] + np.arange(ex[0],ex[1]+1)*dx[0]
	yi = ori[1] + np.arange(ex[2],ex[3]+1)*dx[1]

	return xi,yi,dBz

def getPs(h5pDir,h5pStub,t,dt=10.0):
	tSlc = np.int(t/dt)
	h5pFile = h5pDir + "/" + h5pStub
	t,xeq = lfmpp.getH5pT(h5pFile,"xeq",tSlc)
	t,yeq = lfmpp.getH5pT(h5pFile,"yeq",tSlc)
	t,kev = lfmpp.getH5pT(h5pFile,"kev",tSlc)

	t,mp = lfmpp.getH5pT(h5pFile,"mp",tSlc)
	t,tl = lfmpp.getH5pT(h5pFile,"tl",tSlc)
	t,atm = lfmpp.getH5pT(h5pFile,"atm",tSlc)

	In = (atm+tl+mp) < 0.5
	xeq = xeq[In]
	yeq = yeq[In]
	kev = kev[In]
	
	return xeq,yeq,kev

Spcs = ["H+","e-"]
h5ps = ["H.100keV.h5part","e.100keV.h5part"]
Mrk = [-60,60]
RMax = 20
RMin = 2.0

Ts = 3100

figSize = (10,10)
figQ = 300 #DPI
figName = "khiPanel.png"

#Plot bounds fields/particles (nT/keV), plot details
fldBds = [-35,35]
fldCMap = "RdGy_r"
fldOpac = 0.5
fldDomX = [-5,10]


pBds = [50,150]
pCMap = "cool"
pSize = 2; pMark = 'o'; pLW = 0.2

#Locations
RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data"
vtiDir = RootDir + "/" + "eqSlc"
h5pDir = RootDir + "/" "H5p"

#Do figures
lfmv.initLatex()
fig = plt.figure(figsize=figSize)
#fig = plt.figure()

Ns = len(Spcs)
#Get field data
#xi,yi,dBz = getFld(vtiDir,Ts)
radScl = np.pi/180.0

for s in range(Ns):
	if (Ns==0):
		fldDomY = [-20,0]
	else:
		fldDomY = [0,20]
	fig = plt.figure()
	Ax = plt.gca()
	figName = "khiPanel_%d.png"%(s)
	#Fields
	#fldPlt = Ax.pcolormesh(xi,yi,dBz,vmin=fldBds[0],vmax=fldBds[1],cmap=fldCMap,shading='gouraud',alpha=fldOpac)
	lfmv.addEarth2D()
	#Now do particles
	#xs,ys,zs = getPs(h5pDir,h5ps[s],Ts)
	#pPlt = Ax.scatter(xs,ys,s=pSize,marker=pMark,c=zs,vmin=pBds[0],vmax=pBds[1],cmap=pCMap,linewidth=pLW)
	#Now do KHI marker
	Phi = radScl*Mrk[s]
	p0 = (RMin*np.cos(Phi),RMin*np.sin(Phi))
	p1 = (RMax*np.cos(Phi),RMax*np.sin(Phi))
	khiLine = [p0,p1]
	(ln_xs, ln_ys) = zip(*khiLine)

	Ax.add_line(Line2D(ln_xs,ln_ys,linewidth=2,color='blue'))

	#Pretty-ify
	plt.axis('scaled')
	plt.xlim(fldDomX); plt.ylim(fldDomY)
	plt.xlabel('GSM-X [Re]')
	plt.ylabel('GSM-Y [Re]')

	plt.savefig(figName,dpi=figQ)
