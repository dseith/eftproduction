from CRABClient.UserUtilities import config, getUsername
from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration

import datetime

time = datetime.datetime.today()
timestamp = time.strftime('%d%B')

def submit(tar_ball):

    name = tar_ball.rsplit('.')[0].replace('st_tch_top_', '').replace('_slc6_amd64_gcc700_CMSSW_9_3_0_tarball', '')

    config = Configuration()

    config.section_('General')
    config.General.requestName = name
    config.General.workArea = 'crab_projects'
    config.General.transferOutputs = True
    config.General.transferLogs = True

    config.section_('JobType')
    config.JobType.pluginName = 'PrivateMC'
    config.JobType.psetName = 'TOP-RunIIFall18wmLHEGS-00060_1_cfg.py'
    config.JobType.inputFiles = [tar_ball]


    config.section_('Data')
    config.Data.outputPrimaryDataset = 'ST_t-channel_4f_elmuDecays_13TeV-amcatnloFXFX-pythia8'
    config.Data.splitting = 'EventBased'
    config.Data.unitsPerJob = 10000
    NJOBS = 400  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
    config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
    config.Data.outLFNDirBase = '/store/user/%s/' % (getUsername())
    config.Data.publication = True
    config.Data.outputDatasetTag = 'GT_stEFT_dim2_930X' + timestamp 

    config.section_('User')
    config.User.voGroup = 'dcms'

    config.section_('Site')
    config.Site.storageSite = 'T1_DE_KIT_Disk'

    crabCommand('submit', config=config)

if __name__ == '__main__':

    import sys
    submit(sys.argv[1])
