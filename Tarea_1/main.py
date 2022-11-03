import os
import time
import csv
import pandas as pd 


# Encabezado del archivo CVS
def encabezado():
    hederaCVS = ['ID', 'TITULO', 'GENERO', 'ISBN', 'EDITORAL','AUTORES']
    with open('Libros.cvs', 'w', newline='') as f_libro:
        dw = csv.DictWriter(f_libro, delimiter=',', fieldnames=hederaCVS)
        dw.writeheader()

    fileContent = pd.read_csv('Libros.cvs')
    fileContent


#Funcion Menu
def menu():
    print("-----Menu-----")
    print("Preciona una letra por cada opcion:")
    print("[1]Leer archivo de disco duro")

#Funcion para que elija una opcion (PRINCIPAL)
def run():
    encabezado()
    menu()

    command = input()
    command = command.upper()

    if command == '1':
        pass
    elif command == '2':
        pass
    elif command == '3':
        pass
    elif command == '4':
        pass
    elif command == '5':
        pass
    elif command == '6':
        pass
    elif command == '7':
        pass
    elif command == '8':
        pass
    elif command == '9':
        pass
    elif command == '10':
        pass
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')
        time.sleep(1)
        run()


#Func Agregar libro
def add_book():
    pass


#Func Inicializador del programa
if __name__ == "__main__":
    run()