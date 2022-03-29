# EventProducer

This repository contains script that will generate and produce MINIAOD samples with setup corresponding to the UL16/UL17 and UL18 campaigns. 

The required inputs are:

- generator fragment 
- gridpack. 

Clone repository and setup CMSSW/crab:


```bash
git clone git@github.com:selvaggi/CrabEventProducer.git
cd CrabEventProducer
cmsrel CMSSW_10_6_18
cd CMSSW_10_6_18
cmsenv
cd .. 
source /cvmfs/cms.cern.ch/crab3/crab.sh

```

Create a proxy (need to query DBS for MinBias pile for pile-up mixing):

```bash
voms-proxy-init --rfc --voms cms
```


Copy the gridpack in some web directory, e.g. ```https://selvaggi.web.cern.ch/selvaggi/gridpacks/```


Create a gen fragment (see in ```fragments``` directory for examples) and insert in the ```gridpack_file``` variable the correct gridpack name.



The script options for generating events are:

```
submitCrabJob.py [-h] [--fragment FRAGMENT] [--procname PROCNAME]
                        [--tag TAG] [--gp_webdir GP_WEBDIR] [--outdir OUTDIR]
                        [--era ERA] [--njobs NJOBS] [--nev NEV] [--dry]
                        [--local] [--submit] [--status] [--resubmit]
```


For example, to test locally on 10 events:

```bash
python submitCrabJob.py --fragment fragments/fragment_ggh_jhu4l_powheg_herwig.py \
--procname GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV714_herwig7 \
--gp_webdir https://selvaggi.web.cern.ch/selvaggi/gridpacks/ \
--tag local_test \
--nev 10 \
--local
```

For proper crab submission:


```bash
python submitCrabJob.py --fragment fragments/fragment_ggh_jhu4l_powheg_herwig.py \
--procname GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV714_herwig7 \
--gp_webdir https://selvaggi.web.cern.ch/selvaggi/gridpacks/ \
--tag v1 --nev 200 --njobs 1000
--submit
```

To check status:


```bash
python submitCrabJob.py --fragment fragments/fragment_ggh_jhu4l_powheg_herwig.py \
--procname GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV714_herwig7 \
--gp_webdir https://selvaggi.web.cern.ch/selvaggi/gridpacks/ \
--tag v1 --nev 200 --njobs 1000
--status
```

To resubmit failed jobs:


```bash
python submitCrabJob.py --fragment fragments/fragment_ggh_jhu4l_powheg_herwig.py \
--procname GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV714_herwig7 \
--gp_webdir https://selvaggi.web.cern.ch/selvaggi/gridpacks/ \
--tag v1 --nev 200 --njobs 1000
--resubmit
```
