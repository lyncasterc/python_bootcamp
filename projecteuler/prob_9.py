def pythagoreanTriplets() : 
    c, m = 0, 2
    boop = True
  
    # Limiting c would limit  
    # all a, b and c 
    while boop == True : 
          
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            # if c is greater than 
            # limit then break it 
            if a+b+c == 1000:
              print(a,b,c, a*b*c)  
              boop = False
              break
  
            # print(a, b, c) 
  
        m+=1
  
pythagoreanTriplets()