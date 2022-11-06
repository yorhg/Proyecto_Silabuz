# Inicio de Tarea_2
# Se utiliza la librería requests, instalar desde la consola con 'pip3 install requests'
import requests


def getPokemonGeneration():
    #url de api usados para la parte 1 del problema
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
        sub_response= requests.get(url_pokeapi_pokemon + pokemon)
        data_2 = sub_response.json()
        lista_habilidades = [habilidad["ability"]['name'] for habilidad in data_2['abilities']]
        print(pokemon)
        print(lista_habilidades)

#Se llama a la función getPokemonGeneration('generación_a_buscar')
getPokemonGeneration()

#Nota: Aún necesita ser añadido la imagen del Pokemon a la función

def getPokemonGeneration():

    #url de api usados para la parte 1 del problema
    #url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_sheps = 'https://pokeapi.co/api/v2/pokemon-shape/'
    sub_response= requests.get(url_pokeapi_sheps)
    data_2 = sub_response.json()
    #sugerir formas---
    lista_habilidades = [forma['name'] for forma in data_2['results']]
    print(lista_habilidades)
    forma = input("Ingrese la forma del pokemon: ")
    #se hace petición al api y se convierte los datos a .json
    response = requests.get(url_pokeapi_sheps + forma)   
    data_1 = response.json()
    #se usa comprehension para añadir elementos de los datos_1 a la lista_especies
    lista_especies = [especies['name'] for especies in data_1['pokemon_species']]
    print('Los pokemons que se son de forma', forma, 'són: \n ')  
    #se usa el segundo api, para añadir las habilidades de cada pokemon en lista_especies
    for pokemon in lista_especies:     
        print(pokemon)
        
getPokemonGeneration()