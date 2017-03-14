#Calculate various particle drift velocities
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import cPickle as pickle
import matplotlib.gridspec as gridspec
from matplotlib.colors import LogNorm
import vtk
from vtk.util import numpy_support as npvtk

#Various constants
Qe = 4.8032e-10 #Electron charge [CGS]
Me = 9.1094e-28 #Electron mass [g]
Re = 6.38e+8 #Earth radius [cm]
clightCMS = 2.9979e+10 #Speed of light [cm/s]

EBscl = (Qe*Re/Me)/(clightCMS**2.0)

def Cull(xx,yy,Vx,Vy,IndK,Nv,Tiny=0.025):
	np.random.seed(seed=31337)

	nV = np.sqrt(Vx**2.0+Vy**2.0)
	IndT = (nV >= Tiny)
	IndG = IndK & IndT

	Vx = Vx[IndG]
	Vy = Vy[IndG]
	xxV = xx[IndG]
	yyV = yy[IndG]

	Ng = len(Vx)
	
	IndS = np.random.choice(Ng,size=Nv,replace=False)

	xxV = xxV[IndS]
	yyV = yyV[IndS]
	Vx  = Vx [IndS]
	Vy  = Vy [IndS]
	
	return xxV,yyV,Vx,Vy

def SmoothOp(A,sig=1):
	import scipy
	import scipy.ndimage

	from scipy.ndimage.filters import gaussian_filter
	A = gaussian_filter(A,sig)

	return A

def sclMag(Bx,By,Bz):
        #Incoming data is in dim-less units (EB from LFMTP)
        #Scale to nT
        eb2cgs = 1/EBscl #Convert EB to CGS
        G2nT = 10**5.0 #Convert Gauss to nT
        scl = (eb2cgs*G2nT)
        return SmoothOp(scl*Bx),SmoothOp(scl*By),SmoothOp(scl*Bz)

def sclElec(Ex,Ey,Ez):
        #Incoming data is in dim-less units (EB from LFMTP)
        #Scale to mili-Volts over meters [mV/m]

        eb2cgs = 1/EBscl #Convert EB to CGS
        G2T = 10**(-4.0)
        V2mV = 10**3.0
        clight = 2.9979e+8 #Speed of light, [m/s]
        #Convert E -> "Gauss" then Tesla, xC_light to V/m then mV/m
        scl = eb2cgs*G2T*clight*V2mV
        return SmoothOp(scl*Ex),SmoothOp(scl*Ey),SmoothOp(scl*Ez)

def getMidplane(fname,fldStr='B'):
	data = lfmv.getVTI_Data(fname)
	pdat = data.GetPointData() #Assuming point data
	fldDat = pdat.GetArray(fldStr)
	rawDat = npvtk.vtk_to_numpy(fldDat)
	dims = [i for i in data.GetDimensions()]
	dims.append(3) #For vector structure
	Vec = rawDat.reshape(dims,order='F')
	Zeq = np.int( np.ceil( 0.5*dims[2] ) )
	Vx = Vec[:,:,Zeq-1:Zeq+2,0].squeeze()
	Vy = Vec[:,:,Zeq-1:Zeq+2,1].squeeze()
	Vz = Vec[:,:,Zeq-1:Zeq+2,2].squeeze()

	return Vx,Vy,Vz

def getGrid(fname):
	ori,dx,ex = lfmv.getVTI_Eq(fname)
	xi = ori[0] + np.arange(ex[0],ex[1]+1)*dx[0]
	yi = ori[1] + np.arange(ex[2],ex[3]+1)*dx[1]
	return xi,yi,dx[0],dx[1]

def Cross(Ax,Ay,Az,Bx,By,Bz):
	Cx = Ay*Bz - Az*By
	Cy = Az*Bx - Ax*Bz
	Cz = Ax*By - Ay*Bx
	return Cx,Cy,Cz

def Del2(A,dx,dy,dz):
	Ax,Ay,Az = np.gradient(A,dx,dy,dz) #[X/Re]
	Axx,Axy,Axz = np.gradient(Ax,dx,dy,dz) #[X/Re2]
	Ayx,Ayy,Ayz = np.gradient(Ax,dx,dy,dz) #[X/Re2]
	Azx,Azy,Azz = np.gradient(Ax,dx,dy,dz) #[X/Re2]

	LapA = Axx+Ayy+Azz
	return LapA
def ExBs(Ex,Ey,Ez,Bx,By,Bz,dx,dy,dz,Ki=100,TINY=1.0e-8):
	Re = 6380.0 #Earth Radius [km]
	Re2 = Re*Re
	#Get uniform/non-uniform pieces of ExB drift
	B2 = Bx*Bx+By*By+Bz*Bz
	B2 = np.maximum(B2,TINY)

	EBx,EBy,EBz = Cross(Ex,Ey,Ez,Bx,By,Bz)
	EBx = EBx/B2
	EBy = EBy/B2
	EBz = EBz/B2

	Rg = (4.6*1.0e+3)*np.sqrt(Ki)/np.sqrt(B2) #[km]
	RgS = Rg[:,:,1].squeeze()

	Vu = np.sqrt(EBx**2.0+EBy**2.0+EBz**2.0) #Uniform
	VuS = Vu[:,:,1].squeeze()

	VnuX = Del2(EBx,dx,dy,dz)
	VnuY = Del2(EBy,dx,dy,dz)
	VnuZ = Del2(EBz,dx,dy,dz)
	VnuX = VnuX/Re2
	VnuY = VnuY/Re2
	VnuZ = VnuZ/Re2

	Vnu = np.sqrt(VnuX**2.0+VnuY**2.0+VnuZ**2.0)
	VnuS = Vnu[:,:,1].squeeze()
	VnuS = 0.25*RgS*RgS*VnuS

	return VuS,VnuS
doKev = True
doExB = False

MagM = -0.311*1.0e+5 #Mag moment, Gauss->nT
clight = 2.9979e+8 #Speed of light, [m/s]
Re = 6380.0 #Earth Radius [km]
q = 1.6021766e-19 #Coulombs
Scl = (1.0e+6)/( q*6.242e+15*1.0e+3)
TINY = 1.0e-8

fldSlc = "mhd.vti"
#fldSlc = "testSlc.vti"

lfmv.ppInit()

#Get grid
xc,yc,dx,dy = getGrid(fldSlc)
Nx = len(xc)
Ny = len(yc)
xi = np.linspace(xc[0]-0.5*dx,xc[-1]+0.5*dx,Nx+1)
yi = np.linspace(yc[0]-0.5*dy,yc[-1]+0.5*dy,Ny+1)

xxi,yyi = np.meshgrid(xi,yi,indexing='ij')
xx,yy = np.meshgrid(xc,yc,indexing='ij')


dz = dx #Assume isotropic
Nk = 3
zc = np.linspace(-dz,dz,Nk)

#Get midplane slices
dBx,dBy,dBz = getMidplane(fldSlc)
Ex,Ey,Ez = getMidplane(fldSlc,fldStr='E')

#Scale units
dBx,dBy,dBz = sclMag(dBx,dBy,dBz)
Ex,Ey,Ez = sclElec(Ex,Ey,Ez)

#Define Earth field
eBx = np.zeros_like(dBx)
eBy = np.zeros_like(dBx)
eBz = np.zeros_like(dBx)

for k in range(Nk):
	zk = zc[k]
	Rc = np.sqrt(xx**2.0+yy**2.0+zk**2.0)
	Ind = (Rc<=2.01)
	Rc[Ind] = 2.01

	Rm5 = Rc**(-5.0)
	eBx[:,:,k] = 3*MagM*xx*zk*Rm5
	eBy[:,:,k] = 3*MagM*yy*zk*Rm5
	eBz[:,:,k] = MagM*(3*zk*zk - Rc*Rc)*Rm5

Bx = eBx+dBx
By = eBy+dBy
Bz = eBz+dBz

#Now have fields, can calulate drifts
Bmag = np.sqrt(Bx**2.0+By**2.0+Bz**2.0)
Emag = np.sqrt(Ex**2.0+Ey**2.0+Ez**2.0)
Bmag = np.maximum(Bmag,TINY)
Emag = np.maximum(Emag,TINY)

GBx,GBy,GBz = np.gradient(Bmag,dx,dy,dz) #[nT/Re]
GBx = GBx/Re #Convert to nT/km
GBy = GBy/Re
GBz = GBz/Re

BxGBx = By*GBz - Bz*GBy
BxGBy = Bz*GBx - Bx*GBz
BxGBz = Bx*GBy - By*GBx

BxGBMag = np.sqrt(BxGBx**2.0+BxGBy**2.0+BxGBz**2.0)

VdPkev = Scl*BxGBMag/(Bmag**3.0)

Veb = 1000*Emag/Bmag #ExB drift [km/s]

#eqKev = (2/3.0)*Veb/VdPkev #Using Kperp + 2Kpar
eqKev = (2*Veb/VdPkev) #Only gradient, alpha=45o


RcSlc = np.sqrt(xx**2.0+yy**2.0)
IndS = RcSlc<=2.01

#Get vector components ExB drift
EBx,EBy,EBz = Cross(Ex,Ey,Ez,Bx,By,Bz)
B2 = Bmag*Bmag
Vebx = EBx/B2
Veby = EBy/B2
Vebz = EBz/B2
VebxS = Vebx[:,:,1].squeeze()
VebyS = Veby[:,:,1].squeeze()
VebzS = Vebz[:,:,1].squeeze()

if (doKev):
	fig = plt.figure(figsize=(6,8))
	figQ = 300 #DPI
	gs = gridspec.GridSpec(1,2,width_ratios=[25,1],right=0.8,left=0.1)

	eqKevSlc = eqKev[:,:,1].squeeze()
	eqKevSlc[IndS] = 0.0

	K0 = 1; K1 = 500
	vNorm = LogNorm(K0,K1)
	cMap = "inferno"

	Ax = fig.add_subplot(gs[0,0])
	Ax.pcolormesh(xxi,yyi,eqKevSlc,norm=vNorm,vmin=K0,vmax=K1,cmap=cMap,shading='gourand')

	lfmv.addEarth2D()

	#Add directions
	ebVmag = np.sqrt(VebxS**2.0+VebyS**2.0)
	ebV = np.sqrt(VebxS**2.0+VebyS**2.0+VebzS)
	plt.axis('scaled')

	#Config #1
	Kc = 10
	KcM = 500
	Nv = 2500
	Scl = 0.375
	Tiny=0.025
	doUnit = False
	doColor = False	
	plt.xlim(-14.5,12)
	plt.ylim(-20,20)

	#Config #2
	# Kc = 10
	# KcM = 10000
	# Nv = 10000
	# Scl = 0.375
	# Tiny=0.025
	# doUnit = False
	# doColor = False
	# plt.xlim(-3,5)
	# plt.ylim(8,16)

	Ind = (eqKevSlc<Kc) | (eqKevSlc>KcM)
	IndG = (eqKevSlc>Kc) & (eqKevSlc<KcM)
	if (doUnit):
		Vx = VebxS/ebVmag
		Vy = VebyS/ebVmag
		Vz = VebzS/ebVmag
	else:
		Vx = VebxS
		Vy = VebyS
		Vz = VebzS

	xyF = ebVmag/ebV
	xxV,yyV,Vx,Vy = Cull(xx,yy,Vx,Vy,IndG,Nv,Tiny)


	print(len(xxV))
	if (doColor):
		Ax.quiver(xxV,yyV,Vx,Vy,xyF,cmap="winter",vmin=0,vmax=1,scale=2,alpha=0.5,units='xy',pivot='mid',edgecolor='k',linewidth=0.25)
	else:	
		Ax.quiver(xxV,yyV,Vx,Vy,scale=Scl,alpha=0.5,units='xy',pivot='mid',color='dodgerblue',edgecolor='k',linewidth=0.25,minlength=TINY)
	#



	plt.xlabel('GSM-X [Re]')
	plt.ylabel("GSM-Y [Re]")
	Axc = fig.add_subplot(gs[0,1])
	cb = mpl.colorbar.ColorbarBase(Axc,cmap=cMap,norm=vNorm,orientation='vertical')
	cb.set_label("Energy [keV]\n$V_{E \\times B} = V_{\\nabla}$",fontsize="small")
	plt.savefig("vMap.png",dpi=figQ)

if (doExB):
	f0 = 1.0e-4
	f1 = 1.0e+1
	vNorm = LogNorm(f0,f1)
	cMap = "inferno"
	Vu,Vnu = ExBs(Ex,Ey,Ez,Bx,By,Bz,dx,dy,dz)
	dVeb = Vnu/Vu
	plt.pcolormesh(xx,yy,dVeb,norm=vNorm,vmin=f0,vmax=f1,cmap=cMap,shading='flat')
	plt.colorbar()

