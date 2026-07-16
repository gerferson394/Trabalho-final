import os
from model.movimentacao import Movimentacao

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n-----------------------------------------")
    print("      ORGANIZADOR FINANCEIRO PESSOAL     ")
    print("-----------------------------------------")
    print(" 1. Ver todas as movimentações")
    print(" 2. Adicionar Receita (+)")
    print(" 3. Adicionar Despesa (-)")
    print(" 4. Ver Saldo e Gastos por Categoria")
    print(" 5. Remover uma movimentação")
    print(" 0. Sair")
    print("-----------------------------------------")

def exibir_lista(movimentacoes):
    if len(movimentacoes) == 0:
        print("\n[!] Nenhuma movimentação cadastrada ainda.")
        return

    print("\nNº  | TIPO     | VALOR       | CATEGORIA       | DESCRIÇÃO   | DATA")
    print("-" * 75)
    # O enumerate dá o índice (pos) e o item ao mesmo tempo
    for pos, m in enumerate(movimentacoes):
        
        print(f"{pos + 1:<3} | {m['tipo']:<8} | R$ {m['valor']:<9.2f} | {m['categoria']:<15} | {m['descricao']:<11} | {m['data']}")
    print("-" * 75)

def iniciar_interface_terminal(controller):
    while True:
        limpar_tela()
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            limpar_tela()
            print(">>> HISTÓRICO DE MOVIMENTAÇÕES:")
            exibir_lista(controller.obter_todas())
            input("\nPressione [ENTER] para voltar...")

        elif opcao in ["2", "3"]:
            limpar_tela()
            tipo = "Receita" if opcao == "2" else "Despesa"
            print(f">>> REGISTRAR {tipo.upper()}:\n")
            
            try:
                valor = float(input("Digite o valor (R$): ").replace(',', '.'))
                if valor <= 0:
                    print("\n[Erro] O valor deve ser maior que zero!")
                    input("\nPressione [ENTER] para voltar...")
                    continue
            except ValueError:
                print("\n[Erro] Digite um número válido!")
                input("\nPressione [ENTER] para voltar...")
                continue
                
            categoria = input("Categoria (Ex: Salário, Alimentação, Lazer): ").strip().capitalize()
            if not categoria:
                categoria = "Geral"
                
            descricao = input("Descrição: ").strip()
            if not descricao:
                descricao = "Sem descrição"
                
            data = input("Data (DD/MM/AAAA) [Deixe em branco para usar hoje]: ").strip()
            if not data:
                from datetime import datetime
                data = datetime.now().strftime("%d/%m/%Y")
            
            # 1. cria o objeto usando o Model
            nova_mov = Movimentacao(valor, tipo, categoria, descricao, data)
            # 2. envia para o Controller salvar
            controller.adicionar_movimentacao(nova_mov)
            
            print(f"\n[Sucesso] {tipo} salva com sucesso!")
            input("\nPressione [ENTER] para voltar...")

        elif opcao == "4":
            limpar_tela()
            print(">>> RESUMO FINANCEIRO:\n")
            saldo, receitas, despesas = controller.calcular_saldo()
            
            print(f"Total de Receitas (+) : R$ {receitas:.2f}")
            print(f"Total de Despesas (-) : R$ {despesas:.2f}")
            print(f"Saldo Atual           : R$ {saldo:.2f}")
            print("-" * 40)
            
            print("\n>>> GASTOS POR CATEGORIA:")
            gastos = controller.calcular_por_categoria()
            if gastos:
                for cat, total in gastos.items():
                    print(f" - {cat}: R$ {total:.2f}")
            else:
                print("Nenhuma despesa registrada.")
                
            input("\nPressione [ENTER] para voltar...")

        elif opcao == "5":
            limpar_tela()
            print(">>> REMOVER MOVIMENTAÇÃO:")
            lista = controller.obter_todas()
            exibir_lista(lista)
            
            if len(lista) > 0:
                try:
                    num = int(input("\nDigite o número (Nº) que deseja excluir: "))
                    
                    indice = num - 1
                    
                    if controller.remover_movimentacao(indice):
                        print("\n[Sucesso] Movimentação excluída com sucesso!")
                    else:
                        print("\n[!] Número inválido.")
                except ValueError:
                    print("\n[Erro] Digite um número inteiro válido!")
            input("\nPressione [ENTER] para voltar...")

        elif opcao == "0":
            print("\nSaindo... Obrigado por usar o Organizador Financeiro!")
            break
        else:
            print("\n[Erro] Opção inválida!")
            input("\nPressione [ENTER] para continuar...")
