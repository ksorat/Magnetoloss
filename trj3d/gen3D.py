import sys
import numpy as np
import os
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
fGen = False
Quiet = True

aIDs = np.arange(1,Np+1)
rootDir = os.path.expanduser('~') + "/Work/Magnetoloss/Data/"
fIn = rootDir+ "H5p/" + h5id

fOut = "o3d.h5part"
if (fGen):
	Mask = np.zeros(Np,dtype=bool)
	for n in range(Np):
		Mask[n] = (aIDs[n] in cIDs)
	
	lfmpp.subH5p(fIn,Mask,len(cIDs),fOut=fOut)

#Now do visit stuff
Src0 = "/glade/u/home/skareem/scratch/lfmVTIs/sns/SNS-Bz-5-Vx400-N5-F200_mhd_1200000.vti"

if (Quiet):
        LaunchNowin()
else:
        Launch()

#Do some defaults
pyv.lfmExprsEB()
pyv.pvInit()
DefineScalarExpression("radius","sqrt(x*x+y*y+z*z)")

#Field data
# OpenDatabase(Src0)
# vBds = [-35,35]
# pyv.lfmPCol(Src0,"dBz",vBds=vBds,Inv=True,pcOpac=0.5)
# AddOperator("Slice")
# sOp = GetOperatorOptions(0)
# sOp.axisType = 2
# sOp.project2d = 0
# SetOperatorOptions(sOp)

OpenDatabase(fOut)
ActivateDatabase(fOut)

pyv.lfmPCol(fOut,"radius",cMap="viridis")
pOp = GetPlotOptions()
pOp.lineType = 1
pOp.tubeResolution = 100
pOp.tubeRadiusBBox = 0.1
print(pOp)
SetPlotOptions(pOp)

AddOperator("PersistentParticles")
ppOp = GetOperatorOptions(0)

ppOp.stopIndex = 450
ppOp.connectParticles = 1
ppOp.indexVariable = "id"
print(ppOp)
SetOperatorOptions(ppOp)

pyv.SetWin3D(Ax=1,Ang=-90)

DrawPlots()
#pyv.cleanLegends(plXs,plYs,plTits)
#pyv.setAtts()

SaveWindow()