from at import *
from doc_string import *
def exibir_menu():
    print('-' * 25)
    print(f'{'':>10}Menu{'':>10}')
    print('-' * 25)
    print("[1]  - Cadastrar produto")
    print("[2]  - Atualizar estoque")
    print("[3]  - Buscar produto")
    print("[4]  - Remover produto")
    print("[5]  - Verificar produtos esgotados")
    print("[6]  - Filtrar produtos com baixa quantidade")
    print("[7]  - Atualização de preços")
    print("[8]  - Calcular valor total de estoque")
    print("[9]  - Calcular lucro presumido")
    print("[10] - Listar Produtos")
    print("[11] - Gerar Relatório")
    print("[12] - Consultar por quantidade")
    print("[13] - Exibir DocString")
    print("[0]  - Sair")
    print('-' * 25)


def entrar_opcao():
    while (True):
        limite = 13
        exibir_menu()
        opcao = int(input("Entre com a opção: "))
        if (opcao not in range(limite+1)):
            print("Erro: opção inválida")
        else:
            break
    return opcao
opcao = entrar_opcao()
while (opcao != 0):
    match (opcao):
        case 1: cadastrar_novos_produtos()
        case 2: atualizar_estoque()
        case 3: buscar_produtos()
        case 4: remover_produto()
        case 5: consulta_esgotados()
        case 6: filtro_baixa_quantidade()
        case 7: atualizar_preco()
        case 8: valor_total_estoque()
        case 9: valor_lucro_presumido()
        case 10: listar_produtos()
        case 11: gerar_relatorio()
        case 12: ordernar_quantidade()
        case 13: exibir_docstring()
        case _: print("Erro: opção inválida")
    opcao = entrar_opcao()
print("Saindo da aplicação")
