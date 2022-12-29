def hexaAddition(a,b):
   basehexin = int(a, 16)
   sechexin = int(b, 16)
   actualStart = hex(basehexin + sechexin)[2:].upper().zfill(6)
   return actualStart