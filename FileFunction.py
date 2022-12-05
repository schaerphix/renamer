# *********************************************************************
# 
#                           FileFunction
#
#**********************************************************************
#
#  Autor:    schaerphix
#  Date:     05.12.2022
#  Revision: V1.1
#
#  LICENSE:  GNU General Public License v3.0  
#
#  FileFunction.py
#  
#  
# Description
# ===========
# With the Rename you can Rename Files and Folder
# 
#  


#   ********************************************************************
#                           Import
#   ********************************************************************
import os
import shutil
from os import path



#   ********************************************************************
#                           Function
#   ********************************************************************
def Rename(pfad,fileName,newName):
    if path.exists(pfad + fileName):                                    
        os.rename(pfad + fileName, pfad + newName)                      
        status = 0
        statusText = "Rename in new name %s done"%(newName)              
    else:
        status = 1
        statusText = "Error:    File or Path not found"                 
    return status,statusText
    
    

