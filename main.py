#Entrada
print("Cálcular mi impuesto")
sala= float(input("Ingrese su salario mensual: "))

#operación1


#operación2
if sala <= 3644.94 and sala >= 0.01:
  ISR = 12.88+ ((sala - 0.01)*.1)
elif sala <= 7446.19 and sala >= 3644.95:
  ISR = 303.76+ ((sala - 3644.95)*.2)
elif sala <= 10298.35 and sala >= 7446.2:
  ISR = 1063.92+ ((sala - 7446.2)*.3)
elif sala >= 10298.36:
  ISR = 3327.42+ ((sala - 10298.36)*.35)

#salida
print(ISR)

