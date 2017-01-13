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

doSingle = True
pId = 50
Nstrd = 1 #What fraction of MP crossings to trace
Quiet = False
User = True
doProd = True

SrcF = "fld.vti"
if (doSingle):
	SrcP = "pZoom.h5part"
	pId = 0
else:
	SrcP = "prt.h5part"

t,tCr = lfmpp.getH5pid(SrcP,"tCr",pId)
t,xCr = lfmpp.getH5pid(SrcP,"xCr",pId)
t,yCr = lfmpp.getH5pid(SrcP,"yCr",pId)
t,zCr = lfmpp.getH5pid(SrcP,"zCr",pId)

#Find unique MP crossings
mpT,I = np.unique(tCr,return_index=True)
print("Found %d MP crossings"%(len(I)-1))
I = I[1::Nstrd] #Remove null point
Ns = len(I) #Number of seeds
print("Using %d seeds from MP crossings"%(Ns))

x = xCr[I]
y = yCr[I]
z = zCr[I]

if (Quiet):
        LaunchNowin()
else:
        Launch()

#Do some defaults
pyv.lfmExprsEB()
pyv.pvInit()

#Field data
OpenDatabase(SrcF)
pyv.lfmPCol(SrcF,"Bmag",vBds=[1,500],cMap="viridis",pcOpac=0.85,Legend=False,Log=True)

AddOperator("Slice")
sOp = GetOperatorOptions(0)
sOp.axisType = 2
sOp.project2d = 0
print(sOp)
SetOperatorOptions(sOp)

#Do streams
if (doProd):
	#Only do streams for final version
	scMap = "Blues"
	scMap = "Reds"
	pyv.lfmStream(SrcF,"Bfld",x,y,z,cMap=scMap,tRad=0.0025,Legend=False)
	icOp = GetOperatorOptions(0)
	#icOp.dataValue = 10
	#icOp.dataVariable = "dPhi"
	SetOperatorOptions(icOp)
	pcOp = GetPlotOptions()
	#pcOp.minFlag=1; pcOp.maxFlag=1
	#pcOp.min = -dpMax; pcOp.max = dpMax
	SetPlotOptions(pcOp)


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

Nt = TimeSliderGetNStates()
print(Nt)
DefineScalarExpression("Trap","Op+Om")
pyv.lfmPCol(SrcP,"Trap",cMap="Cool",vBds=[0,1],Legend=False,Light=True,Inv=False)
pOp = GetPlotOptions()
# pOp.lineType = 1
# pOp.tubeResolution = 100
# pOp.tubeRadiusBBox = 0.025
print(pOp)
SetPlotOptions(pOp)

AddOperator("PersistentParticles")
ppOp = GetOperatorOptions(0)

ppOp.stopIndex = Nt
ppOp.connectParticles = 1
ppOp.indexVariable = "id"
ppOp.stride = 1
print(ppOp)
SetOperatorOptions(ppOp)

AddOperator("Tube")
tOp = GetOperatorOptions(1)
tOp.radiusFractionBBox = 0.005
tOp.fineness = 10
tOp.capping = 1
print(tOp)
SetOperatorOptions(tOp)

if (not doSingle):
	AddOperator("Isovolume")
	ivOp = GetOperatorOptions(2)
	ivOp.lbound = pId-1
	ivOp.ubound = pId
	ivOp.variable = "id"
	print(ivOp)
	SetOperatorOptions(ivOp)


w3d = GetView3D()
w3d.viewNormal = (0.878976, -0.138305, 0.45637)
w3d.focus = (-1.025, 0, 0.000166655)
w3d.viewUp = (-0.434782, 0.160665, 0.886087)
w3d.viewAngle = 30
w3d.parallelScale = 25.6497
w3d.nearPlane = -51.2994
w3d.farPlane = 51.2994
w3d.imagePan = (0, 0)
w3d.imageZoom = 1.452
w3d.perspective = 1
w3d.eyeAngle = 2
w3d.centerOfRotationSet = 0
w3d.centerOfRotation = (-1.025, 0, 0.000166655)
w3d.axis3DScaleFlag = 0
w3d.axis3DScales = (1, 1, 1)
w3d.shear = (0, 0, 1)
w3d.windowValid = 0

SetView3D(w3d)

DrawPlots()
#pyv.cleanLegends(plXs,plYs,plTits)

pyv.setAtts()

SaveWindow()
if (User and not Quiet):
	OpenGUI()
