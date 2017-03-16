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

#Grab line of constant j, average k=0/k=-1
#Assuming k,j,i ordering
def getLine(X3,jS,xScl=1.0):
	k0 = 0
	k1 = -1
	k0 = -1
	xR = 0.5*xScl*(X3[k0,jS,:] + X3[k1,jS,:])
	return xR

#fIn = "/glade/p/hao/wiltbemj/SNS/ION/SNS-Bz-5-Vx400-N5-F200/SNS-Bz-5-Vx400-N5-F200_mhd_1070000.hdf"
fIn = "/glade/p/hao/wiltbemj/SNS/ION/SNS-Bz-5-Vx400-N5-F200/SNS-Bz-5-Vx400-N5-F200_mhd_1500000.hdf"
msDataFile = "mSheath.pkl"
Re = 6.38e+8 #Earth radius [cm]
iRe = 1/Re
bScl = 1.0e+5 #Gauss->nT
gamma = 5.0/3.0
Mp = 1.6726219e-27 #kg

if (os.path.isfile(msDataFile)):
	print("Loading data")
	with open(msDataFile, "rb") as f:
		B0  = pickle.load(f)
		Bx0 = pickle.load(f)
		By0 = pickle.load(f)
		Bz0 = pickle.load(f)		
		d0  = pickle.load(f)
		Cs0 = pickle.load(f)
		kT0 = pickle.load(f)
		Vx0 = pickle.load(f)
		Vy0 = pickle.load(f)
		Vz0 = pickle.load(f)		
		Rc  = pickle.load(f)

else:
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
	pc0 = 0.5*(pi0[0:-1] + pi0[1:])
	mltJ = np.abs(pc0-pMLT).argmin()

	#Find radial cell centers at this slice
	Rci = rri[mltJ,:]
	Rc = 0.5*(Rci[0:-1] + Rci[1:])

	BxCC,ByCC,BzCC = lfm.getHDFVec(hdffile,'b')
	#Get soundspeed [km/s]
	C3 = lfm.getHDFScl(hdffile,"c",Scl=1.0e-5)
	#Get rho [kg/m3]
	D3 = lfm.getHDFScl(hdffile,"rho",Scl=1.0e+3)
	
	#Get velocities [m/s]
	Vx3,Vy3,Vz3 = lfm.getHDFVec(hdffile,"v",Scl=1.0e-3)

	#Field lines/scaling
	Bx0 = getLine(BxCC,mltJ,bScl)
	By0 = getLine(ByCC,mltJ,bScl)
	Bz0 = getLine(BzCC,mltJ,bScl)

	B0 = np.sqrt(Bx0**2.0 + By0**2.0 + Bz0**2.0)

	#Density/temperature + scaling
	d0 = getLine(D3,mltJ)
	Cs0 = getLine(C3,mltJ)

	kT0 = (1.0/gamma)*(0.1*Cs0)**2.0 #eV

	Vx0 = getLine(Vx3,mltJ)
	Vy0 = getLine(Vy3,mltJ)
	Vz0 = getLine(Vz3,mltJ)

	#Save to pickle
	print("Writing pickle")
	with open(msDataFile, "wb") as f:
		pickle.dump(B0 ,f)
		pickle.dump(Bx0,f)
		pickle.dump(By0,f)
		pickle.dump(Bz0,f)
		pickle.dump(d0,f)
		pickle.dump(Cs0,f)
		pickle.dump(kT0,f)
		pickle.dump(Vx0,f)
		pickle.dump(Vy0,f)
		pickle.dump(Vz0,f)
		pickle.dump(Rc ,f)


print("Field maxes = ", np.abs(Bx0).max(),np.abs(By0).max(),np.abs(Bz0).max())

#Scale density to number density
n0 = d0/Mp #Number/m3
n0 = 1.0e-6*n0 #Number/cm3

#Scale velocity to km/s
Vx0 = 1.0e-3*Vx0
#Do pic
figName = "mSheath.png"
figSize = (12,8)
figQ = 300 #DPI

lfmv.initLatex()
plt.figure(1,figsize=figSize)
Leg = ['$5 \\times B_{x}$ [nT]','$5 \\times B_{y}$ [nT]','$B_{z}$ [nT]','$0.05 \\times kT$ [eV]','$N_{i}$ [cm$^{-3}$]','$V_{x}$ [km/s]']
#plt.plot(Rc,B0,'ko-',Rc,Bx0,'bo-',Rc,By0,'go-',Bz0,'ro-')
plt.plot(Rc,5*Bx0,'b-')
plt.plot(Rc,5*By0,'g-')
plt.plot(Rc,Bz0,'ro-')
plt.plot(Rc,kT0/20,'c-')
plt.plot(Rc,n0,'k')
plt.plot(Rc,Vx0,'m')

plt.legend(Leg,fontsize="large")
plt.xlabel('Distance [Re]')
plt.ylabel('MHD Quantity')
plt.xlim([9,13.5])
plt.ylim([-50,75])
#plt.show()
plt.savefig(figName,dpi=figQ)
