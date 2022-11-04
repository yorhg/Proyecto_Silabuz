class Libro:
    
    def __init__(self,id, titulo, genero, ISBN, editorial, autores):
       self._id = id 
       self._titulo = titulo
       self._genero = genero
       self._ISBN = ISBN
       self._editorial = editorial
       self._autores = autores
    
    def __str__(self) -> str:
        return f"Id= {self._id}, Titulo = {self._titulo}, Genero = {self._genero}, ISBN= {self._ISBN}, Editorial= {self.editorial}, Autores= {self._autores}"

    @property
    def get_id(self):
        return self._id
        
    @get_id.setter
    def set_id(self, id):
        self._id = id

    @property
    def get_titulo(self):
        return self._titulo

    @get_titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def ISBN(self):
        return self._ISBN

    @ISBN.setter
    def ISBN(self, ISBN):
        self._ISBN = ISBN

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def autores(self):
        return self._autores

    @autores.setter
    def autores(self, autores):
        self._autores = autores