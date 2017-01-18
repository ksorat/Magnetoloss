#Given phi/radial range, marks the point to setup injection

import numpy as np
import os
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import lfmGrids as lfm
import pyVisit as pyv

Quiet = True
T0 = 3750

#Order sinj,minj,xlinj

Phi0s = [110]
Phi1s = [112.5]
R0s = [19.25]
R1s = [20.25]
Cols = [(0, 255, 255, 255),(0,0,255,255),(255,0,255,255)]
#EqSlc DB
EqDir = os.path.expanduser('~') + "/Work/Magnetoloss/rewe"
Src0 = EqDir + "/eqSlc.*.vti database"
Src0 = EqDir + "/eqSlc.0200.vti"
Nw0 = 0
Nw = len(Phi0s)

#dBz
abBz = 25;
dBzBds = [-abBz,abBz]

if (Quiet):
	LaunchNowin()
else:
	Launch()

#Do some defaults
pyv.lfmExprs()
pyv.setAtts()

#Open databases
OpenDatabase(Src0)
md0 = GetMetaData(Src0)

#Get time
Time = np.array(md0.times)
Nt = np.argmax(Time>=T0)



DefineScalarExpression("PCut","Phi*RCut0*RCut1")
DefineScalarExpression("RCut","Rcyl*PCut0*PCut1")

#Draw field marker
pyv.lfmPCol(Src0,"dBz",vBds=dBzBds,pcOpac=0.7,Inv=True)

#Draw wedges

for n in range(Nw0,Nw):
	DefineScalarExpression("RCut0_%d"%(n),"if( ge(Rcyl, %f), 1, 0)"%(R0s[n])) 
	DefineScalarExpression("RCut1_%d"%(n),"if( le(Rcyl, %f), 1, 0)"%(R1s[n])) 
	DefineScalarExpression("PCut0_%d"%(n),"if( ge(Phi, %f), 1, 0)"%(Phi0s[n])) 
	DefineScalarExpression("PCut1_%d"%(n),"if( le(Phi, %f), 1, 0)"%(Phi1s[n])) 
	DefineScalarExpression("Wedge_%d"%(n),"RCut0_%d*RCut1_%d*PCut0_%d*PCut1_%d"%(n,n,n,n))

	AddPlot("Contour","Wedge_%d"%(n))
	cOp = GetPlotOptions()
	cOp.contourMethod = 1
	#cOp.contourValue = tuple([Phi0,Phi1])
	cOp.contourValue = 1
	cOp.colorType = 0
	cOp.singleColor = Cols[n]
	cOp.legendFlag=0
	cOp.lineWidth=2
	
	SetPlotOptions(cOp)

SetTimeSliderState(Nt)
DrawPlots()
SaveWindow()