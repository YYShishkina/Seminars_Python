for i in range (0, 2):
    for j in range (0,2):
        for k in range (0,2):
            print(f' {i},{j},{k},{(not (i or j or k) == ((not i) and (not j) and (not k)))}') 