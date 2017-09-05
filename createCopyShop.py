import os
import sys
import stat
import glob
import subprocess
import collections


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

def create_script(cmsswpath,outputDir,i, lines=[]):
    script='#!/bin/bash\n'
    script+='export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n'
    script+='source $VO_CMS_SW_DIR/cmsset_default.sh\n'
    script+='cd '+cmsswpath+'/src\neval `scram runtime -sh`\n'
    #script+='python '+scriptpath+' '+outputDir+' '+toplevel+' '+d
    for l in lines:
      script+=l+'\n'
    
    filename='scripts/'+'copyshop'+'_'+str(i)+'.sh'
    f=open(filename,'w')
    f.write(script)
    f.close()
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)



sampleNameMap={
    "WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-2500-Inf_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-800-1200_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-400-600_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-600-800_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-100-200_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-1250To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-1250-2500_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-200-400_madgraph_pythia_CUETP8M1",
    "WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Wjets-HT-70-100_madgraph_pythia_CUETP8M1",
    "DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-100-200_madgraph_pythia_CUETP8M1",
    "DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-200-400_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-400-600_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-600-800_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-800-1200_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-1200-2500_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-2500-Inf_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m50toInf-HT-70-100_madgraph_pythia_CUETP8M1",    
    
    "DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m5to50-HT-100-200_madgraph_pythia_CUETP8M1",
    "DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m5to50-HT-200-400_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m5to50-HT-400-600_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m5to50-HT-600-Inf_madgraph_pythia_CUETP8M1",    
    "DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": "Zjets_m5to50-HT-70-100_madgraph_pythia_CUETP8M1",    
    
    "WW_TuneCUETP8M1_13TeV-pythia8" : "WW_pythia_CUETP8M1",
    "WZ_TuneCUETP8M1_13TeV-pythia8" : "WZ_pythia_CUETP8M1",
    "ZZ_TuneCUETP8M1_13TeV-pythia8" : "ZZ_pythia_CUETP8M1",
    
    "ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1": "st_schan_amc_pythia_CUETP8M1",
    "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4": "st_tWchan_powheg_pythia_CUETP8M2T4",
    "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4": "stbar_tWchan_powheg_pythia_CUETP8M2T4",
    "ST_t-channel_top_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV-powhegV2-madspin": "st_tchan_powheg_pythia_CUETP8M2T4",
    "ST_t-channel_antitop_4f_inclusiveDecays_TuneCUETP8M2T4_13TeV-powhegV2-madspin": "stbar_tchan_powheg_pythia_CUETP8M2T4",
    
    "TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8": "ttW_hadr_amc_pythia_CUETP8M1",
    "TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8": "ttW_lept_amc_pythia_CUETP8M1",
    "TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8": "ttZ_lept_amc_pythia_CUETP8M1",
    "TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8" : "ttZ_hadr_amc_pythia_CUETP8M1",
    
    "SingleMuon": "OVERRIDE",
    "SingleElectron": "OVERRIDE",
    
    "ttHTobb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8": "ttHbb",
    "ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8": "ttHnonbb",
    
    "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8": "ttbar_incl",
    "TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8": "ttbar_excl_SL",
    "TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8": "ttbar_excl_DL",
    "TT_TuneCUETP8M2T4_13TeV-powheg-fsrdown-pythia8": "ttbar_fsr_down",
    "TT_TuneCUETP8M2T4_13TeV-powheg-fsrup-pythia8": "ttbar_fsr_up",
    "TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8": "ttbar_isr_down",
    "TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8": "ttbar_isr_up",
    }
    
overrideSampleMap={
        "170828_092611": "SingleMuon_Run2016B",
        "170828_092903": "SingleMuon_Run2016C",
        "170828_093152": "SingleMuon_Run2016D",
        "170828_093425": "SingleMuon_Run2016E",
        "170828_093726": "SingleMuon_Run2016F",
        "170828_094022": "SingleMuon_Run2016G",
        "170828_094321": "SingleMuon_Run2016Hv2",
        "170828_094602": "SingleMuon_Run2016Hv3",

        "170828_090327": "SingleElectron_Run2016B",
        "170828_090621": "SingleElectron_Run2016C",
        "170828_090922": "SingleElectron_Run2016D",
        "170828_091205": "SingleElectron_Run2016E",
        "170828_091449": "SingleElectron_Run2016F",
        "170828_091750": "SingleElectron_Run2016G",
        "170828_092030": "SingleElectron_Run2016Hv2",
        "170828_092329": "SingleElectron_Run2016Hv3",

        }
        
        

###################################################################

outputDir=sys.argv[1]
inputfilelist=sys.argv[2]
ncopiesperjob=sys.argv[3]
ncopiesperjob=int(ncopiesperjob)

cmsswpath=os.getenv("CMSSW_BASE")

# create top level directory
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

inflf=open(inputfilelist,"r")
fl=list(inflf)

listOfCopyLines=[]
xchecklist=[]
filecounter={}
print fl

# first loop to set things up and count files
for line in fl:
  line=line.replace("\n","")
  print "at ", line
  # get dataset name and task id
  sl=line.split("/")
  # last item is taskID
  thisTaskID=0
  if sl[-1]=="":
    thisTaskID=sl[-2]
  else:
    thisTaskID=sl[-1]
  thisDASName=""
  if sl[-1]=="":
    thisDASName=sl[-4]
  else:
    thisDASName=sl[-3]
  
  thisSampleAlias=thisDASName
  if thisDASName in sampleNameMap:
      thisSampleAlias=sampleNameMap[thisDASName]
  if thisSampleAlias=="OVERRIDE":
      if thisTaskID in overrideSampleMap:
          thisSampleAlias=overrideSampleMap[thisTaskID]
      else:
          thisSampleAlias=thisDASName+"_"+thisTaskID

  # create counter to keep track of numbering
  if thisSampleAlias not in filecounter:
    filecounter[thisSampleAlias]=0
    
  # create sample directorty
  if not os.path.exists(outputDir+"/"+thisSampleAlias):
    print "creating directory ", outputDir+"/"+thisSampleAlias
    os.makedirs(outputDir+"/"+thisSampleAlias)
  # directory already exists
  # check how many files are already there
  nfilesthere=len(glob.glob(outputDir+"/"+thisSampleAlias+"/*.root"))
  filecounter[thisSampleAlias]=nfilesthere
       
  print "1stL: ", thisSampleAlias, thisDASName, thisTaskID, nfilesthere
    
# second loop to create the scripts
for line in fl:
  line=line.replace("\n","")
  # get dataset name and task id
  sl=line.split("/")
  # last item is taskID
  thisTaskID=0
  if sl[-1]=="":
    thisTaskID=sl[-2]
  else:
    thisTaskID=sl[-1]
  thisDASName=""
  if sl[-1]=="":
    thisDASName=sl[-4]
  else:
    thisDASName=sl[-3]
  
  thisSampleAlias=thisDASName
  if thisDASName in sampleNameMap:
      thisSampleAlias=sampleNameMap[thisDASName]
  if thisSampleAlias=="OVERRIDE":
      if thisTaskID in overrideSampleMap:
          thisSampleAlias=overrideSampleMap[thisTaskID]
      else:
          thisSampleAlias=thisDASName+"_"+thisTaskID
  
  print "2ndL: ", thisSampleAlias, thisDASName, thisTaskID 
  # find files to copy
  tocpy=glob.glob(line+"*/*.root")
  #print tocpy
  
  outbase=outputDir+"/"+thisSampleAlias+"/"
  for tc in tocpy:
    # increment counter
    filecounter[thisSampleAlias]=filecounter[thisSampleAlias]+1
    thisnumber=filecounter[thisSampleAlias]
    
    oname=tc.rsplit("/",1)[1]
    son=oname.split("_")
    newname=thisSampleAlias+"_"+str(thisnumber)+"_"+son[1]+"_Tree.root"
    outfilename=outbase+newname
    # write to list of copy commands
    listOfCopyLines.append("cp "+tc+" "+outfilename)
    xchecklist.append(outfilename)

maxOcc, numMaxOcc = collections.Counter(xchecklist).most_common(1)[0]
if not numMaxOcc == 1:
  print maxOcc, numMaxOcc
  exit(1)


logfile=open("completeListOfCopyCommands.txt","w")
for loc in listOfCopyLines:
  logfile.write(loc+"\n")
logfile.close()

jobcounter=0
copycounter=0
templist=[]
fulllist=[]
theCounter=0
for loc in listOfCopyLines:
  templist.append(loc)
  copycounter+=1
  theCounter+=1
  if theCounter%ncopiesperjob==0 or theCounter==len(listOfCopyLines): 
    print copycounter, jobcounter
    create_script(cmsswpath,outputDir,jobcounter,templist)
    jobcounter+=1
    copycounter=0
    fulllist+=templist
    templist=[]
  
if fulllist!=listOfCopyLines:
  print "PROBLEM"




