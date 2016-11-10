#Calculate statistics for radial excursions in the magnetosheath
import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def findMaxRad(fIn):

	isOut = lfmpp.getOut(fIn)
	t,ids= lfmpp.getH5p(fIn,"id",Mask=isOut)
	t,mp= lfmpp.getH5p(fIn,"mp",Mask=isOut)
	t,x  = lfmpp.getH5p(fIn,"x",Mask=isOut)
	t,y  = lfmpp.getH5p(fIn,"y",Mask=isOut)
	t,z  = lfmpp.getH5p(fIn,"z",Mask=isOut)
	t,tCr = lfmpp.getH5p(fIn,"tCr",Mask=isOut)
	ids = ids[0,:]

	cylR = np.sqrt(x**2.0+y**2.0)
	Np = len(ids)
	Rs = []
	print("\tFound %d particles\n"%(Np))
	print(Np)
	#Find slices for which particle is in sheath
	for n in range(Np):
		#Find last MP xing
		mpn = mp[:,n]
		tCrn = tCr[:,n]
		tSlc1 = tCrn.argmax()
		#Find box xing
		tSlc2 = np.argmax(mpn>0)
		Rn = cylR[tSlc1:tSlc2,n]
		if (len(Rn)>0):
			maxRn = Rn.max()
			Rs.append(maxRn)
	return Rs


dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"
spcs = ["H","O","e"]
cm = plt.cm.get_cmap('RdYlBu')
Leg = ["Hydrogen","Oxygen","Electron"]
Ns = len(spcs)
maxRad = []
for i in range(Ns):
	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	print("Reading %s"%(fIn))
	Rs = findMaxRad(fIn)
	maxRad.append(Rs)

Nb = 50
T0 = 0; Tf = 900
doNorm = True
doLog = False
bins = np.linspace(T0,Tf,Nb)

rFig = plt.hist(maxRad,Nb,normed=doNorm,log=doLog)
plt.legend(Leg)
plt.xlabel("Maximum Cyl R in Sheath [Re]")
plt.ylabel("Fraction")
plt.savefig("MaxR_MPx.png")
plt.show()
plt.close()