# ISR
# Equipo 2: Roberto, Alejandra y Juan Pablo Valdez
# Fecha: 25/02/2021

#Entradas
salario = float(input("Digite el salario para el calculo del impuesto:"))

#Procesos
if salario <= 3644.94:
  ISR = 12.88 + ((salario - 0.01) * 0.10)
  print(ISR)

if  3644.94<=salario <= 7446.19:
  ISR = 303.76 + ((salario - 3644.95) * 0.20)
  print(ISR)

if 7446.19<= salario <= 10298.35:
  ISR = 1063.92 + ((salario - 7446.20) * 0.30)
  print(ISR)

if salario > 10298.35:
  ISR = 3327.42 + ((salario - 10298.35) * 0.35)
  print(ISR)
