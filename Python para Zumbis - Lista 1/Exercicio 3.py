#Exercício 3

dias=int(input('Digite a quantidade de dias:'))
horas=int(input('Digite a quantidade de horas:'))
minutos=int(input('Digite a quantidade de minutos:'))
segundos=int(input('Digite a quantidade de segundos:'))

convertdias=dias*24*60*60
converthoras=horas*60*60 
convertminutos=minutos*60 

resultfinal=convertdias+converthoras+convertminutos+segundos

print('\nO valor convertido para segundos é', resultfinal)
