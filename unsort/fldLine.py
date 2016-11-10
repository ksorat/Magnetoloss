#Reads in 3D Cartesian field VTI and plots some field lines
#3D field data is in code units, transfer to B field in nT

import numpy as np
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import lfmGrids as lfm
import pyVisit as pyv

#fIn = "fldDatLorez.vti"
fIn = "fldDat.vti"
db = fIn
PhiCs = [0.0,30,60]

P0 = (2.2,0,0)
P1 = (15,0,0)

pcOpac = 0.75
pcOpacP = 0.35

Launch()

OpenDatabase(fIn)
md = GetMetaData(fIn) #Metadata

#Import definitions
pyv.lfmExprsEB()

#Start plotting
pyv.setAtts() #Some defaults
pyv.lfmPCol(db,"dBz",vBds=(-25,25),Inv=True,pcOpac=pcOpac,Light=False)

# Do a lineout on all 4 variables to produce 4 curves.
Lineout(P0, P1, ("Bx","By","Bz"))
