#Exercício 1

a = float(input('Digite o valor do lado A:'))
b = float(input('Digite o valor do lado B:'))
c = float(input('Digite o valor do lado C:'))

if a + b < c or a + c < b or b + c < a:
  print ('\nNão é um triângulo')

else:
  print ('\nÉ um triangulo')

  if a == b == c:
    print ('\nO triângulo é Equilátero')

  elif a == b or b == c or c == a:
    print ('\nO triângulo é Isósceles')

  else:
    print ('\nO triângulo é Escaleno') 

