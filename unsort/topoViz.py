import sys
import numpy as np
import datetime
from visit import *
from visit_utils import *
from visit_utils.common import lsearch #lsearch(dir(),"blah")
import pyVisit as pyv

Pids = [1335,301,95834,12593]

RunID = 3 #Which pStub to use
pStub = ["e.100keV","H.100keV","O.100keV","e.100keV.HF"]
pLabs = ["Electron (100 keV)", "Hydrogen (100 keV)", "Oxygen (100 keV)","Electron (100 keV)"]

Base = "~/Work/magnetoloss/"
EqDir = Base + "eqSlc" #eqSlc database
pDir = Base + "synth" #Directory of h5part

Quiet = False

titS = pLabs[RunID]

#dBz 
abBz = 25; 
dBzBds = [-abBz,abBz]

#Particles
#kevBds = [50,150]
pCMap = "Cool" #ColorTableNames()
if (Quiet):
	LaunchNowin()
else:
	Launch()

#Legends
plXs = [0.03]
plYs = [0.9,0.4]
plTits = ["Residual Bz [nT]","Particle Energy [keV]"]
#Construct filenames/directory structure
#Use ActivateDatabase to swap between
#md0 = GetMetaData(dbs[0]) for info

Src0 = EqDir + "/eqSlc.*.vti database"
Src1 = pDir + "/" + pStub[RunID] + ".h5part" 
 
dbs = [Src0,Src1]

#Do some defaults
pyv.lfmExprs(doTrace=True)

#Open databases
OpenDatabase(dbs[0])
OpenDatabase(dbs[1])


#Create database correlation
CreateDatabaseCorrelation("P2Fld",dbs,0)


#Create fields/particle plots
pyv.lfmPCol(dbs[0],"dBz",vBds=dBzBds,pcOpac=0.7,Inv=True)
pyv.lfmPScat(dbs[1],v4="Trapped",vBds=[0,1],cMap=pCMap,Inv=False)

SetActivePlots( (1,2) )
pyv.cutOut()

#Gussy things up
#tit = pyv.genTit( titS=titS )
#pyv.cleanLegends(plXs,plYs,plTits)
pyv.setAtts()

#Let's see what we got
DrawPlots()

#Do time loop
#pyv.doTimeLoop(Nfin=None,T0=0.0,dt=dt,Save=True,tLabPos=(0.3,0.05) )
