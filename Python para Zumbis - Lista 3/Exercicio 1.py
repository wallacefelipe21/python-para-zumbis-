#Exercícios 1 

nota=int(input('Digite uma nota:'))

while nota<0 or nota>10:
    print('\nValor inválido, notas devem ter valor entre 0 e 10')
    nota=int(input('\nDigite uma nota:'))

else:
    print('\nValor válido')