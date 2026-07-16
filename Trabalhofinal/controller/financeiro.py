import json
import os

class GerenciadorFinanceiro:
    def __init__(self):
        self.arquivo = "dados_financeiros.json"
        self.movimentacoes = self.carregar_dados()

    def carregar_dados(self):
        """Abre o arquivo JSON. Se não existir, retorna uma lista vazia."""
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            # carrega a lista de dicionários 
            return json.load(f)

    def salvar_dados(self):
        """Salva a lista de dicionários no arquivo JSON."""
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.movimentacoes, f, indent=4, ensure_ascii=False)

    def adicionar_movimentacao(self, objeto_movimentacao):
        """Recebe o objeto do Model, transforma em dicionário e adiciona à lista."""
        dicionario = objeto_movimentacao.para_dicionario()
        self.movimentacoes.append(dicionario)
        self.salvar_dados()

    def obter_todas(self):
        """Retorna a lista completa de movimentações."""
        return self.movimentacoes

    def remover_movimentacao(self, indice):
        """Remove um item da lista usando a sua posição (índice)."""
        if 0 <= indice < len(self.movimentacoes):
            self.movimentacoes.pop(indice)
            self.salvar_dados()
            return True
        return False

    def calcular_saldo(self):
        """Calcula o saldo usando um loop 'for' bem simples e direto."""
        total_receitas = 0.0
        total_despesas = 0.0

        for m in self.movimentacoes:
            if m['tipo'] == "Receita":
                total_receitas += m['valor']
            elif m['tipo'] == "Despesa":
                total_despesas += m['valor']

        saldo = total_receitas - total_despesas
        return saldo, total_receitas, total_despesas

    def calcular_por_categoria(self):
        """Agrupa os gastos de cada categoria usando um dicionário."""
        categorias = {}
        for m in self.movimentacoes:
            if m['tipo'] == "Despesa":
                cat = m['categoria']
                valor = m['valor']
                # Se a categoria já existe no dicionário, soma. Se não, cria com o valor atual.
                if cat in categorias:
                    categorias[cat] += valor
                else:
                    categorias[cat] = valor
        return categorias
