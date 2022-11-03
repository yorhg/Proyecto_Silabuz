# Inicio de Tarea_2
# Se utiliza la librería requests, instalar desde la consola con 'pip3 install requests'
import requests


def getPokemonGeneration(generation_id):
    #url de api usados para la parte 1 del problema
    url_pokeapi_pokemon = 'https://pokeapi.co/api/v2/pokemon/'
    url_pokeapi_generations = 'https://pokeapi.co/api/v2/generation/'
    
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
getPokemonGeneration('2')

#Nota: Aún necesita ser añadido la imagen del Pokemon a la función