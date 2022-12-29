import pandas as pd
import numpy as np
import os
import glob
import Class.SICXEClass as sicxe
import utilities.HexaAddition as f
import utilities.MrecordAddition as Maddition
from pandasgui import show
import ErrorClass as Err
lst = []
def splittxt(s):
   if(len(s) == 0):
      return lst
   lst.append(s[:2])
   splittxt(s[2:])

   



def TrecordPlacement(progaddress,row,memory):
   start = f.hexaAddition(row[0][1:7],progaddress)     #actual start address of T record
   #print(start)
   opcode = row[0][9:]     #T record - ('T',start address,length)
   splittxt(opcode)        #opcode -> list of (2) hexa digits
   print(lst)
   for i in range(0,len(lst)):
      byte = lst[i]              #2 hexa to place
      #print(byte)
      
      actualaddress = f.hexaAddition(start,hex(i))    #convert i to hexa, heaxaAddition takes hexa values
      #print(actualaddress)
      #print(byte)
      #print(actualaddress)
      row = actualaddress[:5]+"0"
      col = actualaddress[5:]
      #print(row,col)
      memory.loc[row,col] = byte
      #print(memory.loc[row,col])
      #print(type(memory.loc[row,col]))
      #print(memory.loc[row,col])
   lst.clear()


def MrecordModify(progaddress,row,memory,loadmap):
   addressToModify = f.hexaAddition(progaddress,row[0][1:7])      #000052
   # print("---------------")
   # print(row[0])
   # print(addressToModify)
   len = row[0][7:9]       #06
   operator = row[0][9:10] #+/-
   #print("here",row[0][10:])
   required = loadmap.loc[row[0][10:],"start"]  #ENDA
   #print(required)
   # row = addressToModify[:5]+"0"
   # col0 = addressToModify[5:]
   # col1 = f.hexaAddition(col0,"1")[5:]
   # col2 = f.hexaAddition(col0,"2")[5:]

   r0 = f.hexaAddition(addressToModify,"0")  #00402E
   r1 = f.hexaAddition(addressToModify,"1")
   r2 = f.hexaAddition(addressToModify,"2")
   #print(r0,r1,r2)


   row0 = r0[:5]+"0"
   row1 = r1[:5]+"0"
   row2 = r2[:5]+"0"
   col0 = r0[5:]
   col1 = r1[5:]
   col2 = r2[5:]

   #print(row,col0,col1,col2)
   byte0 = memory.loc[row0,col0]
   byte1 = memory.loc[row1,col1]
   byte2 = memory.loc[row2,col2]
   #print(byte0,byte1,byte2)

   if(len == "06"):
      lst.clear()
      total = byte0 + byte1 + byte2
      #newVal = Maddition.SpecialOperator(total,operator,str(required))
      if operator == "+":
         newVal = Maddition.SpecialOperator(total,operator,required)
         splittxt(newVal)
      if operator == "-":
         newVal = Maddition.SpecialOperator(total,operator,required)
         splittxt(newVal)
      
      
      memory.loc[row0,col0] = lst[0]
      memory.loc[row1,col1] = lst[1]
      memory.loc[row2,col2] = lst[2]
      lst.clear()
   elif(len == "05"):
      # total = byte0 + byte1 + byte2
      # #newVal = Maddition.SpecialOperator(total,operator,required)
      # if(operator == "+"):
      #    newVal = hex(int(total[1:], 16) + int(required[1:], 16))[2:].zfill(5).upper()
      #    newVal = newVal[-6:]
      # if(operator == "-"):
      #    newVal = hex(int(total[1:], 16) - int(required[1:], 16))[2:].zfill(5).upper()
      #    newVal = newVal[-6:]
      
      # splittxt(newVal)
      # print("4444444444",lst)
      # memory.loc[row0,col0] = lst[0]
      # memory.loc[row1,col1] = lst[1]
      # memory.loc[row2,col2] = lst[2]
      lst.clear()
      total = byte0 + byte1 + byte2
      #newVal = Maddition.SpecialOperator(total,operator,str(required))
      if operator == "+":
         newVal = Maddition.SpecialOperator(total,operator,required)
         splittxt(newVal)
         #newVal = hex(int(total[1:], 16) + int(required[1:], 16))[2:].zfill(5).upper()
         
      if operator == "-":
         newVal = Maddition.SpecialOperator(total,operator,required)
         splittxt(newVal)
         #newVal = hex(int(total[1:], 16) - int(required[1:], 16))[2:].zfill(5).upper()
         
      print("111111111111111111",lst)
      memory.loc[row0,col0] = memory.loc[row0,col0][:1]+lst[0][1:]
      memory.loc[row1,col1] = lst[1]
      memory.loc[row2,col2] = lst[2]
      lst.clear()

   # elif(len == "05"):
   #    total = byte0 + byte1 + byte2
   #    if(operator == "+"):
   #       newVal = hex(int(total[1:], 16) + int(required, 16)[1:])[2:].zfill(5).upper()
   #       newVal = newVal[-6]
   #    if(operator == "-"):
   #       newVal = hex(int(total[1:], 16) - int(required, 16))[2:].zfill(5).upper()
   #       newVal = newVal[-6:]
      
   
   lst.clear()

   return

def memoryFill(prog: sicxe):
   print("----------------------------------Memory-fill----------------------------")
   DFlist = prog.DFlist
   LoadMap = prog.LoadMap
   MEMORY = prog.MEMORY



   for df in DFlist:
      for index,row in df.iterrows():
         
         if(row[0][:1] == "T"):
            #print(row[0])
            progname = df.iloc[0,0][1:][:5]
            #print(progname)
            progaddress = LoadMap.loc[progname,"start"]
            TrecordPlacement(progaddress,row,MEMORY)
            #print(row[0][0])
         elif(row[0][:1] == "M"):
            progname = df.iloc[0,0][1:][:5]
            progaddress = LoadMap.loc[progname,"start"]
            #print(progname)
            #print(row[0])
            MrecordModify(progaddress,row,MEMORY,LoadMap)
   
   prog.MEMORY = MEMORY
   #print(MEMORY.to_string())
   #show(MEMORY)
   return prog