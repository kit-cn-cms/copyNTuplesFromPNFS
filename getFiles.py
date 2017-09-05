import os
import sys
import glob
import subprocess

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

outputDir=sys.argv[1]
toplevel=sys.argv[2]
samplewildcard=sys.argv[3]
directoriesToDo=samplewildcard
#for swc in samplewildcard:
  #directoriesToDo+=swc
directoriesToDo=[samplewildcard]
print directoriesToDo
print "directories to copy"
for d in directoriesToDo:
  outpath=d.split("/")[-1].replace("crab_MEMKITV4_KITmemV3","").replace("crab_MEMKITV4_scalePS","").replace("crab_MEMKITV4_newTTSL","").replace("crab_MEMKITV4_OldSL","").replace("crab_MEMKITV4_Rest","").replace("crab_MEMKITV4_DL","").replace("_","")
  print d, outpath


#if not askYesNo("ok? Do?"):
  #exit(0)

for d in directoriesToDo:
  print "doing ", d
  outpath=outputDir+"/"+ d.split("/")[-1].replace("crab_MEMKITV4_KITmemV3","").replace("crab_MEMKITV4_scalePS","").replace("crab_MEMKITV4_newTTSL","").replace("crab_MEMKITV4_OldSL","").replace("crab_MEMKITV4_Rest","").replace("crab_MEMKITV4_DL","").replace("_","")
  if not os.path.exists(outpath):
    os.makedirs(outpath)
  files=glob.glob(d+"/*/*/*.root")
  nfiles=len(files)
  for num, f in enumerate(files):
    print num , " of ", nfiles, f
    #print f
    cmd="cp -v "+f+" "+outpath+"/"+f.split("/")[-1]
    print cmd
    subprocess.call(cmd,shell=True)
  #exit(0)
  
  
  print "total files copied ", num , nfiles 
  
  
  
  
  
  
  