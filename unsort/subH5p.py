import argparse
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt

fIn = '/Users/soratka1/Work/magnetoloss/synth/e.100keV.h5part'
fOut = "eSub.h5part"
Out = lfmpp.getOut(fIn)
K = 5

t,x = lfmv.getH5p(fIn,"x")
t,y = lfmv.getH5p(fIn,"y")
t,z = lfmv.getH5p(fIn,"z")
t,ids = lfmv.getH5p(fIn,"id")
id0 = ids[0,:]
trsh, alph0 = lfmpp.getPitch(fIn)


# idMin = 100
# idMax = 120
# idMask = np.logical_and(idMin <= id0, idMax >= id0)
# uMask = idMask

# Mask = 
# xsub =   x[:,Mask]
# ysub =   y[:,Mask]
# zsub = 0*z[:,Mask]
# ids =    id0[Mask]

# lfmpp.mkH5p(fOut, ids,xsub,ysub,zsub)
uMask = (alph0>=80)
print(uMask.sum())
print(K)
Mask = np.logical_and(Out,uMask)
lfmpp.subH5p(fIn,Mask,K)
