from CRABClient.UserUtilities import config, getUsername
from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration

import datetime

time = datetime.datetime.today()
timestamp = time.strftime('%d%B')

def submit(config_name, tar_ball, name, dataset_name):

    config = Configuration()

    config.section_('General')
    config.General.requestName = name
    config.General.workArea = 'crab_projects'
    config.General.transferOutputs = True
    config.General.transferLogs = True

    config.section_('JobType')
    config.JobType.pluginName = 'PrivateMC'
    config.JobType.psetName = config_name 
    config.JobType.inputFiles = [tar_ball]


    config.section_('Data')
    # config.Data.outputPrimaryDataset = 'ST_t-channel_4f_elmuDecays_13TeV-amcatnloFXFX-pythia8'
    # config.Data.outputPrimaryDataset = 'TT_NoFullyHadronic_13TeV-amcatnloFXFX-pythia8'
    config.Data.outputPrimaryDataset  = dataset_name
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 5000
    NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
    config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
    config.Data.outLFNDirBase = '/store/user/%s/' % (getUsername())
    config.Data.publication = True
    config.Data.outputDatasetTag = 'GT_stEFT_dim2_930X' + timestamp 
    config.JobType.maxMemoryMB = 9000
    config.JobType.numCores = 8



    config.section_('User')
    config.User.voGroup = 'dcms'

    config.section_('Site')
    config.Site.storageSite = 'T1_DE_KIT_Disk'

    crabCommand('submit', config=config)

if __name__ == '__main__':

    import sys
    args = sys.argv[1:]
    submit(*args)
