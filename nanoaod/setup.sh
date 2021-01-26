#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_18/src ] ; then 
 echo release CMSSW_10_2_18 already exists
else
scram p CMSSW CMSSW_10_2_18
fi
cd CMSSW_10_2_18/src
eval `scram runtime -sh`


scram b
cd ../../
