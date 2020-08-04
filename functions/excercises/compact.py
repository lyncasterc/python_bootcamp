def compact(lista):
 return [val for val in lista if val]


lista = [1,2,0,"hello", True]
print(compact(lista))