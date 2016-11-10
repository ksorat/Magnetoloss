import argparse
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt

fIn = '/Users/soratka1/Work/magnetoloss/synth/e.100keV.h5part'
fOut = "eLine.h5part"
Out = lfmpp.getOut(fIn)
K = 5

t,x = lfmv.getH5p(fIn,"x")
t,y = lfmv.getH5p(fIn,"y")
t,z = lfmv.getH5p(fIn,"z")
t,ids = lfmv.getH5p(fIn,"id")
id0 = ids[0,:]


uMask = (id0 == 27417)

Mask = np.logical_and(Out,uMask)
lfmpp.subH5p(fIn,Mask,1)
