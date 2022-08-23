#Exercício 9

km=float(input('Digite a quantidade de Km percorridos: '))
dias=int(input('Digite a quantidade de dias: '))

precodia=dias*60
precokm=km*0.15

precototal=precodia+precokm

print('\nO preço total do aluguel é: R$', precototal)

