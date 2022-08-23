#Exercício 4

cont = 0
x=18644
y=33087

for k in range(x, y):
    if '2' in str(k) and '7' not in str(k):
        cont += 1
print (cont)