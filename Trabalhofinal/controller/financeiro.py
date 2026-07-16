import json
import os

class GerenciadorFinanceiro:
    def __init__(self):
        self.arquivo = "dados_financeiros.json"
        self.movimentacoes = self.carregar_dados()

    def carregar_dados(self):
        """abre o  json. se não tiver, retorna uma lista vazia"""
        if not os.path.exists(self.arquivo):
            return []
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            # carrega a lista de dicionários 
            return json.load(f)

    def salvar_dados(self):
        """salva a lista de dicionários no arquivo json"""
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.movimentacoes, f, indent=4, ensure_ascii=False)

    def adicionar_movimentacao(self, objeto_movimentacao):

        dicionario = objeto_movimentacao.para_dicionario()
        self.movimentacoes.append(dicionario)
        self.salvar_dados()

    def obter_todas(self):
        """retorna a lista completa de movimentações"""
        return self.movimentacoes

    def remover_movimentacao(self, indice):
        """remove um item da lista"""
        if 0 <= indice < len(self.movimentacoes):
            self.movimentacoes.pop(indice)
            self.salvar_dados()
            return True
        return False

    def calcular_saldo(self):
        """calcula o saldo usando um loop"""
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
        """agrupa os gastos de cada categoria"""
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
