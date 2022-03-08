#Exercício 6

horatrabmes = int(input('Digite a quantidade de horas trabalhadas no mês:'))
valhora = float(input('Digite o valor da hora trabalhada:'))

salariobruto = horatrabmes * valhora
ir = (salariobruto * 11) / 100
inss = (salariobruto * 8) / 100
sind = (salariobruto * 5) / 100
salarioliqui = salariobruto - (ir+inss+sind)

print('\nSalário Bruto: R$ ', salariobruto,
      '\nImposto de Renda: R$', ir,
      '\nINSS: R$', inss,
      '\nSindicato: R$', sind,
      '\nSalário Líquido: R$', salarioliqui)
