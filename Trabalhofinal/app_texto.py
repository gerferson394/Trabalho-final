from controller.financeiro import GerenciadorFinanceiro
from view_texto.menu import iniciar_interface_terminal

if __name__ == "__main__":
    # Inicializa o controlador (que carrega o arquivo JSON)
    controlador = GerenciadorFinanceiro()
    
    # Inicia a interface textual e entrega o controlador para ela
    iniciar_interface_terminal(controlador)