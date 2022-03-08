#Exercício 2

ano = int(input('Digite o ano desejado:'))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
  print ('\nO ano é Bissexto')

else:
  print ('\nO ano não é Bissexto')
