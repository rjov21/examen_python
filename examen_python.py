# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 11:08:14 2021

@author: DIOS BENDITO
"""
# ejercicio 1
kilos = int(input('ingrese la cantidad de kilos comprados: '))
valor = int(input('ingrese el valor del kilo: '))
if kilos < 2:
    desccuento = 0
elif kilos > 2 and kilos < 5:
    descuento = (kilos * valor) * 0.1
elif kilos > 5 and kilos < 10:
    descuento = (kilos * valor) * 0.15
else:
    descuento = (kilos * valor) * 0.2
valor_final = (kilos * valor) - descuento
print(f'el valor final a pagar es: {valor_final}')

# ejercicio 2
clave = input('ingrese la clave: ')
valor = int(input('ingrese el valor de abanico: '))
if clave == '010':
    descuento = valor * 0.2
elif clave == '020':
    descuento = valor * 0.4
elif clave == '030':
    descuento = valor * 0.55
elif clave == '040':
    descuento = valor * 0.75
valor_final = valor - descuento
print(f'el valor final a pagar es: {valor_final}')
