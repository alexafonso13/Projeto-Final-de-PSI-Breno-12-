from funcionario_hospede import Funcionario, Hospede

class Recepcionista(Funcionario):
    def __init__(self, nome, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self._turno = turno

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, turno):
        turnos_validos = ["manhã", "tarde", "noite"]
        if turno.lower() in turnos_validos:
            self._turno = turno
        else:
            print("Turno inválido. Use: manhã, tarde ou noite")

    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Turno: {self.turno}"

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)
        print(f"Hóspede {hospede.nome} registrado com sucesso!")

    def listar_hospedes(self, lista_hospedes):
        print("=== Lista de Hóspedes ===")
        for hospede in lista_hospedes:
            print(hospede.mostrar_informacoes())

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)
        self.bonus = 0.1  # 10% de bônus

    def mostrar_informacoes(self):
        salario_total = self.salario + (self.salario * self.bonus)
        return f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Bônus: {self.bonus*100}%, Total: {salario_total}"

    def gerar_relatorio(self, funcionarios):
        print("=== Relatório de Funcionários ===")
        for funcionario in funcionarios:
            print(funcionario.mostrar_informacoes())

class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        super().__init__(nome, idade, salario)
        self._especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Especialidade: {self.especialidade}"
    def registrar_reparo(self, descricao):
        print(f"Reparo registrado: {descricao} - Técnico: {self.nome}")

class TecnicoRecepcao(TecnicoManutencao, Recepcionista):
    def __init__(self, nome, idade, salario, turno, especialidade):
        Funcionario.__init__(self, nome, idade, salario)
        self._turno = turno
        self._especialidade = especialidade

    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Turno: {self.turno}, Especialidade: {self.especialidade}"

    def registrar_hospede(self, hospede, lista_hospedes):
        super().registrar_hospede(hospede, lista_hospedes)

    def registrar_reparo(self, descricao):
        super().registrar_reparo(descricao)
