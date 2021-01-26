from CRABClient.UserUtilities import config
from WMCore.Configuration import Configuration
from CRABAPI.RawCommand import crabCommand

import datetime

time = datetime.datetime.today()
timestamp = time.strftime('%d%B')


def submit(name, inputDataSet):
    config = Configuration()
    config.section_('General')
    config.General.requestName = 'MC_MiniAOD_singletop_' + name
    config.General.workArea = 'crab_projects'
    config.General.transferOutputs = True
    config.General.transferLogs = True 


    config.section_('JobType')
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = 'TOP_MiniAOD_cfg.py'

    config.section_('Data')
    config.Data.inputDataset = inputDataSet

    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 1
    # config.Data.splitting = 'Automatic'
    # config.Data.unitsPerJob = 10
    config.Data.outLFNDirBase = '/store/user/dseith/'
    config.Data.outputDatasetTag = 'GT_priv_tuneMiniAOD_' + timestamp
    config.Data.publication = True
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
