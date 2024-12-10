from at import *

def exibir_docstring():
    """
    Exibe a docstring de uma função com base na escolha do usuário.
    """
    funcoes_disponiveis = {
        'processar': processar_produtos,
        'cadastrar': cadastrar_novos_produtos,
        'listar': listar_produtos,
        'ordenar': ordernar_quantidade,
        'buscar': buscar_produtos,
        'remover': remover_produto,
        'esgotados': consulta_esgotados,
        'filtro_quantidade': filtro_baixa_quantidade,
        'atualizar': atualizar_estoque,
        'valor_total': valor_total_estoque,
        'valor_presumido': valor_lucro_presumido,
        'relatorio': gerar_relatorio
    }
    
    escolha = input("Digite a docstring que vc quer exibir\n(processar, cadastrar, listar, ordenar, buscar, remover, esgotados, filtro_quantidade, atualizar, valor_total, valor_presumido, relatorio): ").strip()
    
    if escolha in funcoes_disponiveis:
        print(f"\nDocstring da função '{escolha}':\n")
        print(funcoes_disponiveis[escolha].__doc__)
    else:
        print("Função não encontrada. Tente novamente.")