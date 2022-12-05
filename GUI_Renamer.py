# *********************************************************************
# 
#                           GUI
#
#**********************************************************************
#
#  Autor:    schaerphix
#  Date:     05.12.2022
#  Revision: V1.1
#
#  LICENSE:  GNU General Public License v3.0  
#
#  GUI.py
#
#
# Description
# ===========
# All GUI funktion ar defined in this file.


# Imports
from tkinter import*
from GUIdef_Renamer import*


#   ********************************************************************
#                           Creat Window
#   ********************************************************************
#
#       Creats a new window. The size, icon and color sceme are definned
#       in the value file.
#           Inputs:     Title of the window
#           Output:     Window index

def CreatWin(tit): 
    win = Tk()
    win.geometry(winSizeM)
    win.title(tit)
    #win.iconbitmap(winIcon)
    win.tk_setPalette(winColor)
    return win 

def CreatWin2(tit): 
    win = Tk()
    win.geometry(winSizeS)
    win.title(tit)
    #win.iconbitmap(winIcon)
    win.tk_setPalette(winColor)
    return win  
   
    
#   ********************************************************************
#                           Creat Frame
#   ********************************************************************
#
#       Creats a new Frame. The Background, the width, the height , the
#       relief and the borderwidth are defined in the value file.
#           Inputs:     The root of the Frame, position X and Position Y
#           Output:     Frame Index index
    

#   Frame 3 unit width and 1 unit height
def CreatFrameWBHS (rot,pox,poy):
    fra = Frame(rot,background=frBackground,width=frWidthBig,height=frHeightSmal,relief=frRelief,borderwidth=frBorderwidth)
    fra.place(x=pox,y=poy)
    return fra    

#   Frame 3 unit width and 1 unit height
def CreatFrameWBHS2 (rot,pox,poy):
    fra = Frame(rot,background=frBackground,width=frWidthBig,height=frHeightSmal,relief=frRelief2,borderwidth=frBorderwidth)
    fra.place(x=pox,y=poy)
    return fra
    
#   Frame 3 unit width and 2 unit height
def CreatFrameWBHM (rot,pox,poy):
    fra = Frame(rot,background=frBackground,width=frWidthBig,height=frHeightMid,relief=frRelief,borderwidth=frBorderwidth)
    fra.place(x=pox,y=poy)
    return fra 
    
#   Frame 2 unit width and 3 unit height
def CreatFrameWMHB (rot,pox,poy):
    fra = Frame(rot,background=frBackground,width=frWidthMid,height=frHeightBig,relief=frRelief,borderwidth=frBorderwidth)
    fra.place(x=pox,y=poy)
    return fra
    
#   Frame 3 unit width and 3 unit height
def CreatFrameWBHB (rot,pox,poy):
    fra = Frame(rot,background=frBackground,width=frWidthBig,height=frHeightBig,relief=frRelief,borderwidth=frBorderwidth)
    fra.place(x=pox,y=poy)
    return fra 



#   ********************************************************************
#                           Create Canvas
#   ********************************************************************
#
#       Creats a new Canvas. The Background, the width and the height are
#       defined in the value file.
#           Inputs:     The root of the Canvas, position X and Position Y
#           Output:     Canvas index
    
def CreatCanvasMid (rot,pox,poy):
    can = Canvas(rot,background=caBackground,width=caWidthMid, height=caHeightMid)
    can.place(x=pox,y=poy)
    return can    
 
 
    
#   ********************************************************************
#                           Create Labels
#   ********************************************************************
#
#       Creats a new Labels. The background, the font (Type, style, color
#       and size) are defined in the value file.
#           Inputs:     The root of the Label, the Label text, position X and Position Y
#           Output:     Label index

#   Creat Title
def CreatLabelTi (rot,tex,pox,poy):
    tit = Label(rot,background=laBackground,foreground=tiFonCo,text=tex,font=(tiFon,tiFonSiz,tiFonSty))
    tit.place(x=pox,y=poy)
    return tit  

#   Creat Header
def CreatLabelHe (rot,tex,pox,poy):
    hea = Label(rot,background=laBackground,foreground=heFonCo,text=tex,font=(heFon,heFonSiz,heFonSty))
    hea.place(x=pox,y=poy)
    return hea  
    
#   Creat Text
def CreatLabelTe (rot,tex,pox,poy):
    tet = Label(rot,background=laBackground,foreground=teFonCo,text=tex,font=(teFon,teFonSiz,teFonSty))
    tet.place(x=pox,y=poy)
    return tet
    
#   ********************************************************************
#                           Create Button
#   ********************************************************************
#
#       Creats a new Buttons. The background, the font, the size and the
#       refilef are defined in the value file.
#           Inputs:     The root of the Button, the Button text, the action
#                       position X and Position Y
#           Output:     Button index

#   Create Button S
def CreatButtonS(rot,tex,act,pox,poy):
    but =  Button(rot,background=buBackground,width=buWidthS,text=tex)  
    but["command"] = act
    but.place(x=pox,y=poy)
    return but  
    
#   Create Button S 3
def CreatButtonS3(rot,tex,act,pox,poy):
    but =  Button(rot,background=buBackground3,width=buWidthS,text=tex)  
    but["command"] = act
    but.place(x=pox,y=poy)
    return but 

#   Create Button M 
def CreatButtonM(rot,tex,act,pox,poy):
    but =  Button(rot,background=buBackground,width=buWidthM,text=tex)  
    but["command"] = act
    but.place(x=pox,y=poy)
    return but   
    
#   Creat Button L 2
def CreatButtonL2(rot,tex,act,pox,poy):
    but =  Button(rot,background=buBackground2,width=buWidthL,text=tex)  
    but["command"] = act
    but.place(x=pox,y=poy)
    return but     
    
    
    
#   ********************************************************************
#                           Create Entry
#   ********************************************************************
#
#       Creats a new Entrys. The background, the size, the relief and 
#       the broderwidth are defined in the value file.
#           Inputs:     The root of the Entry, position X and Position Y
#           Output:     Entry index          

#   Creat Entry M
def CreatEntryM(rot,pox,poy):
    ent = Entry(rot,background=enBackground,relief=enRelief,bd=enBorderwidth,width=enWidthM)
    ent.place(x=pox,y=poy)
    return ent 
    
#   Creat Entry L
def CreatEntryL(rot,pox,poy):
    ent = Entry(rot,background=enBackground,relief=enRelief,bd=enBorderwidth,width=enWidthL)
    ent.place(x=pox,y=poy)
    return ent
    
        
#   ********************************************************************
#                           Create Text Output with Scrollbar
#   ********************************************************************
#
#       Creats a new Text Output with Scrollbar. The background, the size, 
#       the relief and the broderwidth are defined in the value file.
#           Inputs:     The root of the Text Output, the text, position X 
#                       and position Y
#           Output:     Text Output index    

#   Create Text Output Width S and Height S
def CreateTexOutWSHS(rot,tex,pox,poy):
    scr =Scrollbar(rot,width=15)
    teo= Text(rot,background=teOuBackground,relief=teOuRelief,borderwidth=teOuBorderwidth,width=teOuWidthS,height=teOuHeightS)
    scr.place(x=(teOuWidthS*8)+pox+4,y=poy,height=40*teOuHeightS)       
    teo.place(x=pox,y=poy,height=40*teOuHeightS)          
    scr.config(command=teo.yview)
    teo.config(yscrollcommand=scr.set)
    teo.insert(END,tex)
    return teo 



