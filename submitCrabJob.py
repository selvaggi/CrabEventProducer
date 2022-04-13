#!/usr/bin/env python
import os, sys, subprocess
import argparse
import commands
import time
import random
import importlib

# /eos/cms/store/cmst3/group/vhcc/hc/samples/
# /store/group/cmst3/group/vhcc/hc/samples/


#__________________________________________________________
def replace_in_file(string_in, string_out, f):

    ftmp = f+'.tmp'
    with open(f, "rt") as fin:
        with open(ftmp, "wt") as fout:
            for line in fin:
                fout.write(line.replace(string_in, string_out))
    os.system('mv {} {}'.format(ftmp, f))

#_____________________________________________________________________________________________________________
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument ('--fragment', help='MC fragment',  default='fragments/fragment_hc_4lc_fxfx_jhu_4fs.py')
    parser.add_argument ('--procname', help='process name', default='HPlusCharm_H4L_JHUGEN_4FS_M125_13TeV_amcatnloFxFx_pythia8_MINIAOD')
    parser.add_argument ('--tag', help='process tag', default='v1')
    parser.add_argument ('--gp_webdir', help='gridpack webdir', default='https://selvaggi.web.cern.ch/selvaggi/gridpacks/')
    parser.add_argument ('--outdir', help='output directory e.g. ', default='/store/group/cmst3/group/vhcc/hc/samples/')
    parser.add_argument ('--era', help='2016/2017/2018', default='2018')
    parser.add_argument ('--njobs', help='number of jobs ', type=int, default=10)
    parser.add_argument ('--nev', help='number of events per job', type=int, default=10)
    parser.add_argument ('--dry', help='', dest="dry", default=False, action='store_true')
    parser.add_argument ('--local', help='', dest="local", default=False, action='store_true')
    parser.add_argument ('--submit', help='', dest="submit", default=False, action='store_true')
    parser.add_argument ('--status', help='', dest="status", default=False, action='store_true')
    parser.add_argument ('--resubmit', help='', dest="resubmit", default=False, action='store_true')


    args = parser.parse_args()

    fragment      = os.path.abspath(args.fragment)
    procname      = args.procname
    tag           = args.tag
    era           = args.era
    gp_webdir     = args.gp_webdir
    outdir        = args.outdir

    #if era != 'UL16' and era != 'UL17' and era != 'UL18':
    if era != '2016' and era != '2017' and era != '2018':
        print 'provide 2016/2017/2018 era option. '
        #print 'provide 2018 era option. '
        sys.exit()


    # create job dir 

    job_name = '{}_{}_{}'.format(procname, era, tag)
    job_dirname = 'job_{}'.format(job_name)
    job_dir = 'jobs/{}/'.format(job_dirname)
    
    if args.submit or args.local:
 
        if os.path.exists(job_dir):
            print 'directory:', job_dir, 'exists ...'
            print 'Choose a different job name and re-submit.'
            exit(1)

        os.system('mkdir -p {}'.format(job_dir))
    
        # copy needed config files to job dir
        template_dir = 'templates/UL_NanoAODv8/{}'.format(era)
        os.system('cp {}/* {}'.format(template_dir, job_dir))

        fragment_file = '{}/fragment.py'.format(job_dir)

        os.system('cp {} {}'.format(fragment, fragment_file))

        os.system('touch jobs/__init__.py')
        os.system('touch {}/__init__.py'.format(job_dir))

        # make necessary changes to config files


        module_name = 'jobs.{}.fragment'.format(job_dirname)
        new_module = importlib.import_module(module_name)
        gridpack_filename = new_module.gridpack_file

        njobs = '{}'.format(args.njobs)
        nevents_per_job = '{}'.format(args.nev)
        nevents_total = '{}'.format(int(njobs) * int(nevents_per_job))
        output_dir = outdir
        output_tag = 'UL{}_{}'.format(era,tag)
        request_name = '{}_{}'.format(procname,output_tag)
        primary_dataset_name = procname
        gridpack_webdir = gp_webdir

        # somehow, max 100 characters allowed for request name 
        request_name = request_name[:100]

        ## loop over config files 
        for filename in os.listdir(job_dir):
            f = os.path.join(job_dir, filename)
            replace_in_file('DUMMY_GRIDPACK', gridpack_filename, f)
            replace_in_file('DUMMY_NEVENTSPERJOB', nevents_per_job,f)
            replace_in_file('9999', nevents_per_job,f)
            replace_in_file('DUMMY_NEVENTSTOTAL', nevents_total,f)
            replace_in_file('DUMMY_OUTPUTDIR', output_dir,f)
            replace_in_file('DUMMY_OUTPUTTAG', output_tag,f)
            replace_in_file('DUMMY_REQUESTNAME', request_name,f)
            replace_in_file('DUMMY_PRIMARYDATASETNAME', primary_dataset_name,f)
            replace_in_file('DUMMY_WEBDIR', gridpack_webdir,f)

        # 
        os.chdir(job_dir)
        if not args.dry:
            if args.submit:
                os.system('crab submit crab.py')
            if args.local:
                os.system('ls -lrth')
                os.system('source ./scriptExe.sh 1')                

       
    elif args.status:
        os.chdir(job_dir)
        cmd = 'crab status -d crab_privateMCProduction/crab_{}_UL{}_{}'.format(procname, era, tag)
        print cmd
        if not args.dry:
            os.system(cmd)


    elif args.resubmit:
        os.chdir(job_dir)
        cmd = 'crab resubmit crab_privateMCProduction/crab_{}_UL{}_{}'.format(procname, era, tag)
        print cmd
        if not args.dry:
            os.system(cmd)



#_______________________________________________________________________________________
if __name__ == "__main__":
    main()
