import os
import glob
import SIC.SICparser as SICparser
import SIC.SICloadmap as SICloadmap
import SIC.SICmemory as SICmemory
import SIC.SICmemoryFill as SICmemoryFill
import SICXE.SICXEparser as parserSICXE
import SICXE.SICXEloadMap as LM
import SICXE.SICXEmemory as MEM
import SICXE.SICXEmemoryFill as MEMfill

Program_type = input("Enter (1) for Absolute loader and (2) for Linker-loader:   ")
if(Program_type == "1"):
   files = glob.glob('./SIC/Res/*')
   for q in files:
     os.remove(q)
   prog = SICparser.parseFile("Test/sic.txt")
   prog = SICloadmap.loadMap(prog=prog,Launch="4000")
   prog = SICmemory.memorySetup(prog=prog)
   prog = SICmemoryFill.memoryFill(prog=prog)
   prog.MemoryShow(prog)

else:
   files = glob.glob('./SICXE/Res/*')
   for q in files:
     os.remove(q)
   startAddress = input("Enter address to start from:    ")
   prog = parserSICXE.parseFile(FilePath="Test/sicxe.txt")
   prog = LM.loadMap(prog=prog,Launch=startAddress)
   prog = MEM.memorySetup(prog=prog)
   prog = MEMfill.memoryFill(prog=prog)
   prog.MemoryShow(prog)




