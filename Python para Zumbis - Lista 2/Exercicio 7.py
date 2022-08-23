#Exercício 7

metros = float(input('Digite o valor da área em metros: '))

if metros % 54 == 0:
  lata = metros / 54
else: 
  lata = (metros // 54) + 1

preco = lata * 80 

print ('\nNúmero de latas:', lata, '\nPreço: R$ ', preco)
