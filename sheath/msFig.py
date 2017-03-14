#Make figure of magnetosheath fields

import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
from pyhdf.SD import SD, SDC
import lfmInterp as lfm

fIn = "/glade/p/hao/wiltbemj/SNS/ION/SNS-Bz-5-Vx400-N5-F200/SNS-Bz-5-Vx400-N5-F200_mhd_2000000.hdf"
Re = 6.38e+8 #Earth radius [cm]
iRe = 1/Re
bScl = 1.0e+5 #Gauss->nT

hdffile = SD(fIn)
#Grab x/y/z arrays from HDF file.  Scale by Re
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
pc0 = 0.5*(pi0[0:-2] + pi0[1:-1])


mltJ = np.abs(pc0-pMLT).argmin()
Rci = rri[mltJ,:]
Rc = 0.5*(Rci[0:-2] + Rci[1:-1])
BxCC,ByCC,BzCC = lfm.getHDFVec(hdffile,'b')

Bx0 = bScl*BxCC[ks,mltJ,:]
By0 = bScl*BxCC[ks,mltJ,:]
Bz0 = bScl*BxCC[ks,mltJ,:]
B0 = np.sqrt(Bx0**2.0 + By0**2.0 + Bz0**2.0)

print("Field maxes = ", np.abs(Bx0).max(),np.abs(By0).max(),np.abs(Bz0).max())

#Do pic
figSize = (8,8)
figQ = 300 #DPI

lfmv.initLatex()

Leg = ['|B|','Bx','By','Bz']
plt.plot(Rc,B0,'ko-',Rc,Bx0,'bo-',Rc,By0,'go-',Bz0,'ro-')
plt.legend(Leg)
plt.xlabel('Distance [Re]')
plt.ylabel('Field Strength [nT]')

