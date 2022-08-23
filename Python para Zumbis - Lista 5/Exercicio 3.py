#Exercício 3

cont = 0
x=1067
y=3628

for k in range(x, y):
    if k%2 == 0 and k%7 == 0:
        cont += 1
print (cont)
