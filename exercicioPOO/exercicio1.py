class ProdutoEmEstoque:
    def __init__(self, produto="", quantidade=0, preco=0.00):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def add_produto(self, produto, quantidade):
        produto.quantidade += quantidade

    def venda_produto(self, produto, quantidade):
        produto.quantidade -= quantidade

class Cliente:
    def __init__(self, nome="", idade=0, sexo=""):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
class Item:
    def __init__(self,produto, quantidade):
        self.produto= produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, cliente , produtos=[], form_pgto=""):
        self.produtos = produtos
        self.cliente = cliente
        self.form_pgto = form_pgto

    def baixar_estoque(self):
        for i in range(len(self.produtos)):
            produto = self.produtos[i]
            ProdutoEmEstoque.venda_produto(produto, 1)

    def valor_pedido(self):
        valor_total = 0
        for i in range(len(self.produtos)):
            produto = self.produtos[i]
            valor_total += produto.produto.preco

def main():
    hamburguer = ProdutoEmEstoque("Hamburguer",5,35.5)
    pizza = ProdutoEmEstoque("Pizza",8,49.5)
    macarrao = ProdutoEmEstoque("Macarrão",10,7.9)

    comidas = [hamburguer, pizza, macarrao]
    estoque = ProdutoEmEstoque(comidas)
    estoque.add_produto("hamburguer",2)

    carlos = Cliente("Carlos",72,"homem")

    ham3= Item(hamburguer,3)
    piz2= Item(pizza,2)
    mac5= Item(macarrao,5)
    lista_comidas=[ham3,piz2,mac5]

    pedido= Pedido(lista_comidas,carlos,"Dinheiro")

if __name__ == '__main__':
    main()