#Use single particle "zoom" run and static field data to generate pic of Spizer orbit

import sys
import numpy as np
import os
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv
import lfmPostproc as lfmpp


pId = 32


SrcF = "fld.vti"
SrcP = "prt.h5part"
#tCr = lfmpp.getH5pid(SrcP,"tCr",pId)

Quiet = False
User = True

if (Quiet):
        LaunchNowin()
else:
        Launch()

#Do some defaults
pyv.lfmExprsEB()
#pyv.pvInit()

#Field data
OpenDatabase(SrcF)
vBds = [-35,35]
#pyv.lfmPCol(Src0,"dBz",vBds=vBds,Inv=True,pcOpac=0.75,Legend=False)
#pyv.lfmPCol(SrcF,"Bmag",vBds=[1,500],cMap="viridis",pcOpac=0.5,Legend=True,Log=True)
pyv.lfmPCol(SrcF,"Bmag",vBds=[1,500],cMap="viridis",Legend=True,Log=True)

AddOperator("Slice")
sOp = GetOperatorOptions(0)
sOp.axisType = 2
sOp.project2d = 0
print(sOp)
SetOperatorOptions(sOp)

# pyv.lfmPCol(Src0,"Bmag",vBds=[1,500],cMap="viridis",pcOpac=0.5,Legend=False,Log=True)
# AddOperator("Slice")
# sOp = GetOperatorOptions(0)
# sOp.axisType = 0
# sOp.project2d = 0
# sOp.originIntercept = 5.0
# SetOperatorOptions(sOp)


#Block out central cutout
AddPlot("Contour","RadAll")
cOps = GetPlotOptions()
cOps.colorType = 0
cOps.singleColor = (0, 0, 0, 255)
cOps.singleColor = (192, 192, 192, 255)
cOps.contourMethod = 1
cOps.contourValue = (2.2)
cOps.legendFlag = 0
SetPlotOptions(cOps)

#Particles
OpenDatabase(SrcP)
ActivateDatabase(SrcP)

#pyv.lfmPCol(fOut,"id",cMap="cpk_jmol",Legend=False)
pyv.lfmPCol(SrcP,"id",cMap="Reds",vBds=[3,20],Legend=False,Light=True,Inv=False)
pOp = GetPlotOptions()
# pOp.lineType = 1
# pOp.tubeResolution = 100
# pOp.tubeRadiusBBox = 0.025
print(pOp)
SetPlotOptions(pOp)

AddOperator("PersistentParticles")
ppOp = GetOperatorOptions(0)

ppOp.stopIndex = 4500
ppOp.connectParticles = 1
ppOp.indexVariable = "id"
ppOp.stride = 100
print(ppOp)
SetOperatorOptions(ppOp)

AddOperator("Tube")
tOp = GetOperatorOptions(1)
tOp.radiusFractionBBox = 0.0025
tOp.fineness = 10
tOp.capping = 1
print(tOp)
SetOperatorOptions(tOp)

AddOperator("Isovolume")
ivOp = GetOperatorOptions(2)
ivOp.lbound = pId-1
ivOp.ubound = pId
ivOp.variable = "id"
print(ivOp)
SetOperatorOptions(ivOp)

#Back and up
pyv.SetWin3D(Ax=1,Ang=+90)
pyv.SetWin3D(Ax=2,Ang=+90)
pyv.SetWin3D(Ax=0,Ang=+45)
pyv.SetWin3D(Zoom=1.2)

#Front and up

DrawPlots()
#pyv.cleanLegends(plXs,plYs,plTits)
pyv.setAtts()

SaveWindow()
if (User and not Quiet):
	OpenGUI()
