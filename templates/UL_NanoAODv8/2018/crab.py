from CRABClient.UserUtilities import config
config = config()

config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'fake.py' ## fake the last step -> step4 + empty source
from glob import glob
config.JobType.inputFiles = ['scriptExe.sh', 'step1_cfg.py','step2_cfg.py','step3_cfg.py','step4_cfg.py','step5_cfg.py','step6_cfg.py','step7_cfg.py','pu.py'] + glob('fragment*py') + ['step1_71_cfg.py']
config.JobType.scriptExe='scriptExe.sh'
#config.JobType.numCores=4

config.Data.splitting = 'EventBased'
#config.Data.unitsPerJob = 500
#config.Data.totalUnits = 2000000

config.Data.unitsPerJob = DUMMY_NEVENTSPERJOB
config.Data.totalUnits = DUMMY_NEVENTSTOTAL


#config.Data.outLFNDirBase = '/store/group/cmst3/group/vhcc/hc/samples/' # % (getUsernameFromSiteDB())
config.Data.outLFNDirBase = 'DUMMY_OUTPUTDIR' # % (getUsernameFromSiteDB())
config.Data.publication = True


#config.Data.outputDatasetTag ='UL2018-NANOAODSIMv8'
#config.Data.outputDatasetTag ='UL2018-MINIAOD'

config.Data.outputDatasetTag ='DUMMY_OUTPUTTAG'

config.Site.storageSite = 'T2_CH_CERN'


#config.General.requestName = 'selvaggi-UL2018_hc_aac_3fs_v2'
#config.Data.outputPrimaryDataset = 'HPlusCharm_HGG_3FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
#config.JobType.scriptArgs=['chain=hc_aac_3fs']

config.General.requestName = 'DUMMY_REQUESTNAME'
config.Data.outputPrimaryDataset = 'DUMMY_PRIMARYDATASETNAME'


'''
do='xxx'
if do=='xxx': raise ValueError('Set do')




if do=='hc_aac_3fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_aac_3fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusCharm_HGG_3FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hc_aac_3fs']

if do=='hc_aac_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_aac_4fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusCharm_HGG_4FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hc_aac_4fs']

if do=='hb_aab_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hb_aab_4fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusBottom_HGG_4FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hb_aab_4fs']

if do=='hb_aab_5fs' :
    config.General.requestName = 'selvaggi-UL2018_hb_aab_5fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusBottom_HGG_5FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hb_aab_5fs']

if do=='hc_4lc_3fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_4lc_3fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusCharm_H4L_3FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hc_4lc_3fs']

if do=='hc_4lc_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_4lc_4fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusCharm_H4L_4FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hc_4lc_4fs']

if do=='hb_4lb_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hb_4lb_4fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusBottom_H4L_4FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hb_4lb_4fs']z

if do=='hb_4lb_5fs' :
    config.General.requestName = 'selvaggi-UL2018_hb_4lb_5fs_v2'
    config.Data.outputPrimaryDataset = 'HPlusBottom_H4L_5FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v2'
    config.JobType.scriptArgs=['chain=hb_4lb_5fs']

if do=='hc_4lc_jhu_3fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_4lc_jhu_3fs_v3'
    config.Data.outputPrimaryDataset = 'HPlusCharm_H4L_JHUGEN_3FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v3'
    config.JobType.scriptArgs=['chain=hc_4lc_jhu_3fs']

if do=='hc_4lc_jhu_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_4lc_jhu_4fs_v1'
    config.Data.outputPrimaryDataset = 'HPlusCharm_H4L_JHUGEN_4FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v1'
    config.JobType.scriptArgs=['chain=hc_4lc_jhu_4fs']

if do=='hb_4lb_jhu_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hb_4lb_jhu_4fs_v1'
    config.Data.outputPrimaryDataset = 'HPlusBottom_H4L_JHUGEN_4FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v1'
    config.JobType.scriptArgs=['chain=hb_4lb_jhu_4fs']

if do=='hb_4lb_jhu_5fs' :
    config.General.requestName = 'selvaggi-UL2018_hb_4lb_jhu_5fs_v1'
    config.Data.outputPrimaryDataset = 'HPlusBottom_H4L_JHUGEN_5FS_M125_13TeV_amcatnlo_pythia8_MINIAOD_v1'
    config.JobType.scriptArgs=['chain=hb_4lb_jhu_5fs']


if do=='hc_aac_fxfx_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_aac_fxfx_4fs_v1'
    config.Data.outputPrimaryDataset = 'HPlusCharm_HGG_4FS_M125_13TeV_amcatnloFxFx_pythia8_MINIAOD_v1'
    config.JobType.scriptArgs=['chain=hc_aac_fxfx_4fs']


if do=='hc_4lc_fxfx_jhu_4fs' :
    config.General.requestName = 'selvaggi-UL2018_hc_4lc_fxfx_jhu_4fs_v1'
    config.Data.outputPrimaryDataset = 'HPlusCharm_H4L_JHUGEN_4FS_M125_13TeV_amcatnloFxFx_pythia8_MINIAOD_v1'
    config.JobType.scriptArgs=['chain=hc_4lc_fxfx_jhu_4fs']
'''
