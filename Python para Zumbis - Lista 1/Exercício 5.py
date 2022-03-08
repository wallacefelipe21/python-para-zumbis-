#Exercício 5

preco=float(input('Digite o valor da mercadoria: R$'))
desconto=float(input('Digite a porcentagem de desconto: '))

precofinal= (desconto * preco / 100) 


print('\nValor final da mercadoria: R$', preco - precofinal)
print('Valor do desconto: R$', precofinal)
