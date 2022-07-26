#MODULO PRINCIPAL
import calculadora_aritmetica as calc
import menu_inicio as menu
import os

ver_menu = ''  #se le da un valor a la variable (declararla) para poder utilizarla.

#while ejecuta las instrucciones mientras la condición se cumpla (comparación)
while (ver_menu.lower() != 's'):
    ver_menu = menu.menu_operaciones()
    print(ver_menu)
    if ver_menu ==str(1):
        numero_1 = float(input('Ingrese el primer número: '))
        numero_2 = float(input('Ingrese el segundo número: '))
        suma = calc.sumar_numeros(numero_1, numero_2)
        print('La suma es igual:', suma)
    elif ver_menu ==str(2):
      numero_1 = float(input('Ingrese el primer número: '))
      numero_2 = float(input('Ingrese el segundo número: '))
      resta = calc.restar_numeros(numero_1, numero_2)
      print('La resta es igual:', resta)
    elif ver_menu ==str(3):
      numero_1 = float(input('Ingrese el primer número: '))
      numero_2 = float(input('Ingrese el segundo número: '))
      multiplicacion = calc.multiplicar_numeros(numero_1, numero_2)
      print('La multiplicación es igual:', multiplicacion)
    elif ver_menu ==str(4):
      numero_1 = float(input('Ingrese el primer número: '))
      numero_2 = float(input('Ingrese el segundo número: '))
      division = calc.dividir_numeros(numero_1, numero_2)
      print('La división es igual:', division)
      
    input('para continuar oprima cualquier tecla:')
    os.system('clear')  #limpiar la pantalla
