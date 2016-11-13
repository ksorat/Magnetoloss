import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt

figQ = 300 #DPI
figName = "LossT.png"

RootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/"
fileStub = "100keV.h5part"

spcs = ["H","O","e"]
Leg = ["H+","O+","e-"]

Ns = len(spcs)
#fig = plt.figure(1, figsize=(10, 10))

Np = 100000.0
for i in range(Ns):
	fIn = RootDir + spcs[i] + "." + fileStub
	t,mpTp = lfmpp.getH5p(fIn,"mp")
	mpT = mpTp.sum(axis=1)
	print(mpT.shape)
	plt.plot(t,mpT/Np)

plt.legend(Leg,loc='lower right')
plt.xlabel('Time [s]'); plt.ylabel('Cumulative Loss Fraction')
plt.savefig(figName,dpi=figQ)