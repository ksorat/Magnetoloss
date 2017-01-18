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
from matplotlib.colors import LogNorm
from matplotlib.colors import Normalize

Root = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"

PhiC = 30
dAlph = 10
doMask = False


doOxy = True
if (doOxy):
	fIn = Root + "O.100keV.h5part"
	spcLab = "O"
else:
	fIn = Root + "H.100keV.h5part"
	vbDataFile = "vbH.pkl"
	spcLab = "H"
	figName = "vB_H.png"

vbDataFile = "vb"+spcLab+str(PhiC)+".pkl"
figName = "vb"+spcLab+str(PhiC)+".png"


if (os.path.isfile(vbDataFile)):
        print("Loading data")
        with open(vbDataFile, "rb") as f:
        	s = pickle.load(f)
        	z = pickle.load(f)
        	Vx = pickle.load(f)
        	Vy = pickle.load(f)
        	Vz = pickle.load(f)
else:
	print("Calculating data for %s"%(spcLab))
	s,z,Vx,Vy,Vz = px.findCrossings(fIn,PhiC=PhiC)
	print("Writing pickle")
	with open(vbDataFile, "wb") as f:
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

lfmv.ppInit()
plt.close(1)
fig = plt.figure(figsize=(18,4))
figQ = 300
gs = gridspec.GridSpec(1,3,width_ratios=[10,10,0.25])

#cMap="viridis"
cMap="YlGnBu"

#cNorm = LogNorm(vmin=1.0e-2,vmax=1)

zb = np.linspace(-8,8,25)
Vpb = np.linspace(-0.2,0.2,30)
Vzb = np.linspace(-0.2,0.2,30)

vMin = 0; vMax = 0.75
vNorm = mpl.colors.Normalize(vmin=vMin,vmax=vMax)

Axp = fig.add_subplot(gs[0,0])
Axp.hist2d(Vphi,z,[Vpb,zb],normed=True,vmin=vMin,vmax=vMax,cmap=cMap)
plt.ylabel("Height [Re]")
plt.xlabel('$V_{\phi}$ [Re/s]')
#plt.colorbar(Axp)

Axz = fig.add_subplot(gs[0,1])
Axz.hist2d(Vz,z,[Vzb,zb],normed=True,vmin=vMin,vmax=vMax,cmap=cMap)
plt.setp(Axz.get_yticklabels(),visible=False)
plt.xlabel('Vz [Re/s]')
#Axz.colorbar()

Axcb = fig.add_subplot(gs[0,2])
cb = mpl.colorbar.ColorbarBase(Axcb,cmap=cMap,norm=vNorm,orientation='vertical')
cb.set_label("Density",fontsize="xx-small")

plt.tight_layout()

plt.show()
#plt.savefig(figName,dpi=figQ)