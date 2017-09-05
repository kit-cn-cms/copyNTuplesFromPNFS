import os
import sys
import glob
import subprocess
import json

inlogs=sys.argv[1:]

for inl in inlogs:
  #print inl
  inf=open(inl,"r")
  inlist=list(inf)
  ll=inlist[-1]
  nll=inlist[-2]
  totalFilesCopied=ll.split(" ")[-1]
  #print totalFilesCopied
  if not "crab" in nll:
    print "ERROR WITH ", inl
  crabname=nll.split(" ")[-2].split("/")[-4]
  #print crabname
  # check crab for how many jobs there were
  crabdir="/nfs/dust/cms/user/kelmorab/MEMProd/CMSSW_8_0_19/src/TTH/CommonClassifier/crab/*/"
  
  logfiles=glob.glob(crabdir+crabname+"/crab.log")
  if len(logfiles)!=1:
    print "ERROR NOT RIGHT AMOITN OF LOGFILES ", crabname
    continue
  #print logfiles
  #open crab log file
  clf=open(logfiles[0],"r")
  clfl=list(clf)
  nFromCrab=0
  for line in clfl:
    if "Jobs status" in line:
      splitline=line.split("/")[-1]
      splitline=splitline.replace(")","")
      nFromCrab=splitline
      break
  #print nFromCrab
  
  #cmd="crab status --json "+crabdir+crabname
  #try:
      #res=subprocess.check_output(cmd,shell=True)
  #except (subprocess.CalledProcessError, OSError) :
      #print "could not check crab"
  
  ##print res
  ##print "ok"
  #sres=res.split("file)")[-1].split("Log file")[0].replace("\n","")
  ##print sres
  #olist=json.loads(sres)
  ##print len(olist)
  #njobs=len(olist)
  print crabname.replace("\n",""), nFromCrab.replace("\n",""), totalFilesCopied.replace("\n",""), str(int(nFromCrab)-int(totalFilesCopied)).replace("\n","")
  ##if njobs!=int(totalFilesCopied):
    ##print "MISSING ", njobs-int(totalFilesCopied):
  
  
  