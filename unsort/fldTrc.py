#Reads in 3D Cartesian field VTI and plots some field lines
#3D field data is in code units, transfer to B field in nT

import numpy as np
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import lfmGrids as lfm
import pyVisit as pyv

fIn = "fldDatLorez.vti"
#fIn = "fldDat.vti"
db = fIn
pcOpac = 0.75
#Num samples
#Circle: Phi/Radius
#Box: X/Y/Z
Nx1 = 5; Nx2 = 5; Nx3 = 1
doCirc = False
slRad = 9.0
#slBoxX = [-10,10]; slBoxY = [-15,15]; slBoxZ = [-4,4]
slBoxX = [0,12]; slBoxY = [0,20]; slBoxZ = [-4*0,4*0]
slCMap = "hot_desaturated"
slCMap = "Cool"

#For Earth dipole field
MagM = -0.311*1.0e+5 #Mag moment, Gauss->nT
eBxStr = "3*xRe*zRe*(%e)*rm5"%(MagM)
eByStr = "3*yRe*zRe*(%e)*rm5"%(MagM)
eBzStr = "(3.0*zRe*zRe - Radius*Radius)*(%e)*rm5"%(MagM)
#To scale EB-LFMTP data
eb2cgs = 1/lfm.EBscl #Convert EB to CGS
G2nT = 10**5.0 #Convert Gauss to nT
V2mV = 10**3.0 #-> miliVolts/m
eb2nT = (eb2cgs*G2nT)
dBxStr = "(%e)*B[0]"%(eb2nT)
dByStr = "(%e)*B[1]"%(eb2nT)
dBzStr = "(%e)*B[2]"%(eb2nT)
vScl = lfm.clight/lfm.Re
EScl = eb2cgs*G2nT*lfm.clight*V2mV

VelStr = "if( ge(Bmag,1.0e-8), (%e)*cross(Efld,Bfld)/dot(Bfld,Bfld) , {0,0,0} )"%(vScl)

Launch()

OpenDatabase(fIn)
md = GetMetaData(fIn) #Metadata

#Define expressions (Geometry)
DefineScalarExpression("RadAll","polar_radius(mesh)")
DefineScalarExpression("Radius","if( ge(RadAll, 2.1), RadAll, 2.1)") #Respect cutout
DefineScalarExpression("xRe","coord(mesh)[0]")
DefineScalarExpression("yRe","coord(mesh)[1]")
DefineScalarExpression("zRe","coord(mesh)[2]")
DefineScalarExpression("rm5","Radius^(-5.0)")

#Earth field
DefineScalarExpression("eBx",eBxStr)
DefineScalarExpression("eBy",eByStr)
DefineScalarExpression("eBz",eBzStr)

#Residual field
DefineScalarExpression("dBx",dBxStr)
DefineScalarExpression("dBy",dByStr)
DefineScalarExpression("dBz",dBzStr)

#Total field components and vector
DefineScalarExpression("Bx","eBx+dBx")
DefineScalarExpression("By","eBy+dBy")
DefineScalarExpression("Bz","eBz+dBz")
DefineScalarExpression("Bmag","sqrt(Bx*Bx+By*By+Bz*Bz)")
DefineVectorExpression("Bfld","{Bx,By,Bz}")
DefineVectorExpression("Efld","(%e)*E"%EScl)

#Get flow velocity (ExB)
DefineVectorExpression("V",VelStr)
#Start plotting
pyv.setAtts() #Some defaults

pyv.lfmPCol(db,"dBz",vBds=(-25,25),Inv=True,pcOpac=pcOpac,Light=False)

#Field slice, equatorial
AddOperator("Slice")
sOps = GetOperatorOptions(0); 
sOps.axisType=2; sOps.project2d=0
SetOperatorOptions(sOps)

#Block out central cutout
AddPlot("Contour","RadAll")
cOps = GetPlotOptions()
cOps.contourMethod = 1
cOps.contourValue = (2.05)
cOps.legendFlag = 0

SetPlotOptions(cOps)

AddPlot("Streamline","Bfld")
#AddPlot("Streamline","V")

slOps = GetPlotOptions()

if (doCirc):
	slOps.sourceType = 3	
	slOps.radius = slRad
else:
	slOps.sourceType = 6
	slOps.useWholeBox = 0
	slOps.boxExtents = (slBoxX[0],slBoxX[1],slBoxY[0],slBoxY[1],slBoxZ[0],slBoxZ[1])
slOps.integrationDirection = 2
slOps.maxSteps = 100
slOps.sampleDensity0 = Nx1
slOps.sampleDensity1 = Nx2
slOps.sampleDensity2 = Nx3
slOps.displayMethod = 1
slOps.showSeeds = 0
slOps.randomSeed = 1
slOps.randomSamples = 1
slOps.numberOfRandomSamples = Nx1*Nx2*Nx3

#slOps.legendFlag = 0
slOps.issueStiffnessWarnings = 0
slOps.coloringMethod = 5 #Seed point ID
#slOps.coloringMethod = 2 #Vorticity
slOps.fillInterior = 1
slOps.geomDisplayQuality = 3
slOps.colorTableName = slCMap

# slOps.legendMinFlag = 1
# slOps.legendMaxFlag = 1
# slOps.legendMin = -20
# slOps.legendMax = 20

SetPlotOptions(slOps)

DrawPlots()

