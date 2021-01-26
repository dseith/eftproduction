#!/bin/bash
THISPATH=pwd

export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_3/src ] ; then 
 echo release CMSSW_10_2_3 already exists
else
scram p CMSSW CMSSW_10_2_3
fi
cd CMSSW_10_2_3/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TOP-RunIIFall18wmLHEGS-00060 --retry 2 --create-dirs -o Configuration/GenProduction/python/TOP-RunIIFall18wmLHEGS-00060-fragment.py 
[ -s Configuration/GenProduction/python/TOP-RunIIFall18wmLHEGS-00060-fragment.py ] || exit $?;

scram b
cd ../../


cp $THISPATH/crab.py $CMSSW_BASE/src
cp $THISPATH/driver*.sh $CMSSW_BASE/src
cp $THISPATH/submit.sh $CMSSW_BASE/src
