import pandas as pd
import numpy as np
import os
import glob
import Class.SICXEClass as program
import utilities.HexaAddition as f
import ErrorClass as Err

def loadMap(prog: program.Program_SICXE, Launch:str):
   print("------------LoadMap-sicxe-------------------------")
  
   DFlist = prog.DFlist
   info = []
   rowList = []
   LaunchAddress = Launch   ####input from user

   for df in DFlist:

      # lst = df.iloc[0,0].split()
      # progName = lst[0][1:]
      # progStart = lst[1][:6]
      # proglen = lst[1][6:]
      # actualStart = f.hexaAddition(progStart,Launch)

      progName = df.iloc[0,0][1:][:5]     #program name,start address,length, actual start
      progStart = df.iloc[0,0][7:][:6]
      proglen = df.iloc[0,0][-6:]
      actualStart = f.hexaAddition(LaunchAddress,progStart)

      rowList.append(progName)   #insert progName as row index
      info.append((progStart,proglen,actualStart,"-")) #insert prog info

      extDef = df.iloc[1,0][1:].split()
      DIC = {extDef[i]: extDef[i + 1] for i in range(0, len(extDef), 2)}
      for x in DIC:
         rowList.append(x)
         info.append((DIC[x],"000000",f.hexaAddition(LaunchAddress,DIC[x]),progName))
      
      LaunchAddress = f.hexaAddition(actualStart,proglen)   #update launch address

   LMdf = pd.DataFrame(info,index=rowList,columns=["address","length","start","program"])
   prog.LoadMap = LMdf
   files = glob.glob('./Res/*')
   for q in files:
     os.remove(q)
   LMdf.to_excel("Res/loadmap.xlsx")
   LMdf.to_csv("Res/loadmap.txt",sep="\t")
   print(prog.LoadMap)

   return prog