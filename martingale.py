# -*- coding: utf-8 -*-

##################################
# MARTINGALA / MARTINGALE SYSTEM #
##################################
#
# Programa que calcula el coste de una martingala.
# Para saber qué es la Martingala o Martingale System
# acudid a Google, os lo explicará mejor que yo :)
#
# Program to calculate the cost of the Martingale System.
# What's the Martingale System? Google will explain it
# better than I could do :)
#
# Personalmente no creo que la Martingala sea un método
# fiable. Difrutad del juego con responsabilidad.
# I personally do not believe in the Martingale System
# as a safe method. Enjoy gambling with resposability.
#
# Creado por / Created by: @miancolrin

def doblar(aDoblar):
    return(aDoblar * 2)

def sumar(doblado, total):
    return(total + doblado)

inicial = input("Valor de la primera apuesta / first stake: ")
n = input("¿Cuantas veces ha doblado? / How many times?: ")

total = 0
doble = 0

for x in range(n):
    if x == 0:
        total = sumar(inicial, 0)
    else:
        inicial = inicial * 2
        total = sumar(total, inicial)
		
print "Valor de última apuesta / Last bet value: ", total
