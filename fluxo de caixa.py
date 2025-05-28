from matplotlib import pyplot as plt


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Empresa:
    def __init__(self):
        self.produtos = {}
        self.estoque = {}
        self.caixa = 0
        self.lucro = 0
        self.historico_caixa = []
        self.historico_lucro = []
        self.historico_estoque = {}

    def adicionar_produto(self, produto, quantidade):
        if produto.nome in self.produtos:
            self.estoque[produto.nome] += quantidade
        else:
            self.produtos[produto.nome] = produto
            self.estoque[produto.nome] = quantidade
            self.historico_estoque[produto.nome] = []

    def vender_produto(self, nome_produto, quantidade):
        if nome_produto in self.estoque and self.estoque[nome_produto] >= quantidade:
            self.estoque[nome_produto] -= quantidade
            self.caixa += self.produtos[nome_produto].preco * quantidade
            self.lucro += self.produtos[nome_produto].preco * quantidade
            self.historico_caixa.append(self.caixa)
            self.historico_lucro.append(self.lucro)
            self.historico_estoque[nome_produto].append(self.estoque[nome_produto])
            print(f"Vendido {quantidade} unidades de {nome_produto} por R${self.produtos[nome_produto].preco * quantidade:.2f}")
        else:
            print("Estoque insuficiente")

    def comprar_produto(self, nome_produto, quantidade, preco_custo):
        if nome_produto in self.produtos:
            self.estoque[nome_produto] += quantidade
            self.caixa -= preco_custo * quantidade
            self.historico_caixa.append(self.caixa)
            self.historico_lucro.append(self.lucro)
            self.historico_estoque[nome_produto].append(self.estoque[nome_produto])
            print(f"Comprado {quantidade} unidades de {nome_produto} por R${preco_custo * quantidade:.2f}")
        else:
            print("Produto não existe")

    def mostrar_fluxo_caixa(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.historico_caixa, label='Caixa')
        plt.plot(self.historico_lucro, label='Lucro')
        plt.xlabel('Operação')
        plt.ylabel('Valor (R$)')
        plt.title('Fluxo de Caixa')
        plt.legend()
        plt.show()

    def mostrar_estoque(self):
        for produto, quantidade in self.estoque.items():
            plt.figure(figsize=(10, 6))
            plt.plot(self.historico_estoque[produto], label=produto)
            plt.xlabel('Operação')
            plt.ylabel('Quantidade')
            plt.title(f'Estoque de {produto}')
            plt.legend()
            plt.show()

# Criar empresa
empresa = Empresa()

# Criar produtos
produto1 = Produto("Produto A", 10)
produto2 = Produto("Produto B", 20)

# Adicionar produtos ao estoque
empresa.adicionar_produto(produto1, 100)
empresa.adicionar_produto(produto2, 50)

# Vender produtos
empresa.vender_produto("Produto A", 20)
empresa.vender_produto("Produto B", 10)
empresa.vender_produto("Produto A", 30)
empresa.vender_produto("Produto B", 20)

# Comprar produtos
empresa.comprar_produto("Produto A", 50, 5)
empresa.comprar_produto("Produto B", 30, 10)

# Mostrar fluxo de caixa
empresa.mostrar_fluxo_caixa()

# Mostrar estoque
empresa.mostrar_estoque()
