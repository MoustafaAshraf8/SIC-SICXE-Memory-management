import pandas as pd
import numpy as np
import os
import glob
import Class.SICXEClass as sicxe
import Class.SICclass as sic
import utilities.HexaAddition as f
import ErrorClass as Err

def loadMap(prog: sic, Launch:str):
   print("------------LoadMap-sic-------------------------")
  
   DFlist = prog.DFlist
   info = []
   rowList = []
   

   for df in DFlist:

      progName = df.iloc[0,0][1:][:5]     #program name,start address,length, actual start
      progStart = df.iloc[0,0][6:][:6]
      proglen = df.iloc[0,0][-6:]
      actualStart = f.hexaAddition(progStart,proglen)


      # lst = df.iloc[0,0].split()
      # progName = lst[0][1:]
      # progStart = lst[1][:6]
      # proglen = lst[1][6:]
      # actualStart = f.hexaAddition(progStart,proglen)

      rowList.append(progName)   #insert progName as row index
      info.append((progStart,proglen,actualStart)) #insert prog info
      
   LMdf = pd.DataFrame(info,index=rowList,columns=["address","length","end"])
   prog.LoadMap = LMdf
   # files = glob.glob('./Res/*')
   # for q in files:
   #   os.remove(q)
   LMdf.to_excel("Res/loadmapSIC.xlsx")
   LMdf.to_csv("Res/loadmapSIC.txt",sep="\t")
   print(prog.LoadMap)

   return prog