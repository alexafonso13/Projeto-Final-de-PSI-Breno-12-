from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválida - não pode ser negativa")
        else:
            self._idade = nova_idade

    @abstractmethod
    def mostrar_informacoes(self):
        pass

class Quarto(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self._preco_diaria = preco_diaria
        self.ocupado = False

    @property
    def ocupado(self):
        return self._ocupado

    @ocupado.setter
    def ocupado(self, status):
        self._ocupado = status

    @property
    def preco_diaria(self):
        return self._preco_diaria

    @preco_diaria.setter
    def preco_diaria(self, preco):
        if preco < 0:
            print("Preço não pode ser negativo")
        else:
            self._preco_diaria = preco

    def mostrar_informacoes(self):
        status = "Ocupado" if self.ocupado else "Livre"
        return f"Quarto {self.numero} - {self.tipo} - € {self.preco_diaria}/dia - {status}"

class QuartoSimples(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Simples", 50.0)

class QuartoLuxo(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Luxo", 150.0)
