# Fecha: 03/03/2021
# Autores: Bruno, Maite y Juan Pablo Rubio

# ENTRADA
salario = float(input("Escriba su salario"))

#PROCESO
if salario >= 0.01 and salario <= 3644.94:    
 lim_inferior = 0.01
 lim_superior = 3644.94
 excedente = salario - lim_inferior
 impuesto_marginal = excedente * .10
 isr = impuesto_marginal + 12.88
elif salario >= 3644.95 and salario <=7446.19:
 lim_inferior = 3644.95
 lim_superior = 7446.19
 excedente = salario - lim_inferior
 impuesto_marginal = excedente * .20
 isr = impuesto_marginal + 303.76
elif salario >= 7446.20 and salario <=10298.35:
 lim_inferior = 7446.20
 lim_superior = 10298.35
 excedente = salario - lim_inferior
 impuesto_marginal = excedente * .30
 isr = impuesto_marginal + 1063.92

else:
 lim_inferior = 10298.36
 excedente = salario - lim_inferior
 impuesto_marginal = excedente * .35
 isr = impuesto_marginal + 3327.42

#SALIDA
print("El el impuesto sobre la renta es de", isr)

