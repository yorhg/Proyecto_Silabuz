# Inicio de Tarea_2
# Se utiliza la librería requests, instalar desde la consola con 'pip3 install requests'
import requests
import time
import os

def menu():
    print(
        ' -----------------------MENU-----------------------\n',
        ' -------------------LISTAR POKEMONES---------------\n',
        'Presiona un número para LISTAR por una opción \n',
        '[1]Listar pokemons por generación\n',
        '[2]Listar pokemons por forma\n',
        '[3]Listar pokemons por habilidad\n',
        '[4]Listar pokemons por habitat\n',
        '[5]Listar pokemons por tipo\n',
        'Presiona S para salir\n'
        )


def run():
    menu()

    command = input('Selecciona una opción\n->')
    command = command.upper()

    if command == '1':
        getPokemonGeneration()

    elif command == '2':
        getPokemonSheps()

    elif command == '3':
        getPokemonAbility()

    elif command == '4':
        getPokemonHabitat()

    elif command == '5':
        getPokemonType()

    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido\n')
        time.sleep(1)
        run()

def salir():
     while True:
        salir = input("\nEscriba X para salir: ")
        if salir == "x":
            run()
            return 

def getPokemonGeneration():
    
    url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_generations = 'https://pokeapi.co/api/v2/generation/'
    
    generation_id = input("Ingrese que generaión listar: ")
    #se hace petición al api y se convierte los datos a .json
    response = requests.get(url_pokeapi_generations + generation_id)   
    data_1 = response.json()
    
    #se usa comprehension para añadir elementos de los datos_1 a la lista_especies
    lista_especies = [especies['name'] for especies in data_1['pokemon_species']]
    print('Los pokemons que se encuentran el la generación', generation_id, 'són: \n ')
    
    #se usa el segundo api, para añadir las habilidades de cada pokemon en lista_especies
    for pokemon in lista_especies:
        try:
            sub_response= requests.get(url_pokeapi_pokemon + pokemon)
            data_2 = sub_response.json()
            lista_habilidades = [habilidad["ability"]['name'] for habilidad in data_2['abilities']]
            imagenes= data_2['sprites']['front_default']
            print(pokemon)
            print(lista_habilidades)
            print(imagenes)
        except:
            pass
    salir()
   
        

#Se llama a la función getPokemonGeneration('generación_a_buscar')
#getPokemonGeneration()

#

def getPokemonSheps():


    
    url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_sheps = 'https://pokeapi.co/api/v2/pokemon-shape/'
    sub_response= requests.get(url_pokeapi_sheps)
    data_1 = sub_response.json()
    #sugerir formas---
    lista_formas = [forma['name'] for forma in data_1['results']]
    print(lista_formas)
    forma = input("Ingrese la forma del pokemon: ")
    #se hace petición al api y se convierte los datos a .json
    response = requests.get(url_pokeapi_sheps + forma)   
    data_2 = response.json()
    #se usa comprehension para añadir elementos de los datos_1 a la lista_especies
    lista_especies = [especies['name'] for especies in data_2['pokemon_species']]
    print('Los pokemons que se son de forma', forma, 'són: \n ')  
    #se usa el segundo api, para añadir las habilidades de cada pokemon en lista_especies
    for pokemon in lista_especies:     
        try:
            sub_responser= requests.get(url_pokeapi_pokemon + pokemon)
            data_3 = sub_responser.json()
            Habilidad = [habilidad["ability"]['name'] for habilidad in data_3['abilities']]
            imagenes= data_3['sprites']['front_default']
            print(pokemon)
            print(Habilidad)
            print(imagenes)
        except:
            pass
    salir()
  

      
#getPokemonGeneration()

def getPokemonAbility():

    
    url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_ability = 'https://pokeapi.co/api/v2/ability/'
    sub_response= requests.get(url_pokeapi_ability)
    data_2 = sub_response.json()
    #sugerir formas---
    lista_habilidades = [forma['name'] for forma in data_2['results']]
    print(lista_habilidades)
    Habilidad = input("Ingrese la Habilidad del pokemon: ")
    #se hace petición al api y se convierte los datos a .json
    response = requests.get(url_pokeapi_ability + Habilidad)   
    data_1 = response.json()
    #se usa comprehension para añadir elementos de los datos_1 a la lista_especies
    lista_especies = [especies['pokemon']['name'] for especies in data_1['pokemon']]
    print('Los pokemons que se son de habilidad', Habilidad, 'són: \n ')  
    #se usa el segundo api, para añadir las habilidades de cada pokemon en lista_especies
    for pokemon in lista_especies:  
        try:
            sub_response= requests.get(url_pokeapi_pokemon + pokemon)
            data_3 = sub_response.json()
            Habilidad = [habilidad["ability"]['name'] for habilidad in data_3['abilities']]
            imagenes= data_3['sprites']['front_default']
            print(pokemon)
            print(Habilidad)
            print(imagenes)
        except:
            pass
        
    salir()
#getPokemonAbility()

def getPokemonHabitat():

    url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_habitad = 'https://pokeapi.co/api/v2/pokemon-habitat/'
    sub_response= requests.get(url_pokeapi_habitad)
    data_2 = sub_response.json()
    #sugerir formas---
    lista_hbitads = [forma['name'] for forma in data_2['results']]
    print(lista_hbitads)
    Habitad = input("Ingrese el habitad del pokemon: ")
    #se hace petición al api y se convierte los datos a .json
    response = requests.get(url_pokeapi_habitad + Habitad)   
    data_1 = response.json()
    #se usa comprehension para añadir elementos de los datos_1 a la lista_especies
    lista_especies = [especies['name'] for especies in data_1['pokemon_species']]
    print('Los pokemons que se son de Habitad', Habitad, 'són: \n ')  
    #se usa el segundo api, para añadir las habilidades de cada pokemon en lista_especies
    for pokemon in lista_especies:     
        try:
            sub_response= requests.get(url_pokeapi_pokemon + pokemon)
            data_3 = sub_response.json()
            Habilidad = [habilidad["ability"]['name'] for habilidad in data_3['abilities']]
            imagenes= data_3['sprites']['front_default']
            print(pokemon)
            print(Habilidad)
            print(imagenes)
        except:
            pass
        
    salir()
#getPokemonHabitat()

def getPokemonType():

    url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_tipo = 'https://pokeapi.co/api/v2/type/'
    sub_response= requests.get(url_pokeapi_tipo)
    data_2 = sub_response.json()
    #sugerir formas---
    lista_tipos = [forma['name'] for forma in data_2['results']]
    print(lista_tipos)
    tipo = input("Ingrese el tipo de pokemon: ")
    #se hace petición al api y se convierte los datos a .json
    response = requests.get(url_pokeapi_tipo + tipo)   
    data_1 = response.json()
    #se usa comprehension para añadir elementos de los datos_1 a la lista_especies
    lista_especies = [especies['pokemon']['name'] for especies in data_1['pokemon']]
    print('Los pokemons que se son de tipo', tipo, 'són: \n ')  
    #se usa el segundo api, para añadir las habilidades de cada pokemon en lista_especies
    for pokemon in lista_especies:    
        try:
            sub_response= requests.get(url_pokeapi_pokemon + pokemon)
            data_3 = sub_response.json()
            Habilidad = [habilidad["ability"]['name'] for habilidad in data_3['abilities']]
            imagenes= data_3['sprites']['front_default']
            print(pokemon)
            print(Habilidad)
            print(imagenes)
        except:
            pass
        
    salir()
#getPokemonType()

run()