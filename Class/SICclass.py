import pandas as pd
from pandasgui import show
class SIC:
   df: pd.DataFrame
   DFlist: list
   LoadMap: pd.DataFrame
   MEMORY: pd.DataFrame

   def __init__(self):
      return

   def printdf(self):
      print(self.df)

   def MemoryShow(self):
      show(self.MEMORY)
