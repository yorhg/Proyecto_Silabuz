import pandas as pd
import csv
import time

#Opciones del menú

def menu():
    print(
        ' -----------------------MENU-----------------------\n',
        'Presiona un número para seleccionar una opción \n',
        '[1]Leer archivo de disco duro\n',
        '[2]Listar libros\n',
        '[3]Agregar libro\n',
        '[4]Eliminar libro\n',
        '[5]Buscar libro por ISBN o por título\n',
        '[6]Ordenar libros por título\n',
        '[7]Buscar libros por autor, editorial o género\n', 
        '[8]Buscar libros por número de autores\n',
        '[9]Editar o actualizar datos de un libro\n',
        '[6]Guardar libros en archivo de disco duro\n'
        )

def Opcion_1():
    archivo = input('Ingresar nombre del archivo(incluyendo ".csv") o ruta de acceso absoluta:\n->')
    results = []
    with open(archivo) as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
        print(results)

def Opcion_2():
    print('-----------------------LIBROS-----------------------\n')
    datos=pd.read_csv('Libros.csv', header=0)
    print(datos)

def Opcion_3():

    bibliotecaList = []
    with open("Libros.csv", "a", newline='') as f:
        ids = {}
        ids['id'] = input('introdusca el ID del libro a agregar:\n-> ')
        ids['titulo'] = input('introdusca el titulo del libro a agregar:\n-> ')
        ids['genero'] = input('introdusca el género del libro a agregar:\n-> ')
        ids['ISBN'] = input('introdusca el ISBN del libro a agregar:\n-> ')
        ids['editorial'] = input('introdusca el editorial del libro a agregar:\n-> ')
        ids['autor(es)'] = input('introdusca el autore(es) del libro a agregar:\n-> ')
        bibliotecaList.append(ids)
        w = csv.DictWriter(f, bibliotecaList[0].keys())
        for a in bibliotecaList:
            w.writerow(a)
        print(bibliotecaList)

def Opcion_6():
    datos=pd.read_csv('Libros.csv', header=0)
    print(datos.sort_values(by='titulo'))


def run():
    #encabezado()
    menu()

    command = input('Selecciona una opción\n->')
    command = command.upper()

    if command == '1':
        Opcion_1()

    elif command == '2':
        Opcion_2()

    elif command == '3':
        Opcion_3()

    elif command == '4':
        pass
    elif command == '5':
        pass
    elif command == '6':
        Opcion_6()

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
        print('Comando inválido\n')
        time.sleep(1)
        run()

run()