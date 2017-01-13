import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp

#Routine to find azimuthal crossings
def findCrossings(fIn,PhiC=30.0,DelPhi=5):

	isOut = lfmpp.getOut(fIn)
	t,ids= lfmpp.getH5p(fIn,"id",Mask=isOut)
	t,mp= lfmpp.getH5p(fIn,"mp",Mask=isOut)
	t,x  = lfmpp.getH5p(fIn,"x",Mask=isOut)
	t,y  = lfmpp.getH5p(fIn,"y",Mask=isOut)
	t,z  = lfmpp.getH5p(fIn,"z",Mask=isOut)
	t,vx = lfmpp.getH5p(fIn,"vx",Mask=isOut)
	t,vy = lfmpp.getH5p(fIn,"vy",Mask=isOut)
	t,vz = lfmpp.getH5p(fIn,"vz",Mask=isOut)
	t,tCr = lfmpp.getH5p(fIn,"tCr",Mask=isOut)
	ids = ids[0,:]

	phi = np.arctan2(y,x)*180/np.pi
	if (np.abs(PhiC) >5):
		#Fix for flop
		phi[phi<0] = phi[phi<0] + 360
	Np = len(ids)
	print("\tFound %d particles\n"%(Np))
	Vx = []
	Vy = []
	Vz = []
	sM = []
	zM = []

	for n in range(Np):
		
		#Find last MP xing
		mpn = mp[:,n]
		tCrn = tCr[:,n]
		tSlc1 = tCrn.argmax()
		#Find box xing
		tSlc2 = np.argmax(mpn>0)
		pn = phi[tSlc1:tSlc2,n]
		
		#print(pn.shape)
		#Identify sign changes and bound for within +/- 5 degrees
		#Otherwise funny business @ p=0/360
		dp = pn-PhiC
		dpsgn = np.sign(dp)
		dpFlp = ( (np.roll(dpsgn,1)-dpsgn) != 0).astype(int)
		dpFlp = (dpFlp > 0)
		dpAbs = np.abs(dp) <= DelPhi
		isPCr = dpFlp & dpAbs
		#print(len(pn),tCr.sum())
		Nx = isPCr.sum()
		if (Nx>0):
			vxn = vx[tSlc1:tSlc2,n]
			vyn = vy[tSlc1:tSlc2,n]
			vzn = vz[tSlc1:tSlc2,n]
			xn  =  x[tSlc1:tSlc2,n]
			yn  =  y[tSlc1:tSlc2,n]
			zn  =  z[tSlc1:tSlc2,n]


			vxx = vxn[isPCr]
			vyx = vyn[isPCr]
			vzx = vzn[isPCr]
			xx =  xn[isPCr]
			yx =  yn[isPCr]
			zx =  zn[isPCr]

			for i in range(Nx):
				Vx.append(vxx[i])
				Vy.append(vyx[i])
				Vz.append(vzx[i])
				sM.append(np.sqrt(xx[i]**2.0+yx[i]**2.0))
				zM.append(zx[i])
			#print(n,isPCr)
	Vx = np.array(Vx)
	Vy = np.array(Vy)
	Vz = np.array(Vz)
	sM = np.array(sM)
	zM = np.array(zM)
	print("\tPhi = %5.2f, NumP = %d\n"%(PhiC,len(Vx)))
	return sM,zM,Vx,Vy,Vz

