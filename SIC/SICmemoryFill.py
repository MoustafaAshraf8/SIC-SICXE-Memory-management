import pandas as pd
import numpy as np
import os
import glob
import Class.SICclass as sic
import utilities.HexaAddition as f
import utilities.HexaComparison as hexcomp
from pandasgui import show
import ErrorClass as Err

lst = []
def splittxt(s):
   if(len(s) == 0):
      return lst
   lst.append(s[:2])
   splittxt(s[2:])

def TrecordPlacement(progaddress,row,memory):
   #start = f.hexaAddition(row[0][1:7],progaddress)     #actual start address of T record
   #print(start)
   Tstart = row[0][1:7]
   opcode = row[0][9:]     #T record - ('T',start address,length)
   lst.clear()
   splittxt(opcode)        #opcode -> list of (2) hexa digits
   #print(lst)
   for i in range(0,len(lst)):
      byte = lst[i]              #2 hexa to place
      #print(byte)
      
      actualaddress = f.hexaAddition(Tstart,hex(i))    #convert i to hexa, heaxaAddition takes hexa values
      #print(actualaddress)
      #print(byte)
      #print(actualaddress)
      row = actualaddress[:5]+"0"
      col = actualaddress[5:]
      #print(row,col)
      memory.loc[row[:6],col] = byte
   lst.clear()




def memoryFill(prog: sic):
   print("----------------------------Memory-sic-fill--------------------------")
   MEMORY = prog.MEMORY
   #print(MEMORY)
   LoadMap = prog.LoadMap
   #print(MEMORY)

   DFlist = prog.DFlist
   for df in DFlist:
      for index,row in df.iterrows():
         if(row[0][:1] == "T"):
            #print(row[0])
            progname = df.iloc[0,0][1:][:5]
            #print(progname)
            progaddress = LoadMap.loc[progname,"address"]
            TrecordPlacement(progaddress,row,MEMORY)
            #print(row[0][0])
   MEMORY.replace(to_replace = np.nan, value ="-", inplace=True)
   prog.MEMORY = MEMORY
   print(MEMORY.to_string())
   #print(MEMORY.loc["002070","A"])
   #show(MEMORY)
   return   prog