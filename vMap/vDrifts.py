import sys
import os
import numpy as np
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv

#RootDir = os.path.expanduser('~') + "/Work/Injection/VTIs/"
#fldSlc = RootDir + "/SNS-Bz-5-Vx400-N5-F200_mhd_1141000.vti"
fldSlc = "mhd.vti"
Quiet = True
doPic = True

# fldSlc = "testSlc.vti"
# Quiet = False
# doPic = False

zSlc = 0.0

if (Quiet):
	LaunchNowin()
else:
	Launch()

OpenDatabase(fldSlc)

#Do some defaults
pyv.lfmExprsEB()
pyv.setAtts()

md0 = GetMetaData(fldSlc)

#ExB velocity (in km/s)
#DefineScalarExpression("Veb","1000*Emag/Bmag")
DefineVectorExpression("BfldC","{Bx,By,Bz}")
DefineScalarExpression("RadC","recenter(cylindrical_radius(mesh))")
DefineScalarExpression("Veb","if ( ge(Bmag,1.0e-6), 1000*Emag/Bmag, 0)")
#BxGrad (in 1/Re, convert to 1/km)
DefineScalarExpression("BmagC","recenter(Bmag)")
DefineVectorExpression("GBVec","gradient(BmagC)")
DefineScalarExpression("GBx","GBVec[0]")
DefineScalarExpression("GBy","GBVec[1]")
DefineScalarExpression("GBz","GBVec[2]")

DefineScalarExpression("BxGB","magnitude(cross(recenter(BfldC),GBVec))/(BmagC*BmagC*6380.0)")

#Non-energy part of Vd
q = 1.6021766e-19 #Coulombs
#Will calculate drift velocity (m/s per Joule, want km/s per kev)
Scl = (1.0e+6)/( q*6.242e+15*1.0e+3)
#Drift velocity (km/s per Joule)
DefineScalarExpression("VDpN","1.0e+6*BxGB/(%f*BmagC)"%(q))
DefineScalarExpression("VdPkev","%f*BxGB/BmagC"%(Scl))

#Equality energy (in kev), 2/3 from assuming alpha=45o
DefineScalarExpression("eqKevA","(2/3.0)*Veb/VdPkev")
DefineScalarExpression("eqKev","if( ge(RadC,2.0), eqKevA,0.0)")
DefineScalarExpression("eqKevC","recenter(eqKev)")
cMap="viridis"
cMap = "RdYlBu"
Kbd = [1,500]

#Create slice of eqKev
if (doPic):
	pyv.lfmPCol(fldSlc,"eqKevC",cMap=cMap,vBds=Kbd,Log=True)
	pcOp = GetPlotOptions()
	pcOp.centering = 2
	SetPlotOptions(pcOp)

	AddOperator("Slice",0)
	slOp = GetOperatorOptions(0)
	slOp.axisType = 2
	slOp.originIntercept = zSlc
	SetOperatorOptions(slOp,0)
	
	AddOperator("Threshold",1)
	tOp = GetOperatorOptions(1)
	tOp.listedVarNames = ("RadAll")
	tOp.lowerBounds = (2)
	SetOperatorOptions(tOp,1)
	
	pyv.cleanLegends([0.025],[0.9],["Particle Energy (keV)\nDrift/ExB Equality"])
	DrawPlots()
	pyv.SetWin2D([-15,12,-20,20])
	SaveWindow()
else:
	OpenGUI()
