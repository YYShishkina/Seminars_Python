for i in range (0, 2):
    for j in range (0,2):
        for k in range (0,2):
            if (i or j or k) == i and j and k:
                print ('for')
                print(i,j,k)
                print ('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z is True')
            