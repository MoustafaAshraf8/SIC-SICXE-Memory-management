import pandas as pd
from pandasgui import show
class SICXE:
   df: pd.DataFrame
   LoadMap: pd.DataFrame
   DataList: list
   HeaderList: list
   DFlist: list
   MEMORY: pd.DataFrame
   def __init__(self):
      return

   def printdf(self):
      print(self.df)
   
   def MemoryShow(self):
        show(self.MEMORY)
