#  Author:  Daniel Morvay
#  Creator Email:  morvayd@gmail.com

import getpass
import platform
import ollama
import json
import subprocess
import os
import datetime

import PythonLog

strPythonScript = "Ollama Zip Move.py"
strModified = "2025.12.14"

#  Python Version
strPyVer = platform.python_version()
#  OS - Windows or Linux or Mac
strOS = platform.system()
#  OS Version 
strOSVer = platform.platform()
#  PC Name
strPC = platform.node()
#  UserID
strUser = getpass.getuser()

#  Today's Date
strStartTime = datetime.datetime.today()
strDateNow = strStartTime.strftime("%Y.%m.%d")

#
#  ---------- Python Log Start ----------
#
#  Note:  strLogPath, strLogOut are created & returned at the start of Logging
strReturn = PythonLog.PyLogStart(strPythonScript, strModified, strPyVer, strOS, strOSVer, strPC, strUser, strStartTime, strDateNow)

#  Load the Path and Filename from the function return
strLogPath = strReturn[0]
strLogOut = strReturn[1]

if (strOS=="Windows"):
    strFolder = "C:\\Users\\"+strUser+"\\.ollama\\models"

if (strOS=="Linux"):
    #  strFolder = "/usr/share/ollama/.ollama/models"
    strFolder = "/home/"+strUser+"/.ollama/models"

if (strOS=="Darwin"):
    strFolder = "/Users/"+strUser+"/.ollama/models"

#
#  ---------- Python Log Update ----------
#
strUpdate = "\n"+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+" Using Folder:"
strUpdate = strUpdate+"\n"+strFolder
PythonLog.PyLogUpdate(strUpdate, strLogOut)

#  Change to the models folder
os.chdir(strFolder)

strModels = ollama.list()

strModel = []
#  Simplify the models
for i in range(0, len(strModels['models'])):
    strModel.append(strModels['models'][i]['model'])

#
#  ---------- Python Log Update ----------
#
strUpdate = "\n"+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+" Found Ollama Models"
strUpdate = strUpdate+"\nNumber of Models Found: "+str(len(strModel))
PythonLog.PyLogUpdate(strUpdate, strLogOut)

for i in range(0, len(strModel)):

    strModelSplit = []
    strModelSplit = strModel[i].split(":")

    #  strManifest = strFolder+"\\manifests\\registry.ollama.ai\\library\\"+strModelSplit[0]+"\\"+strModelSplit[1]
    strManifest = ""

    if (strOS=="Windows"):
        strManifest = "manifests\\registry.ollama.ai\\library\\"+strModelSplit[0]+"\\"+strModelSplit[1]

    if (strOS=="Linux" or strOS=="Darwin"):
        strManifest = "manifests/registry.ollama.ai/library/"+strModelSplit[0]+"/"+strModelSplit[1]

    strFile = open(strManifest, 'r')
    strContents = strFile.read()
    #  Convert to JSON
    strContents = json.loads(strContents)

    strBlobs = []

    #  ---------- Create the Blobs File to Store ----------
    #  Load the first blob
    strFile = strContents['config']['digest']
    strTemp = strFile.split(":")
    #  strFile = strFolder+"\\blobs\\"+strTemp[0]+"-"+strTemp[1]

    if (strOS=="Windows"):
        strFile = "blobs\\"+strTemp[0]+"-"+strTemp[1]

    if (strOS=="Linux" or strOS=="Darwin"):
        strFile = "blobs/"+strTemp[0]+"-"+strTemp[1]

    strBlobs.append(strFile)

    #  Save the smaller blobs first
    for j in range(0, len(strContents['layers'])):
        strFile = ""
        strFile = strContents['layers'][j]['digest']
        strTemp = strFile.split(":")
        #  strFile = strFolder+"\\blobs\\"+strTemp[0]+"-"+strTemp[1]

        if (strOS=="Windows"):
            strFile = "blobs\\"+strTemp[0]+"-"+strTemp[1]

        if (strOS=="Linux" or strOS=="Darwin"):
            strFile = "blobs/"+strTemp[0]+"-"+strTemp[1]

        strBlobs.append(strFile)

    #  Now compress the files
    os.chdir(strFolder)

    #
    #  ---------- Python Log Update ----------
    #
    strUpdate = "\n\n---------- Compress Ollama Model ----------\n"+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+" Model: "+str(i)+" of "+str(len(strModel))
    strUpdate = strUpdate+"\nManifest: "+strManifest
    PythonLog.PyLogUpdate(strUpdate, strLogOut)

    if (strOS=="Windows"):
        subprocess.call(['C:\\R\\PortableApps\\7-ZipPortable\\App\\7-Zip64\\7z', 'a', strModelSplit[0]+"-"+strModelSplit[1]+'.7z', strManifest])

    if (strOS=="Linux"):
        subprocess.call(['7z', 'a', strModelSplit[0]+"-"+strModelSplit[1]+'.7z', strManifest])

    if (strOS=="Darwin"):
        subprocess.call(['zip', strModelSplit[0]+"-"+strModelSplit[1]+'.zip' , strManifest])

    #
    #  ---------- Python Log Update ----------
    #
    strUpdate = "\n"+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+" Adding blobs to archive.\nNumber of blobs: "+str(len(strBlobs))
    PythonLog.PyLogUpdate(strUpdate, strLogOut)

    for j in range(0, len(strBlobs)):
        
        if (strOS=="Windows"):
            subprocess.call(['C:\\R\\PortableApps\\7-ZipPortable\\App\\7-Zip64\\7z', 'a', strModelSplit[0]+"-"+strModelSplit[1]+'.7z', strBlobs[j]])

        if (strOS=="Linux"):
            subprocess.call(['7z', 'a', strModelSplit[0]+"-"+strModelSplit[1]+'.7z', strBlobs[j]])

        if (strOS=="Darwin"):
            subprocess.call(['zip', strModelSplit[0]+"-"+strModelSplit[1]+'.zip', strBlobs[j]])

if (strOS=="Windows" or strOS=="Linux"):
    #
    #  ---------- Python Log Update ----------
    #
    strUpdate = "\n"+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+"\n---------- .7z Files Saved to "+strFolder+" ----------\n"
    strUpdate = strUpdate+"\nManifest: "+strManifest
    PythonLog.PyLogUpdate(strUpdate, strLogOut)

if (strOS=="Darwin"):
    #
    #  ---------- Python Log Update ----------
    #
    strUpdate = "\n"+str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))+"\n---------- .zip Files Saved to "+strFolder+" ----------\n"
    strUpdate = strUpdate+"\nManifest: "+strManifest
    PythonLog.PyLogUpdate(strUpdate, strLogOut)

#
#  ---------- Python Log End ----------
#
strEndTime = datetime.datetime.today()
strTimeDelta = strEndTime-strStartTime
strTimeDelta = str(strTimeDelta.total_seconds())

strUpdate="\n\n-----------------------------------------------------------"
strUpdate=strUpdate+"\nPython Script End:          "+str(strEndTime)
strUpdate=strUpdate+"\n-----------------------------------------------------------"
strUpdate=strUpdate+"\nCompleted Python Script Elapsed Time: "+str(strTimeDelta)
strUpdate=strUpdate+"\n***********************************************************\n"

PythonLog.PyLogEnd(strUpdate, strLogOut)
