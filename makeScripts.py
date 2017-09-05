import ROOT
import os
import stat
import glob
import sys

def askYesNo(question):
  print question
  yes = set(['yes','y', 'ye', ''])
  no = set(['no','n'])
  choice = raw_input().lower()
  if choice in yes:
    return True
  elif choice in no:
    return False
  else:
    print "Please respond with 'yes' or 'no'"
    return askYesNo(question)


def create_script(cmsswpath,scriptpath,outputDir, toplevel, d, i):
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmsswpath+'src\neval `scram runtime -sh`\n'
    script+='python '+scriptpath+' '+outputDir+' '+toplevel+' '+d
    filename='scripts/'+'copyshop'+'_'+str(i)+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)
    
    
outputDir=sys.argv[1]
toplevel=sys.argv[2]
samplewildcard=sys.argv[3:]

directoriesToDo=[]
for swc in samplewildcard:
  directoriesToDo+=glob.glob(toplevel+"/"+swc)
print directoriesToDo
print "directories to copy"
for d in directoriesToDo:
  outpath=d.split("/")[-1].replace("crab_MEMKITV4_KITmemV3","").replace("crab_MEMKITV4_scalePS","").replace("crab_MEMKITV4_newTTSL","").replace("crab_MEMKITV4_OldSL","").replace("crab_MEMKITV4_Rest","").replace("crab_MEMKITV4_DL","").replace("_","")
  print d, outpath
  
if not askYesNo("ok? Do?"):
  exit(0)

scriptpath="/nfs/dust/cms/user/kelmorab/copyStuff/getFiles.py"
cmsswpath="/nfs/dust/cms/user/kelmorab/MEMProd/CMSSW_8_0_19/"

i=0   
for d in directoriesToDo:
  print d
  create_script(cmsswpath,scriptpath,outputDir, toplevel, d, i)
  i=i+1
  
  