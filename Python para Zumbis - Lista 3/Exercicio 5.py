#Exercícios 5

a=int(input('Digite o valor de A:'))
b=int(input('Digite o valor de B:'))
x=a%b

while a%b != 0:
    a,b=b,a%b
    x=b
    
print ('O máximo divisor comum é:',x)