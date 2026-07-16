from controller.financeiro import GerenciadorFinanceiro
from view_texto.menu import iniciar_interface_terminal

if __name__ == "__main__":
    # inicia o controlador (que carrega o arquivo JSON)
    controlador = GerenciadorFinanceiro()
    
    # inicia a interface textual 
    iniciar_interface_terminal(controlador)
