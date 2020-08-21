products = []
str_products = []
p = None
multiplier = 100



while multiplier <= 999:
  for i in range(100,1000):
    p = multiplier * i
    products.append(p)

  multiplier+=1  



for i in products:
  str_products.append(str(i))

  


print(max(int(i) for i in str_products if i[::-1] == i))



