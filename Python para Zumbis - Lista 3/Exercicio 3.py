#Exercícios 3

populacaoA=80000
populacaoB=200000
ano=0

while populacaoA <= populacaoB:
    populacaoA+=(populacaoA*0.03)
    populacaoB+=(populacaoB*0.015)
    ano+=1
    
print('Número de anos para a população A igualar a população B'.ano)
