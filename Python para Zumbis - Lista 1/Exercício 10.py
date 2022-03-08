#Exercício 10

cigarros=int(input('Números de cigarros fumados por dia:'))
anos=int(input('Anos como fumante:'))

conversao=cigarros*anos*365//144
print('\nPerdeu', conversao, 'dias')
