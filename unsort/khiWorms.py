import argparse
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt

Ion = False
K = 5
subVTI = True
Eqt = True

if (Ion):
	fIn = '/Users/soratka1/Work/magnetoloss/synth/H.100keV.h5part'
	#Find particles whose last Teq is in range
	T0 = 3400
	T1 = 3500
	P0 = -135; P1 = -80
else:
	fIn = '/Users/soratka1/Work/magnetoloss/synth/e.100keV.h5part'
	fIn = '/Users/soratka1/Work/magnetoloss/debug/e.100keV.h5part'
	#Find particles whose last Teq is in range
	T0 = 2250
	T1 = 2300
	P0 = 80; P1 = 135




fOut = "khiSub.h5part"
Out = lfmpp.getOut(fIn)

t,x   = lfmpp.getH5p(fIn,"x")
t,y   = lfmpp.getH5p(fIn,"y")
t,z   = lfmpp.getH5p(fIn,"z")

t,Teq = lfmpp.getH5pFin(fIn,"Teq")
t,ids = lfmpp.getH5p(fIn,"id")
id0   = ids[0,:]

R,Phi,Lambda = lfmpp.getSphLoss(fIn)

Out[Out] = (Phi>=P0) & (Phi<=P1)
Mask = (Teq>=T0) & (Teq<=T1) & Out

Np = Mask.sum()
t,xeq = lfmpp.getH5p(fIn,"xeq")
t,yeq = lfmpp.getH5p(fIn,"yeq")

xP = xeq[:,Mask]
yP = yeq[:,Mask]
id0 = id0[Mask]

print(Np)
print(K)
if (Np<K):
	K = Np
if (subVTI):
	lfmpp.subH5p(fIn,Mask,K,fOut=fOut,xEq=Eqt)


print(id0)
if (K>=1):
	Ind = np.random.choice(Np,K,replace=False)
	xP = xP[:,Ind]
	yP = yP[:,Ind]
	Np = xP.shape[1]
for n in range(Np):
	plt.plot(xP[:,n],yP[:,n])

plt.axis('equal')
lfmv.addEarth2D()
plt.show()