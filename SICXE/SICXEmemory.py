import pandas as pd
import numpy as np
import os
import glob
import Class.SICXEClass as sicxe
import utilities.HexaAddition as f
from pandasgui import show
import ErrorClass as Err


def memorySetup(prog: sicxe):
   print("----------------------------Memory---------------------------")
   DFlist = prog.DFlist
   LM = prog.LoadMap
   startAddress = LM.iloc[0,2][:5]+"0"
   endAddress = 0
   for ind in LM.index:
    if(LM.loc[ind]["program"] == "-"):
      a = LM.loc[ind]["start"]
      b = LM.loc[ind]["length"]
      endAddress = f.hexaAddition(a,b)[:5]+"0"
   
   MEMcol = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
   MEMrow = []
   while 1:
      MEMrow.append(startAddress)
      startAddress = f.hexaAddition(startAddress,"10")
      if(MEMrow[-1] == endAddress):
         break
   
   MEMORY = pd.DataFrame(index=MEMrow,columns=MEMcol)
   MEMORY.fillna("-", inplace=True)
   prog.MEMORY = MEMORY
   #print(MEMORY)
   # for df in DFlist:
   #    for index,row in df.iterrows():
   #       if(row[:1] == "T"):
   #          print(row[1:7])
   print(MEMORY)
   return prog