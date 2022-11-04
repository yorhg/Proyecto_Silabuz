class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
       self.__id = id 
       self.__titulo = titulo
       self.__genero = genero
       self.__ISBN = ISBN
       self.__editorial = editorial
       self.__autores = autores

@property
def id(self):
    return self.__id

@id.setter
def id(self, id):
    self.__id = id

@property
def titulo(self):
    return self.__titulo

@titulo.setter
def titulo(self, titulo):
    self.__titulo = titulo

@property
def genero(self):
    return self.__genero

@genero.setter
def genero(self, genero):
    self.__genero = genero

@property
def ISBN(self):
    return self.__ISBN

@ISBN.setter
def ISBN(self, ISBN):
    self.__ISBN = ISBN

@property
def editorial(self):
    return self.__editorial

@editorial.setter
def editorial(self, editorial):
    self.__editorial = editorial

@property
def autores(self):
    return self.__autores

@autores.setter
def autores(self, autores):
    self.__autores = autores