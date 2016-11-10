import argparse
import numpy as np
import os
import lfmViz as lfmv
import lfmPostproc as lfmpp
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

fIn = '/Users/soratka1/Work/magnetoloss/synth/H.100keV.h5part'

Ri,Pi,Li,Tmp = lfmpp.getSphLoss1st(fIn)
plt.hist2d(Pi,Tmp,Nb,norm=LogNorm())
