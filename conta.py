
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo Objeto ... {}" .format(self))
        self.texto = ''
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def le_entrada(self):
        self.texto = input()

    def exibe_saida(self):
        print(self.texto)

    def extrato(self):
        print("Saldo de {} do titular {}." .format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("o valor {} passou do limite." .format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def nome(self):  # getters: apenas devolve
        return self.__nome

    @property
    def titular(self):  # getters: apenas devolve
        return self.__titular

    @property
    def saldo(self):  # getters: apenas devolve
        return self.__saldo

    @property
    def limite(self): # getters: apenas devolve
        return self.__limite

    @limite.setter
    def limite(self, limite): # setters: cria
        self.__limite = limite

    @staticmethod # método estático, não precisa de um objeto para chamar a método
    def cogigo_banco():
        return "001"