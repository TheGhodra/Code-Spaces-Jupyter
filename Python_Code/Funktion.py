def prim(zahl):
    if zahl == 1:
        return False
    if zahl == 2:
        return True
    
    for i in range(2, zahl):
        if zahl % 1 == 0:
            return False
        return True
    
for zahl in range(1, 100):
    if prim(zahl):
        print(zahl)