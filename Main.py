from abstract import QuartoSimples, QuartoLuxo
from funcionario_hospede import Hospede
from GRTM_TR import Gerente, Recepcionista, TecnicoManutencao, TecnicoRecepcao
import time 
import os

def wait_n_clear():
    input("Pressione Enter para continuar...")
    os.system('cls')  
    print("\nA Loading....")
    time.sleep(2)
    os.system('cls')

print("=== Sistema de Gestão do Hotel ===")
    
    # Criar quartos
quartos = []
for i in range(1, 6):
    quartos.append(QuartoSimples(i))
for i in range(6, 11):
    quartos.append(QuartoLuxo(i))
    
    # Criar funcionários
gerente = Gerente("Breno Sousa", 21, 12200)
recepcionista = Recepcionista("André Ventura", 30, 2500, "manhã")
tecnico_manutencao = TecnicoManutencao("António Costa", 35, 3000, "Elétrica")
tecnico_recepcao = TecnicoRecepcao("Ana Amiguinho", 28, 2800, "tarde", "Sistemas")
    
    # Lista de hóspedes
hospedes = []
    
print("\n=== Menu do Sistema ===")
while True:
    print("\n1. Registrar Hóspede")
    print("2. Listar Hóspedes")
    print("3. Listar Quartos")
    print("4. Relatório de Funcionários")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção (1-5): ")
    wait_n_clear()
    match opcao:
        case "1":
            print("\n=== Registro de Hóspede ===")
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            dias = int(input("Dias de estadia: "))
            wait_n_clear()
            print("\nQuartos disponíveis:")
            for quarto in quartos:
                if not quarto.ocupado:
                    print(quarto.mostrar_informacoes())
            wait_n_clear()
            try:
                num_quarto = int(input("Número do quarto: "))
                quarto_escolhido = None
                for quarto in quartos:
                    if quarto.numero == num_quarto and not quarto.ocupado:
                        quarto_escolhido = quarto
                        break
                    
                if quarto_escolhido:
                    hospede = Hospede(nome, idade, dias, quarto_escolhido)
                    recepcionista.registrar_hospede(hospede, hospedes)
                    print(f"Conta total: € {hospede.calcular_conta()}")
                else:
                    print("Quarto não disponível!")
                    wait_n_clear()
            except ValueError:
                print("Número de quarto inválido!")
            wait_n_clear()
        case "2":
            recepcionista.listar_hospedes(hospedes)
            wait_n_clear()
        case "3":
            print("\n=== Status dos Quartos ===")
            for quarto in quartos:
                print(quarto.mostrar_informacoes())
            wait_n_clear()
        case "4":
            funcionarios = [gerente, recepcionista, tecnico_manutencao, tecnico_recepcao]
            gerente.gerar_relatorio(funcionarios)
            wait_n_clear()
            
        case "5":
            print("Saindo...")
            time.sleep(2)
            os.system('cls')
            break
            
        case _:
            print("Opção inválida!")

