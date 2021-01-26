# Generate Samples

To generate samples there are multiple Steps necessary: 

 1. LHE + Gen (often done together)
 2. Premix
 3. AOD
 4. MiniAOD
 5. NanoAOD

There is a directory for each step. Each directory has the following files:

 1. setup.sh
 2. driver.sh
 3. crab.py
 
The setup.sh file contains the code to setup the CMSSW environment and copy necessary files.
The driver.sh file is for creating the _cfg.py config file which is executed with cmsRun to generate the samples.
crab.py is for job submission on the grid.

Those files are mostly for illustration to generate samples one needs to look up the exact setup and driver commands on MCM.
In the crab file one needs to change the name of the datasets, storage location, output directory, ...
Also if one published the data one needs to check the name of the output dataset and use it as input for the next step.

Here are some notes on the individual steps:

## LHE + Gen
In the setup step a configuration file is downloaded. Which is in the example:
*Configuration/GenProduction/python/TOP-RunIIFall18wmLHEGS-00060-fragment.py*
In this configuration one needs to replace in the *ExternalLHEProducer* the tarball with ones own tarball. 
The tarball should be copied to *$CMSSW_BASE/src*
And then it should be included in the configuration file like this:  
``
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",  
    args = cms.vstring('../tarball.tar.xz'),  
    ...
 ``  
 Note the ``../``.

## Premix

Here one needs to check which Neutrino Gun dataset to use.
It is normally best to create a list of all files in the dataset for example with:
``
dasgoclient --query="file dataset=/Name/Of/DAS/Dataset"
``
And then add this text file in the driver command with ``filelist:``.

## AOD + MiniAOD
nothing special here

## NanoAOD
If one wants to have the EFT Weights in the NanoAOD file one needs to write a producer which creates the necessary table(s).
The easiest thing is to use the already available GenWeightsTableProducer:
https://github.com/cms-sw/cmssw/blob/master/PhysicsTools/NanoAOD/plugins/GenWeightsTableProducer.cc
and modify it.
Like here:
https://github.com/dseith/cmssw/blob/eft_weights/PhysicsTools/NanoAOD/plugins/GenWeightsTableProducer.cc

This reads the EFTWeights from the LHE information in the sample.
In this code the names of the EFT Weights are hard coded and therefore need to be changed if one uses different weights.

The driver.sh file in the nanoaod directory also contains a line to replace the 
*PoolOutputModule* with the *NanoAODOutputModule*, which is somehow not done automatically by the cmsDriver command but needs to be done in order to use the samples afterwards.
