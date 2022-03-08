#Exercício 3

kg = float(input('Digite o peso dos peixes em Kg:'))

if kg > 50:
  excesso = kg - 50
  multa = excesso * 4
  print ('\nO valor da multa é: R$', multa)

else:
  print ('\nJoão não pagará multa')

