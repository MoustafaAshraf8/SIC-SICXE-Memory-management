def SpecialOperator(a,operator,b):
   if(operator == "+"):
      basehexin = int(a, 16)
      sechexin = int(b, 16)
      # actualStart = hex(basehexin + sechexin)[2:].upper().zfill(6)
      actualStart = hex((basehexin + sechexin) & (2**24-1))[2:].upper().zfill(6)[-6:]
      # if(len(actualStart) > 6):
      #    actualStart = actualStart[len(actualStart)-6:]
      print(actualStart)
      return actualStart
   else:
      basehexin = int(a, 16)
      sechexin = int(b, 16)
      actualStart = hex((basehexin - sechexin) & (2**24-1))[2:].upper().zfill(6)[-6:]
      
      # if(len(actualStart) > 6):
      #    actualStart = actualStart[len(actualStart)-6:]
      print(actualStart)
      return actualStart
   