# *********************************************************************
# 
#                           Renamer
#
#**********************************************************************
#
#  Autor:    schaerphix
#  Date:     05.12.2022
#  Revision: V1.1
#
#  LICENSE:  GNU General Public License v3.0  
#
#  Renamer.py
#    
#  
# Description
# ===========
# The Renamer is a GUI applikation that can rename n numbers of 
# of files or folders
#  

#   ********************************************************************
#                           Import
#   ********************************************************************

from FileFunction import Rename
from GUI_Renamer import*
from GUIdef_Renamer import*
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import shutil
from os import path
from datetime import*

    
#   ********************************************************************
#                           Classes
#   ********************************************************************


class Variablen :
    """
    erstellt die Klasse für Variable
    """
    
    def __init__(self):
        """
        siz =  Window Size        
        """
        self.value = ""

    def WriteVariable(self,val):
        self.value = val
        
    def GetVariable(self):
        return self.value
        

                   

#   ********************************************************************
#                           Functions
#   ********************************************************************

def GetFiles (firstPath,filesSelect,noOfFiles):
    try:
        filesSelect.WriteVariable(fd.askopenfilenames(title="Files öffnen"))
        noOfFiles.WriteVariable(len(filesSelect.GetVariable()))
        firstPath.WriteVariable(filesSelect.GetVariable()[0])
        status = "done"
    except IndexError:
        firstPath.WriteVariable("No file selected")
        status = "No file selected"
    return status
    
def GetFileName(filePath,newBodyName):
    if newBodyName == 1: 
        name = filePath.split('/')
        name = name[len(name)-1]
        name = name.split('.')
    if newBodyName == 2:
        name = filePath.split('/')
        name = name[len(name)-1]
        name = name.split('.')
        name[0] = newName.get()
    return name

def GetFileNameOrig(filePath,i):
    name = filePath[i].split('/')
    name = name[len(name)-1] 
    return name

def GetFolder(filePath,i):
    folder = filePath[i].split('/')
    folderPath =""
    a = 0
    while a < (len(folder)-1) :
        folderPath = folderPath + folder [a] + "/"
        a += 1
    return folderPath
    
    
    
    
def GetFilePath(filePath,folderPath):
    if not (filePath == "No file selected"):
        name = filePath.split('/')
        tempName=""
        i = 0
        while i < len(name) -1:
            tempName = tempName + name[i] + "/"
            i= i+1
    else:
        tempName = ""
    folderPath.WriteVariable(tempName)

    
def CreatNewNames(var,i):
    dif = GetDifference(var,i)
    path = var[0].GetVariable()
    name = GetFileName(path[i],var[4].GetVariable())
    option = GetOption(var)
    if var[8].GetVariable() == 1:                                       
        nameOut = dif + option + name[0] + "." + name[1]                                                  
    elif var[8].GetVariable() == 2:                                     
        nameOut = name[0] + option + dif + "." + name[1]                                                   
    else:
        nameOut = name
    return nameOut

    

def GetDifference(var,i):
    diff = ""
    if var[6].GetVariable() == 1:
        diff = DateNow()
    elif var[6].GetVariable() == 2:
        diff = str(i)
    elif var[6].GetVariable() == 3:
        diff = var[7].GetVariable()
    else:
        diff = diff = str(i)
    return diff
        
def GetOption(var):
    opt = ""
    if var[9].GetVariable() == 1:
        opt = "_"
    elif var[9].GetVariable() == 2:
        opt= "-"
    elif var[9].GetVariable() ==3:
        opt = var[10].GetVariable()
    else:
        opt=""
    return opt
    
    
def GetAll(entryRad,var,allVar):
    i = 0
    for n in var:
        n.WriteVariable(entryRad[i].get())
        step = 1510 + i
        i = i + 1
    allVar[11].WriteVariable(DateNow())

def DateNow():
    datTime = datetime.now()
    datTime = datTime.strftime("%Y%m%d")
    return datTime    
     

def CheckPosible(var):
    status = 0
    if var[2].GetVariable() == 0:
        messagebox.showwarning("Warning", "There is no File to Rename selected. Please Select minimum one file")
        status = 3
    else:
        if var[4].GetVariable() == 2 and var[6].GetVariable() == 1:                                     
            status = 1
            messagebox.showwarning("Warning", "The Difference option can not be set to 'Date' if the New Name option is set to 'New Name'.\n \nPlease change one oft those settings")
        if var[4].GetVariable() == 2 and var[6].GetVariable() == 3:                                     
            status = 1
            messagebox.showwarning("Warning", "The Difference option can not be set to 'Customize' if the New Name option is set to 'New Name'.\n \nPlease change one oft those settings")
        if var[4].GetVariable() == 2 and var[5].GetVariable() == "":                                     
            status = 2
            messagebox.showwarning("Warning", "The New Name option is set to 'New Name' but there is no new name definied in the Entry fild.\n \nPlease define a name or change the New Name option")
        if var[6].GetVariable() == 3 and var[7].GetVariable() == "":                                     
            status = 2
            messagebox.showwarning("Warning", "The Difference option is set to 'Customize' but there is no new name definied in the Entry fild.\n \nPlease define a difference or change the Differnce option")
    return status

def Rename(pfad,fileName,newName):                                    
    if path.exists(pfad + fileName):                                                                   
        os.rename(pfad + fileName, pfad + newName)                                                               
        status = 0
        statusText = "Rename in new name %s done"%(newName)             
    else:                              
        status = 1
        statusText = "Error:    File or Path not found"                  
    return status,statusText


#   ********************************************************************
#                           MAIN
#   ********************************************************************



def main():

#                           Variable definition
#   -------------------------------------------------------------------- 
    
    inputPath = Variablen()
    inputPath.WriteVariable("") 
    
    firstFilePath = Variablen()
    firstFilePath.WriteVariable("No file selected")
    
    nOfFiles = Variablen()
    nOfFiles.WriteVariable(0)
    
    filePathFolder = Variablen()
    filePathFolder.WriteVariable("")
    
    toNewName = Variablen()
    toNewNameEntry = Variablen()
    differenceOption = Variablen()
    differenceOptionEntry = Variablen()
    positionOption = Variablen()
    separationOption = Variablen()
    separationOptionEntry = Variablen()
    
    dateActual = Variablen()
    dateActual.WriteVariable("") 
    
     

#                           Button Functions
#   --------------------------------------------------------------------    
    
    def InPathSelect():
        inPath = GetFiles(firstFilePath,inputPath,nOfFiles)
        inPathString["text"] = firstFilePath.GetVariable()
        numberOfFiles["text"] = nOfFiles.GetVariable()
        GetFilePath(firstFilePath.GetVariable(),filePathFolder)
        
    
    def PreviewUpdat(): 
        GetAll(entryRadio,varEntryRadio,allVar)
        status = 0                                                      
        status = CheckPosible(allVar)
        
        name = CreatNewNames(allVar,0)
        textBody["text"] = name

    def RenameStart():
        GetAll(entryRadio,varEntryRadio,allVar)
        status = 0                                                      
        status = CheckPosible(allVar)
        if status == 0:
            i=0
            path = allVar[0].GetVariable()
            for n in path:
                path = GetFolder(allVar[0].GetVariable(),i)
                nameOrig = GetFileNameOrig(allVar[0].GetVariable(),i)
                name = CreatNewNames(allVar,i)
                stat = Rename(path,nameOrig,name)
                i +=1

        
    def Info():
        global infoWindow 
        infoWindow = CreatWin2("Info")
        
        # Creat Title
        CreatLabelHe(infoWindow,"About Renamer",5,10)
        
        
        # Creat Text
        textVersion = CreatLabelTe(infoWindow,"Revison:",5,50)
        textVersionV = CreatLabelTe(infoWindow,"V1.1",100,50)
        
        textAutor = CreatLabelTe(infoWindow,"Autor:",5,80)
        textAutorV = CreatLabelTe(infoWindow,"schaerphix",100,80)
        
        textComp = CreatLabelTe(infoWindow,"Companie:",5,110)
        textCompV = CreatLabelTe(infoWindow,"",100,110)    
        
        textDate = CreatLabelTe(infoWindow,"Date:",5,140)
        textDateV = CreatLabelTe(infoWindow,"05.12.2022",100,140)
        
        # Buttons  
        CreatButtonS3(infoWindow,"OK",InfoOK,160,250)  
        
        infoWindow.mainloop()
        
    def InfoOK():
        infoWindow.destroy()


#                           GUI
#   --------------------------------------------------------------------

    #   Window
    wid=CreatWin("Renamer")
    
    #   Title
    title = CreatLabelTi(wid,"Renamer",5,10)

    #   File Select
    selectFrame = CreatFrameWBHS(wid,5,60)
    selectHeader = CreatLabelHe(selectFrame,"File Select",5,0)
    
    labelInPath = CreatLabelTe(selectFrame,"Path of first file: ",100,25)
    inPathString = CreatLabelTe(selectFrame,"No file selected",200,25)
    
    labelNumberOfFiles = CreatLabelTe(selectFrame,"Number of files: ",100,50)
    numberOfFiles = CreatLabelTe(selectFrame,nOfFiles.GetVariable(),200,50)
        
    selectButton = CreatButtonS(selectFrame,"File Select",InPathSelect,5,35)
    
    #   Function Select
    functionFrame = CreatFrameWBHM(wid,5,140)
    functionHeader = CreatLabelHe(functionFrame,"Function Select",5,0)
    
    textChangeName = CreatLabelTe(functionFrame,"New Name:",5,20)
    textSelectValriable = CreatLabelTe(functionFrame,"Difference:",5,45)
    textVariablePosition = CreatLabelTe(functionFrame,"Position:",5,95)
    textSeparation = CreatLabelTe(functionFrame,"Option:",5,70)
    textNameBody = CreatLabelTe(functionFrame,"Name Preview:",150,120)
    textBody = CreatLabelTe(functionFrame,"",250,120)
    
    changeNameSelect = IntVar()
    changeNameSelect.set(1)
    differenceSelect = IntVar()
    differenceSelect.set(2)
    startEndSelect = IntVar()
    startEndSelect.set(2)
    separationSelect = IntVar()
    separationSelect.set(1)
    
    unchangedName = Radiobutton(functionFrame,text='No Change',variable=changeNameSelect,value = 1 )
    unchangedName.place(x=150,y=20)
    changeName = Radiobutton(functionFrame,text='New Name',variable=changeNameSelect, value=2)
    changeName.place(x=235,y=20)    
    
    dateVariant = Radiobutton(functionFrame,text='Date',variable=differenceSelect,value = 1 )
    dateVariant.place(x=150,y=45)
    numberVariant= Radiobutton(functionFrame,text='Number',variable=differenceSelect, value=2)
    numberVariant.place(x=235,y=45)
    indyVariant= Radiobutton(functionFrame,text='Customize',variable=differenceSelect, value=3)
    indyVariant.place(x=320,y=45)

    underLineSep = Radiobutton(functionFrame,text='_',variable=separationSelect,value = 1 )
    underLineSep.place(x=150,y=70)
    minusSep= Radiobutton(functionFrame,text='-',variable=separationSelect, value=2)
    minusSep.place(x=235,y=70)
    otherSep= Radiobutton(functionFrame,text='Other',variable=separationSelect, value=3)
    otherSep.place(x=320,y=70) 
    
    startPosition = Radiobutton(functionFrame,text='Beginning',variable=startEndSelect,value = 1 )
    startPosition.place(x=150,y=95)
    endPosition= Radiobutton(functionFrame,text='End',variable=startEndSelect, value=2)
    endPosition.place(x=235,y=95)
    

    global newName
    newName = CreatEntryM(functionFrame,450,20)
    newDifference = CreatEntryM(functionFrame,450,45)
    newSeparation = CreatEntryM(functionFrame,450,70)
    
    previewButton = CreatButtonS(functionFrame,"Preview",PreviewUpdat,5,120)
    
    #   START
    startFrame = CreatFrameWBHS2(wid,5,300)
    startHeader = CreatLabelHe(startFrame,"",5,0)
    
    startButton = CreatButtonL2(startFrame,"START",RenameStart,5,30)
    
    infoButton = CreatButtonS3(wid,"info",Info,624,30)
    
    
    # General
    allVar = inputPath,firstFilePath,nOfFiles,filePathFolder,toNewName,toNewNameEntry,differenceOption,differenceOptionEntry,positionOption,separationOption,separationOptionEntry,dateActual
    entryRadio = changeNameSelect,newName,differenceSelect,newDifference,separationSelect,newSeparation,startEndSelect
    varEntryRadio = toNewName,toNewNameEntry,differenceOption,differenceOptionEntry,separationOption,separationOptionEntry,positionOption,
    
    wid.mainloop()
    return 0

if __name__ == '__main__':
    main()

