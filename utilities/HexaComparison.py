def hexaCompare(a,b):
   q = hex(int(a,16))
   w = hex(int(b,16))
   if(q>w):
      return True
   else:
      return False