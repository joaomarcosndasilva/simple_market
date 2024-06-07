from typing import List, Dict
from time import sleep
import os
from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('====================================================')
    print('=================Bem Vindo(a)=======================')
    print('=================Brutus Market======================')
    print('====================================================')
    print('Selecione uma opção abaixo:')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Comprar Produto')
    print('4 - Visualizar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair')
    opcao: int = int(input('Digite a opção desejada: '))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre...')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_produto() -> None:
    """Este menu cadastra os produtos. pedindo nome e preço e joga para lista produtos"""
    print('Cadastro de Produto: ')
    print('=====================')

    nome: str = input('Informe o nome do produto: ').title()
    preco: float = input('Informe o preço do produto: ')

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

def listar_produtos() -> None:
    """Faz um for para litar os produtos formatados"""
    if len(produtos) > 0:
        print('Listagem de produtos:')
        print('--------------------------------------')
        for produto in produtos:
            print(produto)
            print('----------------------------------')
            sleep(1)
        sleep(5)
        os.system('cls')
        menu()
    else:
        print('Ainda não existem produtos cadastrados')
        sleep(2)
        os.system('cls')
        menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print("Informe o código do produto que deseja adicionar no carrinho: ")
        print('====================Produtos disponíveis======================')
        for produto in produtos:
            print(produto)
            print('------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('Digite aqui o código para adicionar ao carrinho: '))

        produto: Produto = pega_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant +1
                        print(f'O produto {produto.nome} possui agora {quant +1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionando no carrinho')
                    sleep(2)
                    menu()

            else:
                item = {produto:1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado')
            sleep(2)
            menu()
    else:
        print('Ainda não existe produtos para comprar')
        sleep(2)
        os.system('cls')
        menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')
        for item in carrinho:
            for dados in item.items():
                print('-----------------------------------')
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------------------')
                sleep(1)
        os.system('pause')
        menu()
    else:
        print('Ainda não existem produtos no carrinho!')
        sleep(2)
        os.system('cls')
        menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho:')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += float(dados[0].preco) * int(dados[1])
                print('----------------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre')
        carrinho.clear()
        sleep(5)
    else:
        print("Ainda não existe produtos no carrinho!")
        sleep(2)
        os.system('cls')
        menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None
    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
