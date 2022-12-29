import pandas as pd
import numpy as np
import SIC.AbsoluteLoader as abs
import SIC.SICparser as SICparser
import SIC.SICloadmap as SICloadmap
import SIC.SICmemory as SICmemory
import SIC.SICmemoryFill as SICmemoryFill
import SICXE.SICXEparser as parserSICXE
import SICXE.SICXEloadMap as LM
import SICXE.SICXEmemory as MEM
import SICXE.SICXEmemoryFill as MEMfill
import Class.SICclass as sic
import Class.SICXEClass as sicxe
from pandasgui import show

Program_type = input("Enter (1) for Absolute loader and (2) for Linker-loader:   ")
if(Program_type == "1"):
   prog = SICparser.parseFile("Test/sic.txt")
   prog = SICloadmap.loadMap(prog=prog,Launch="4000")
   prog = SICmemory.memorySetup(prog=prog)
   prog = SICmemoryFill.memoryFill(prog=prog)
   show(prog.MEMORY)

else:
   startAddress = input("Enter address to start from:    ")
   prog = parserSICXE.parseFile(FilePath="Test/sicxe.txt")
   #start = input("enter the start address: ")
   prog = LM.loadMap(prog=prog,Launch="4000")
   prog = MEM.memorySetup(prog=prog)
   prog = MEMfill.memoryFill(prog=prog)
   show(prog.MEMORY)




