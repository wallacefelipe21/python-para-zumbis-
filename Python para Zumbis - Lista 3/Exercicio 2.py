#Exercícios 2

nome=str(input('Digite seu nome de usuário:'))
senha=str(input('Digite sua senha:'))

while nome == senha:
    print('\nERRO!!!')
    nome=str(input('\nDigite seu nome de usuário:'))
    senha=str(input('Digite sua senha:'))

else:
    print('\nEntrou')