import pandas as pd
import numpy as np
import Class.SICXEClass as sicxe
import Class.SICclass as sic
import ErrorClass as Err
# from pandasgui import show
def parseFile(FilePath):
   print("------------Parser-sic--------------------------")
   prog = sic
   df = pd.read_csv(FilePath, delimiter='\t',header=None)
   prog.df = df
   DFlist = []
   i = 1
   start = 0
   end = 0
   for x in range(len(df)):
      if(df.iloc[x,0][:1] == "E"):
         end = i
         DFlist.append(df[start:end])
         start = end
      i=i+1
   prog.DFlist = DFlist    #list of df/programs

   #print(len(DFlist))

   return prog
