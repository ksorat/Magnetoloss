#Look for velocity statistics at given phi in sheath
import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

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
	#print("\tFound %d particles\n"%(Np))
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

plt.figure(figsize=(8,12))

dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

SpcsLab = ["H","O","e"]
cm = plt.cm.get_cmap('RdYlBu')

Leg = ["Hydrogen","Oxygen","Electron"]

Qlab = 'Vertical Velocity [Re/s]'
Spcs = [1]
Phis = [0,30,60]
Ns = len(Spcs)
Np = len(Phis)
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['font.family'] = 'STIXGeneral'
FS = 14
#gs=gridspec.GridSpec(1,3, width_ratios=[4,4,0.2])
#xR = 15*np.ones(Ns+1)
#xR[-1] = 1
xR = [15,1]
gs=gridspec.GridSpec(Np,1+1, width_ratios=xR)


nSpc = 1
for i in range(1):
	for j in range(Np):
		ax = plt.subplot(gs[j,i])
		circ = plt.Circle((0,0),1,color='k')
		ax.add_artist(circ)
		fIn = dirStub + "/" + SpcsLab[nSpc] + "." + fileStub
		print("Reading %s"%(fIn))
	
		#Get x,y,z,vx,vy,vz of particles that are lost
		PhiC = Phis[j]
		print(PhiC)
		s,z,Vx,Vy,Vz = findCrossings(fIn,PhiC=PhiC)
		#Get angle with vertical
		MagV = np.sqrt(Vx**2.0 + Vy**2.0 + Vz**2.0)
		MagVxy = np.sqrt(Vx**2.0 + Vy**2.0)
		ph = PhiC*np.pi/180
		CAlp = (-Vx*np.sin(ph) + Vy*np.cos(ph))/MagVxy
		CAlph = Vz/MagV
		alph = np.arccos(CAlph)*180/np.pi
		vp = np.arctan2(Vy,Vx)*180/np.pi  + 90
		alphP = np.arccos(CAlp)*180/np.pi

		Vphi = -np.sin(ph)*Vx + np.cos(ph)*Vy

		Q = Vz
		#Sc = ax.scatter(s,z,c=alph,vmin=0,vmax=180)
		#Sc = ax.scatter(s,z,c=alphP,vmin=0,vmax=180)
		#Sc = ax.scatter(s[Mask],z[Mask],c=alph[Mask],vmin=80,vmax=100)
		#Sc = ax.scatter(s[Mask],z[Mask],c=alphP[Mask],vmin=0,vmax=180)
		if (np.mod(i,2) == 0):
			Sc = ax.scatter(s,z,c=Q,cmap=cm,vmin=-0.10,vmax=0.10)
		else:
			Mask = (alph>=80) & (alph<=100)
			Sc = ax.scatter(s[Mask],z[Mask],c=Q[Mask],cmap=cm,vmin=-0.10,vmax=0.10)
		 
		
		plt.axis('scaled'); 
		plt.xlim(0,16);
		plt.ylim(-8,8)
		
		
		if (i>0):
			plt.setp(ax.get_yticklabels(),visible=False)
		else:
			plt.ylabel('$\phi = $%4.2f \n Height [Re]'%PhiC,fontsize=FS)
		if (j<Np-1):
			plt.setp(ax.get_xticklabels(),visible=False)
		else:
			plt.xlabel('Radius [Re]',fontsize=FS)
		if (j==0):
			if (i==0):
				plt.title('All Pitch Angles',fontsize=FS)
			else:
				plt.title('Near Equatorial',fontsize=FS)

ax = plt.subplot(gs[:,-1])
plt.colorbar(Sc,cax=ax)#,orientation='horizontal')
plt.ylabel(Qlab,fontsize=FS)
plt.suptitle('Magnetosheath Azimuthal Slices\nOxygen',fontsize=FS+2)
#gs.update(bottom=0.05)
plt.savefig("OxyVzSlc.png")
#plt.show()
