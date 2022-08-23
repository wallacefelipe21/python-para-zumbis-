#Exercicio 1

import random

x=random.sample (range (0,100), 10)
maior=0
menor=101

for y in x:
  if y > maior:
    maior=y
  if y < menor:
    menor=y
print ('Lista:',x,'\nMenor número:',menor, '\nMaior número:', maior)