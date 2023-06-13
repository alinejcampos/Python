salario = float(input('Qual valor do seu sálario? '))
soma = salario / 1300

if soma <= 1:
 print(f'Você recebe {soma:,.0f} salário minimo!')
 
if soma <= 5:
 print(f'Você está acima do salário minimo e recebe {soma:,.1f}') 
 
else:
     
 print(f'Você recebe {soma:,.1f} salários minimos!')
 
