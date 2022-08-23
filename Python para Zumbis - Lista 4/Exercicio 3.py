#Exercicio 3

import random

vetor1=random. sample (range (0,100), 10)
vetor2=random. sample (range (0,100), 10) 
vetor3=[]

for x in range (0,10):
  vetor3.append (vetor1 [x])
  vetor3.append(vetor2 [x])
  
print ('Lista aleatória A:', vetor1, '\nLista aleatória B:', vetor2, '\n\nLista Misturada:', vetor3)