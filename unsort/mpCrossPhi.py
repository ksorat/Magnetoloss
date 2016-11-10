#Calculate time lost particles spend on open field lines before leaving box
#Look at correlation of number of crossings with MLT of first MP crossing

import numpy as np
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

dirStub = "/Users/soratka1/Work/magnetoloss/synth"
fileStub = "100keV.h5part"

spcs = ["H","O","e"]
Leg = ["Hydrogen","Oxygen","Electron"]

Ns = len(spcs)


aNumX = []
LogScl = LogNorm(1,500)
fig = plt.figure(1, figsize=(20,6))

for i in range(2):
	#xBin = np.linspace(-180,180,100)
	xBin = np.linspace(-60,60,100)
	yBin = np.linspace(0,30,30)

	fIn = dirStub + "/" + spcs[i] + "." + fileStub
	print("Reading %s"%(fIn))
	print("Species %s"%(Leg[i]))
	isOut = lfmpp.getOut(fIn)
	pid, NumX = lfmpp.countMPX(fIn,isOut)
	R, PhiF, Lambda, Tmp = lfmpp.getSphLoss1st(fIn)
	R,PhiL,Lambda = lfmpp.getSphLoss(fIn)
	DelPhi = PhiL-PhiF
	#IndF = (PhiF<=45) & (PhiF>=-45)
	#IndL = (PhiL<=0) & (PhiL>=-45)
	#Ind = IndF & IndL
	#DelPhi = PhiL[Ind]-PhiF[Ind]
	#NumX = NumX[Ind]
	titS = "%s 100 keV"%Leg[i]
	plt.subplot(1,3,i+1)
	#plt.hist2d(Phi,NumX,[xBin,yBin],norm=LogScl)

	plt.hist2d(DelPhi,NumX,[xBin,yBin],norm=LogScl)
	#plt.hist2d(DelPhi,NumX,[xBin,yBin])
	plt.xlim( (-120,120) ); plt.xlabel("Delta-Phi")
	plt.ylim( (0,30) ); plt.ylabel("# of Crossings")
	plt.colorbar()
	plt.title(titS)


