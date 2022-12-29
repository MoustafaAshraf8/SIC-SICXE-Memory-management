import pandas as pd
import numpy as np
import Class.SICXEClass as sicxe
import ErrorClass as Err
# from pandasgui import show
def parseFile(FilePath):
   print("------------Parser-sicxe--------------------------")
   df = pd.read_csv(FilePath, delimiter='\t',header=None)
   DataList = df.values.tolist()
   prog = sicxe.SICXE
   prog.df = df
   prog.DataList = DataList
   prog.HeaderList = df.columns.values 
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

   prog.DFlist = DFlist

   return prog