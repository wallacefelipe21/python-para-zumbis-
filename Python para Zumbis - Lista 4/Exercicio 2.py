#Exercicio 2

import random

lista=random.sample(range (0,100),20)
par=[]
impar=[]

for y in lista:
  if (y%2)!=0:
    impar.append(y)
  else:
    par.append(y)
    
print ('Lista', lista, '\nNúmeros pares:',par,'\nNúmero impares:', impar)
