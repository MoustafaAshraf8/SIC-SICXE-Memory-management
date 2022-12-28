import pandas as pd
import numpy as np
import os
import glob
import Class.SICclass as sic
import utilities.HexaAddition as f
import utilities.HexaComparison as hexcomp
from pandasgui import show
import ErrorClass as Err


def memorySetup(prog: sic):
   print("----------------------------Memory-sic--------------------------")
   DFlist = prog.DFlist
   LM = prog.LoadMap
   startAddress = LM.iloc[0,0]
   endAddress = f.hexaAddition(startAddress,LM.iloc[0,1])[:5]+"0"
   #print(startAddress)
   #print(endAddress)
   MEMcol = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
   # maxlen = "0"
   # for ind in LM.index:
   #    a = LM.loc[ind]["start"]
   #    b = LM.loc[ind]["length"]
   #    endAddress = f.hexaAddition(a,b)[:5]+"0"
   #    if(hexcomp.hexaCompare(endAddress,maxlen) == True):
   #       maxlen = endAddress
   #       print(maxlen)
   #    print(endAddress)
   #    print(hexcomp.hexaCompare(endAddress,maxlen))

   # endAddress = max
   # print(type(endAddress))



   startAddress = startAddress[:5]+"0"
   MEMrow = []
   while 1:
      MEMrow.append(startAddress)
      startAddress = f.hexaAddition(startAddress,"10")
      if(MEMrow[-1] == endAddress):
         break
   
   MEMORY = pd.DataFrame(index=MEMrow,columns=MEMcol)
   MEMORY.fillna("-", inplace=True)
   prog.MEMORY = MEMORY
   # #print(MEMORY)
   # # for df in DFlist:
   # #    for index,row in df.iterrows():
   # #       if(row[:1] == "T"):
   # #          print(row[1:7])
   print(MEMORY.to_string())
   return prog