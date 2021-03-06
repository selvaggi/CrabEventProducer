#!/bin/bash

echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log


curl --insecure DUMMY_WEBDIR/DUMMY_GRIDPACK  --retry 2 -o ./DUMMY_GRIDPACK  
ls -ltrh 


source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc7_amd64_gcc700

BASE=$PWD

### to run old herwig configuration 
MYCMSSW=CMSSW_9_3_15_patch1
MYCMSSW=CMSSW_10_6_18
#MYCMSSW=CMSSW_10_6_30_patch1


echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 1 ====================" | tee -a job.log
cmsRun -j step1.log step1_cfg.py jobNum=$1


export SCRAM_ARCH=slc7_amd64_gcc700
MYCMSSW=CMSSW_10_6_17_patch1
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 2 ====================" | tee -a job.log
cmsRun -j step2.log step2_cfg.py

CLEAN=step1.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_6_17_patch1
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 3 ====================" | tee -a job.log
cmsRun -j step3.log step3_cfg.py

CLEAN=step2.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_2_16_UL
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 4 ====================" | tee -a job.log
cmsRun -j step4.log step4_cfg.py

ls -lrth

CLEAN=step3.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_6_17_patch1
#MYCMSSW=CMSSW_10_2_16_UL

    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

export HOME=${BASE}

echo "================= CMSRUN starting Step 5 ====================" | tee -a job.log
export DISPLAY=localhost.0.0
cmsRun -j step5.log step5_cfg.py

CLEAN=step4.root
    echo "--> cleaning up $CLEAN"
    rm -v $CLEAN

MYCMSSW=CMSSW_10_6_20

    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE


echo "================= CMSRUN starting Step 6 ====================" | tee -a job.log
#cmsRun -e -j FrameworkJobReport.xml step6_cfg.py
#cmsRun -j step6.log step6_cfg.py
cmsRun  -j FrameworkJobReport.xml step6_cfg.py

MYCMSSW=CMSSW_10_6_19_patch2
    echo "================= CMSRUN setting up $MYCMSSW ===================="| tee -a job.log
    if [ -r $MYCMSSW/src ] ; then 
     echo release $MYCMSSW already exists
    else
     scram p CMSSW $MYCMSSW
    fi
    cd $MYCMSSW/src
    eval `scram runtime -sh`
    scram b 
    cd $BASE

echo "================= CMSRUN starting Step 7 ====================" | tee -a job.log
#cmsRun -e -j FrameworkJobReport.xml step7_cfg.py

echo "================= CMSRUN finished ====================" | tee -a job.log
