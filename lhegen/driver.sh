seed=10

cmsDriver.py $1 --fileout $2 --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN,SIM --geometry DB:Extended --era Run2_2018 --python_filename $3  --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring  -n 132  --nThreads 8

echo "from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper" >> $3
echo "randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)" >> $3
echo "randSvc.populate()" >> $3
