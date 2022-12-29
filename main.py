import pandas as pd
import numpy as np
import os
import glob
import SIC.SICparser as SICparser
import SIC.SICloadmap as SICloadmap
import SIC.SICmemory as SICmemory
import SIC.SICmemoryFill as SICmemoryFill
from pandasgui import show


Program_type = input("Enter (1) for Absolute loader and (2) for Linker-loader:   ")
if(Program_type == "1"):
   files = glob.glob('./SIC/Res/*')    # clear result dir for new files
   for q in files:
     os.remove(q)
   prog = SICparser.parseFile("Test/sic.txt")
   prog = SICloadmap.loadMap(prog=prog,Launch="4000")
   prog = SICmemory.memorySetup(prog=prog)
   prog = SICmemoryFill.memoryFill(prog=prog)
   #show(prog.MEMORY)