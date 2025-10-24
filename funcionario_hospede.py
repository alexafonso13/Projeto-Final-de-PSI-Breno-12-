from abstract import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}"

class Hospede(Pessoa):
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self.dias_estadia = dias_estadia
        self._quarto = quarto
        if quarto:
            quarto.ocupado = True

    @property
    def quarto(self):
        return self._quarto

    @quarto.setter
    def quarto(self, quarto):
        if quarto is not None and not quarto.ocupado:
            self._quarto = quarto
            quarto.ocupado = True
            print("Quarto atribuído com sucesso!")
        else:
            print("Quarto inválido ou ocupado")

    def atribuir_quarto(self, quarto):
        if quarto is not None and not quarto.ocupado:
            self._quarto = quarto
            quarto.ocupado = True
            return f"Quarto {quarto.numero} atribuído ao hóspede {self.nome}"
        else:
            return "Quarto não disponível"

    def calcular_conta(self):
        if self._quarto is not None:
            return self.dias_estadia * self._quarto.preco_diaria
        return 0

    def mostrar_informacoes(self):
        quarto_info = f", Quarto: {self._quarto.numero}" if self._quarto else ", Sem quarto"
        return f"Nome: {self.nome}, Idade: {self.idade}{quarto_info}"
    def checkout(self):
        if self._quarto is not None:
            self._quarto.ocupado = False
            print(f"Checkout realizado para {self.nome}. Quarto {self._quarto.numero} liberado.")
            self._quarto = None
        else:
            print(f"{self.nome} não possui quarto atribuído.")

