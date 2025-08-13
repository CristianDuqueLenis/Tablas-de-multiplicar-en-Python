# -*- coding: utf-8 -*-
"""
=============================================================================== 
|calculadora simple - menu| =============================================================================== 

Este programa es una calculadora con un menu interactivo que permite realizar operaciones basicas como suma, resta
multiplicacion y division.

Autor: Cristian Duque
Fecha:13/08/2025
"""

# Crear un blucle infinito para mostrar el menu hasta que el usuario decida salir
while True:
    print ("\n===Menu de la calculadora")
    print ("1. sumar")
    print ("2. restar")
    print ("3. Multiplicar")
    print ("4. Dividir")
    print ("5. Salir")

    # Solicitar al usuario que elija una opcion del menu
    opcion = input ("seleccione una opcion 1-5_ ")

    # operaciones

    # opcion 1: Sumar
    if opcion =="1":
        num1=float(input("Ingrese el primer numero"))
        num2=float(input("Ingrese el segundo numero"))
        resultado = num1+num2
        print (f"la suma de {num1} y {num2} es {resultado}")