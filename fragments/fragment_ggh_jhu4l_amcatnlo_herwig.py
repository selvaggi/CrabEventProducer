import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Herwig7Settings.Herwig7CH3TuneSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7StableParticlesForDetector_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7MGMergingSettings_cfi import *


generator = cms.EDFilter("Herwig7GeneratorFilter",
    herwig7CH3SettingsBlock,
    herwig7StableParticlesForDetectorBlock,
    herwig7MGMergingSettingsBlock,
    configFiles = cms.vstring(),
    hw_user_settings = cms.vstring(
        'set FxFxHandler:MergeMode FxFx',
        'set FxFxHandler:njetsmax 2'
    ),
    parameterSets = cms.vstring(
        'herwig7CH3PDF',
        'herwig7CH3AlphaS',
        'herwig7CH3MPISettings',
        'herwig7StableParticlesForDetector',
        'hw_mg_merging_settings',
        'hw_user_settings'
        ),
    crossSection = cms.untracked.double(-1),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest'),
    runModeList = cms.untracked.string("read,run"),
    seed = cms.untracked.int32(12345)
)

gridpack_file='ggh012j_5f_NLO_FXFX_125_JHUGenV714_HZZ4l_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'

import os
externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    nEvents = cms.untracked.uint32(9999),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    numberOfParameters = cms.uint32(1),
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/DoublyChargedHiggsGMmodel_HWW_M2000/v1/DoublyChargedHiggsGMmodel_HWW_M2000_tarball.tar.xz'),
    args = cms.vstring(os.environ['PWD']+'/'+gridpack_file),
)
