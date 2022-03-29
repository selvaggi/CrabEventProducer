import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Herwig7Settings.Herwig7LHECommonSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7StableParticlesForDetector_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7CH3TuneSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7LHEPowhegSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7PSWeightsSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7_7p1SettingsFor7p2_cfi import *

generator = cms.EDFilter("Herwig7GeneratorFilter",
    herwig7LHECommonSettingsBlock,
    herwig7LHEPowhegSettingsBlock,
    herwig7StableParticlesForDetectorBlock,
    herwig7PSWeightsSettingsBlock,
    herwig7CH3SettingsBlock,
    herwig7p1SettingsFor7p2Block,
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(1.0),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),    
    hw_user_settings = cms.vstring(
        'cd /Herwig/EventHandlers',
        'create Herwig::BranchingRatioReweighter /Herwig/Generators/BRReweighter',
        'insert /Herwig/Generators/EventGenerator:EventHandler:PostHadronizationHandlers 0 /Herwig/Generators/BRReweighter',
        'cd /',
    ),     
    parameterSets = cms.vstring(
        'hw_lhe_common_settings',
        'hw_lhe_powheg_settings',
        'herwig7CH3PDF', 
        'herwig7CH3AlphaS', 
        'herwig7CH3MPISettings', 
        'herwig7StableParticlesForDetector',
        'hw_PSWeights_settings',
        'hw_user_settings',
        'hw_7p1SettingsFor7p2',
    ),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest'),
    runModeList = cms.untracked.string('read,run'),
)

gridpack_file='gg_H_quark-mass-effects_NNPDF31_13TeV_M125_JHUGenV714_HZZ4l.tgz'


import os
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(9999),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/DoublyChargedHiggsGMmodel_HWW_M2000/v1/DoublyChargedHiggsGMmodel_HWW_M2000_tarball.tar.xz'),
    args = cms.vstring(os.environ['PWD']+'/'+gridpack_file),
)
