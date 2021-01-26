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
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = 'TOP-RunIIFall18wmGS-00060_1_cfg.py'


    config.section_('Data')
    config.Data.inputDataset = "/ST_t-channel_4f_elmuDecays_13TeV-amcatnloFXFX-pythia8/dseith-GT_stEFT_dim2_930X11July-1109e3973be8fcd89b87655c5e215dad/USER"

    config.Data.inputDBS = 'phys03'
    config.Data.splitting = 'Automatic'
    config.Data.outLFNDirBase = '/store/user/%s/' % (getUsername())
    config.Data.publication = True
    config.Data.outputDatasetTag = 'GT_stEFT_dim2_930X_GEN' + timestamp 
    config.JobType.maxMemoryMB = 5000
    config.JobType.numCores = 4

    config.section_('User')
    config.User.voGroup = 'dcms'

    config.section_('Site')
    config.Site.storageSite = 'T1_DE_KIT_Disk'

    crabCommand('submit', config=config)

if __name__ == '__main__':

    import sys
    submit(sys.argv[1])
