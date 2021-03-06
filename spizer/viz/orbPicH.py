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
import random

np.random.seed(31337)
random.seed(31337)

#Config 1
doSingle = True
pId = 10
#Nstrd = 60
NumT = 60 #How many to trace

#Config 2
# doSingle = True
# pId = 50
# Nstrd = 60

#Nstrd = 4 #What fraction of points to trace


tRadFld=0.00125
tRadTrj=0.0015
FldCmap = "Summer" #Winter,YlGnBu,YlGn

doProd = True
Quiet = False
User = True

SrcF = "fld.vti"
#SrcF = "fldLorez.vti"

if (doSingle):
	SrcP = "pZoom.h5part"
	#SrcP = "../H100/H.100keV.ZoomID.000010.h5part"
	SrcP = "../H100/H.100keV.ZoomID." + "%06d"%pId + ".h5part"
	pId = 0
else:
	SrcP = "prt.h5part"


t,tCr = lfmpp.getH5pid(SrcP,"tCr",pId)
t,xCr = lfmpp.getH5pid(SrcP,"xCr",pId)
t,yCr = lfmpp.getH5pid(SrcP,"yCr",pId)
t,zCr = lfmpp.getH5pid(SrcP,"zCr",pId)
t,xP  = lfmpp.getH5pid(SrcP,"x",pId)
t,yP  = lfmpp.getH5pid(SrcP,"y",pId)
t,zP  = lfmpp.getH5pid(SrcP,"z",pId)
t,mp  = lfmpp.getH5pid(SrcP,"mp",pId)

#Find unique MP crossings
mpT,I = np.unique(tCr,return_index=True)
print("Found %d MP crossings"%(len(I)-1))
#Ix = I[1::Nstrd] #Remove null point

#i0 = Ix[0] #Use first MPX

#i1 = t.shape[0]-1
i0 = 0
i1 = mp.argmax()
I = random.sample(range(i0,i1),NumT)
#print("I0 = %d, I1 = %d, Stride = %d"%(i0,i1,Nstrd))

#print("Found %d slices after first MP"%(i1-i0))
#I = range(i0,i1,Nstrd)

Ns = len(I) #Number of seeds
print("Using %d seeds from crossings"%(Ns))

# x = xCr[I]
# y = yCr[I]
# z = zCr[I]
x = xP[I]
y = yP[I]
z = zP[I]


if (Quiet):
        LaunchNowin()
else:
        Launch()

#Do some defaults
pyv.lfmExprsEB()
pyv.pvInit()

#Field data
OpenDatabase(SrcF)
pyv.lfmPCol(SrcF,"Bmag",vBds=[1,500],cMap="magma",pcOpac=0.85,Legend=False,Log=True)

AddOperator("Slice")
sOp = GetOperatorOptions(0)
sOp.axisType = 2
sOp.project2d = 0
print(sOp)
SetOperatorOptions(sOp)

#Do streams
if (doProd):
	#Only do streams for final version
	pyv.lfmStream(SrcF,"Bfld",x,y,z,cMap=FldCmap,tRad=tRadFld,Legend=False)
	icOp = GetOperatorOptions(0)
	SetOperatorOptions(icOp)
	pcOp = GetPlotOptions()
	SetPlotOptions(pcOp)

	AddOperator("Tube")
	tOp = GetOperatorOptions(1)
	tOp.radiusFractionBBox = tRadFld
	tOp.fineness = 10
	tOp.capping = 1
	SetOperatorOptions(tOp)

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
#print(Nt)
DefineScalarExpression("Trap","Op+Om")
pyv.lfmPCol(SrcP,"Trap",cMap="Cool",vBds=[0,1],Legend=False,Light=True,Inv=False)
pOp = GetPlotOptions()
# pOp.lineType = 1
# pOp.tubeResolution = 100
# pOp.tubeRadiusBBox = 0.025
#print(pOp)
SetPlotOptions(pOp)

AddOperator("PersistentParticles")
ppOp = GetOperatorOptions(0)

ppOp.stopIndex = Nt
ppOp.connectParticles = 1
ppOp.indexVariable = "id"
ppOp.stride = 1
#print(ppOp)
SetOperatorOptions(ppOp)

AddOperator("Tube")
tOp = GetOperatorOptions(1)
tOp.radiusFractionBBox = tRadTrj
tOp.fineness = 10
tOp.capping = 1
#print(tOp)
SetOperatorOptions(tOp)

if (not doSingle):
	AddOperator("Isovolume")
	ivOp = GetOperatorOptions(2)
	ivOp.lbound = pId-1
	ivOp.ubound = pId
	ivOp.variable = "id"
	#print(ivOp)
	SetOperatorOptions(ivOp)


w3d = GetView3D()
#Config 1
w3d.viewNormal = (0.995442, -0.0559352, 0.0772398)
w3d.focus = (-1.025, 0, 0.00223994)
w3d.viewUp = (-0.0764053, 0.0169112, 0.996933)
w3d.viewAngle = 30
w3d.parallelScale = 25.6503
w3d.nearPlane = -51.3007
w3d.farPlane = 51.3007
w3d.imagePan = (-0.0450417, -0.0198424)
w3d.imageZoom = 3.76612
w3d.perspective = 1
w3d.eyeAngle = 2
w3d.centerOfRotationSet = 0
w3d.centerOfRotation = (-1.025, 0, 0.00223994)
w3d.axis3DScaleFlag = 0
w3d.axis3DScales = (1, 1, 1)
w3d.shear = (0, 0, 1)
w3d.windowValid = 0

#Config 2
w3d.viewNormal = (0.25179, 0.965079, 0.0722824)
w3d.focus = (-1.025, 0, 3.19481e-05)
w3d.viewUp = (-0.0166425, -0.0703598, 0.997383)
w3d.viewAngle = 30
w3d.parallelScale = 25.6497
w3d.nearPlane = -51.2993
w3d.farPlane = 51.2993
w3d.imagePan = (0.103121, -0.0140319)
w3d.imageZoom = 3.1125
w3d.perspective = 1
w3d.eyeAngle = 2
w3d.centerOfRotationSet = 0
w3d.centerOfRotation = (-1.025, 0, 3.19481e-05)
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
