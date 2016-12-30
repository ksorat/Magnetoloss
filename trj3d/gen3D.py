import sys
import numpy as np
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv
import lfmPostproc as lfmpp

#Grab several Oxygen IDs and create easier to use H5p

Np = 100000
cIDs = [1335,301,95834,12593,63464,75685]
h5id = "O.100keV.h5part"

aIDs = np.arange(1,Np+1)
fIn = os.path.expanduser('~') + "/Work/Magnetoloss/Data/H5p/" + h5id
Mask = np.zeros(Np,dtype=bool)
for n in range(Np):
	Mask[n] = (aIDs[n] in cIDs)

lfmpp.subH5p(fIn,Mask,len(cIDs))