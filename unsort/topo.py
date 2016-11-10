import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fld = "/Users/soratka1/Work/magnetoloss/eqSlc/eqSlc.0250.vti"
IDs = [1335,301,95834,12593,63464,75685]
fIn = "/Users/soratka1/Work/magnetoloss/synth/O.100keV.h5part"

Bz = lfmv.getVTI_SlcSclr(fld,fldStr='dBz')
xm = np.linspace(-15.0,13,560)
ym = np.linspace(-20.0,20,801)
xx,yy = np.meshgrid(xm,ym)
Ni = len(IDs)
#fig = plt.figure(1, figsize=(15,10))
gs = gridspec.GridSpec(Ni, 1)

t,x  = lfmpp.getH5p(fIn,"x")
t,y  = lfmpp.getH5p(fIn,"y")
t,z  = lfmpp.getH5p(fIn,"z")
t,pids  = lfmpp.getH5p(fIn,"id")
t,Om  = lfmpp.getH5p(fIn,"Om")
t,Op  = lfmpp.getH5p(fIn,"Op")

Omp = (Om+Op)
for n in range(len(IDs)):
	pid = IDs[n]
	npid = (pids == pid).argmax()
	xp = x[:,npid]
	yp = y[:,npid]
	zp = z[:,npid]
	cp = Omp[:,npid]
	#ax = plt.subplot(gs[n,0])
	plt.scatter(xp,yp,c=cp,vmin=0,vmax=1, cmap="cool")#,edgecolors='none')
	plt.plot(xp,yp,'k',linewidth=0.5)
	lfmv.addEarth2D()
	
	plt.xlabel('X [Re]',fontsize="x-large");plt.ylabel('Y [Re]',fontsize="x-large");
	plt.contour(xx,yy,Bz.T,np.linspace(-5,5,5),cmap="RdGy_r")
	plt.axis('scaled')
	plt.xlim(-15,10); plt.ylim(-20,20);
	fOut = "Topo.%d.png"%(n)
	plt.savefig(fOut)
	plt.close('all')
	# ax = plt.subplot(gs[n,1])
	# plt.scatter(yp,zp,c=cp,vmin=0,vmax=1, cmap="cool",edgecolors='none')
	# #lfmv.addEarth2D()
	# plt.axis('scaled')
	# plt.xlabel('Y [Re]');plt.ylabel('Z [Re]');
	# #plt.xlim(-20,20); plt.ylim(-8,8);


#plt.suptitle("Example O+ Trajectories")


