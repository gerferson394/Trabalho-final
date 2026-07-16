class Movimentacao:
    def __init__(self, valor, tipo, categoria, descricao, data):
        self.valor = float(valor)
        self.tipo = tipo            #pode ser receita ou despesa
        self.categoria = categoria
        self.descricao = descricao
        self.data = data

    def para_dicionario(self):
        """converte as informações do objeto num dicionário simples."""
        return {
            'valor': self.valor,
            'tipo': self.tipo,
            'categoria': self.categoria,
            'descricao': self.descricao,
            'data': self.data
        }
