cmsDriver.py step1 --filein $1 --fileout $2 --mc --eventcontent NANOEDMAODSIM --datatier NANOAODSIM --conditions 102X_upgrade2018_realistic_v20 --step NANO --nThreads 4 --era Run2_2018,run2_nanoAOD_102Xv1 --python_filename $3 --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 

sed -i s/PoolOutputModule/NanoAODOutputModule/g $3

