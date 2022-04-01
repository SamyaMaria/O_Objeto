class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property  # esse método representa uma propriedade(sem precisar colar os parênteses)
    def nome(self): # chama o get sem precisar especificar
        return  self.__nome.title()

    @nome.setter # para esse atributo esse método será o setters: criar
    def nome(self, nome):
        self.__nome = nome

