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
        ids['titulo'] = input('introdusca el titulo del libro a agregar(No usar tíldes):\n-> ')
        ids['genero'] = input('introdusca el género del libro a agregar(No usar tíldes):\n-> ')
        ids['ISBN'] = input('introdusca el ISBN del libro a agregar:\n-> ')
        ids['editorial'] = input('introdusca el editorial del libro a agregar(No usar tíldes):\n-> ')
        ids['autor(es)'] = input('introdusca el autore(es) del libro a agregar(No usar tíldes):\n-> ')
        bibliotecaList.append(ids)
        w = csv.DictWriter(f, bibliotecaList[0].keys())
        for a in bibliotecaList:
            w.writerow(a)
        print(bibliotecaList)

def Opcion_5():

    datos = pd.read_csv('Libros.csv')
    df = pd.DataFrame(datos)
    
    print('Seleccionar una opción:\n[1] Buscar por ISBN\n[2] Buscar por Titulo')
    selección = input('Ingresar opción:\n->')

    if selección == '1':
        Buscador_isbn = input('Escribe el ISBN del libro a Buscar:\n->')
        respuesta = df[df['ISBN'] == Buscador_isbn]
        print(respuesta)
    elif selección == '2':
        Buscador_tit = input('Escriba el titulo del libro a buscar:\n->')
        respuesta = df[df['titulo'] == Buscador_tit]
        print(respuesta)
    else:
        print('Opción inválida')
        time.sleep(1)
        Opcion_5()

def Opcion_6():
    datos=pd.read_csv('Libros.csv', header=0)
    print(datos.sort_values(by='titulo'))


def Opcion_7():

    datos = pd.read_csv('Libros.csv')
    df = pd.DataFrame(datos)
    
    print('Seleccionar una opción:\n[1] Buscar por Autor\n[2] Buscar por Editorial\n[3] Buscar por Género')
    selección = input('Ingresar opción:\n->')

    if selección == '1':
        Buscador_isbn = input('Escribe el Autor del libro a Buscar:\n->')
        respuesta = df[df['autor(es)'] == Buscador_isbn]
        print(respuesta)
    elif selección == '2':
        Buscador_tit = input('Escriba el Editorial del libro a buscar:\n->')
        respuesta = df[df['editorial'] == Buscador_tit]
        print(respuesta)
    elif selección == '3':
        Buscador_tit = input('Escriba el Género del libro a buscar:\n->')
        respuesta = df[df['genero'] == Buscador_tit]
        print(respuesta)
    else:
        print('Opción inválida')
        time.sleep(1)
        Opcion_7()


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
        Opcion_5()

    elif command == '6':
        Opcion_6()

    elif command == '7':
        Opcion_7()
        
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