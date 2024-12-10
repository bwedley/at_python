estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00#Mouse Logitech;203;50;70.00;150.00#Mouse Razer;204;40;120.00;250.00#Monitor Samsung;205;10;800.00;1200.00#Monitor LG;206;8;750.00;1150.00#Teclado Mecânico Corsair;207;30;180.00;300.00#Teclado Mecânico Razer;208;25;200.00;350.00#Impressora HP;209;5;400.00;650.00#Impressora Epson;210;3;450.00;700.00#Monitor Dell;211;12;850.00;1250.00#Monitor AOC;212;7;700.00;1100.00"
estoque = []

'''
2. Inserção inicial de estoque: O aluno deve copiar e colar o seguinte bloco de código como string no início do programa para definir o estoque inicial.
O sistema deve processar essa string e converter os dados em uma lista de dicionários:
'''
def processar_produtos(produto):
    '''
    Processa uma string contendo informações de produtos, convertendo em um dicionário

    Args:
        produto (str): Uma string contendo dados separados por ponto e vírgula (;).
        Formato esperado: "descrição; código; quantidade; custo; preço de venda".

    Returns:
        dict: Um dicionário com as chaves:
            - 'descrição' (str): A descrição do produto.
            - 'código' (int): O código do produto.
            - 'quantidade' (int): A quantidade disponível em estoque.
            - 'custo' (float): O custo de produção unitária do produto.
            - 'preço de venda' (float): O preço do produto.
    '''
    produtos = produto.split(';')
    return {
            'descrição': produtos[0],
            'código': int(produtos[1]),
            'quantidade': int(produtos[2]),
            'custo': float(produtos[3]),
            'preço de venda': float(produtos[4])
        }
estoque = list(map(processar_produtos, estoque_inicial.split('#')))
#print(estoque)
'''
1. Cadastro de produtos: Implemente uma função que permita o cadastro de novos produtos. Cada produto deve conter os seguintes atributos:
descrição, código, quantidade em estoque, custo do item e preço de venda por item. O código deve ser um identificador único do produto.
'''

def identificador_unico(codigo):
    '''
    Verifica se um código já existe na lista.

    Args:
        codigo (int): O código a ser verificado

    Returns:
        bool: True se o código já existir, caso contrário, False.
    '''
    return any(produto['código'] == codigo for produto in estoque)

def cadastrar_novos_produtos():
    '''
    Cadastra um novo produto no estoque com informações fornecidas pelo usuário.

    O programa solicita ao usuário informaçõs como descrição, código, quantidade em estoque, custo de produção e preço de venda.
    A função verifica se o código do produto é único antes de realizar a adição ao estoque. Caso contrário, uma mensagem de erro é exibida.
    A função também conta com tratamento de entradas inválidas via try except.

    Args:
        None
    
    Returns:
        None
    '''
    try:
        desc = input("Informe a descrição do produto: ")
        cod = int(input("Informe o código do produto: "))
        if identificador_unico(cod):
            print(f"Código {cod} já existente no banco")
            return
        qtde = int(input("Informe a quantidade de estoque do produto: "))
        custo = float(input("Informe o preço de custo do produto: "))
        preco = float(input("Informe o preço de venda do produto: "))
        novo_produto = {
            "descrição": desc,
            "código": cod,
            "quantidade": qtde,
            "custo": custo,
            "preço de venda": preco
        }
    except ValueError:
        print("Entradas inválidas")
        return

    estoque.append(novo_produto)
    print(f"Produto {desc} cadastrado com sucesso!")
    print(estoque)
'''
3. Listagem de produtos: Desenvolva uma função que exiba uma lista de todos os produtos cadastrados, incluindo a descrição,
código, quantidade, custo e preço de venda de cada item.
'''
def listar_produtos():
    '''
    Lista todos os produtos cadastrados no estoque com informações formatadas.

    A função exibe os produtos em uma tabela que incluem descrição, código, quantidade, custo e preço de venda.
    Caso o estoque esteja vazio uma mensagem será exibida informado o que não existem produtos cadastrados.

    Args: 
        None

    Returns:
        None
    '''
    if not estoque:
        print("Nenhum produto cadastrado no estoque.")
        return

    print("Produtos cadastrados no estoque:")
    print("-" * 80)
    print(f"{'Descrição':<25} {'Código':<10} {'Quantidade':<15} {'Custo':<10} {'Preço de Venda':<15}")
    print("-" * 80)

    for produto in estoque:
        print(f"{produto['descrição']:<25}| {produto['código']:<10}| {produto['quantidade']:<14}| "
              f"{produto['custo']:<8.2f}| {produto['preço de venda']:<15.2f}|")
    
    print("-" * 80)

'''
4. Ordenação de produtos por quantidade: Desenvolva uma função que permita ao usuário ordenar os produtos pela
quantidade disponível no estoque, exibindo a lista em ordem crescente ou decrescente.
'''
def ordernar_quantidade():
    '''
    Ordena e lista os produtos com base na quantidade por ordem escolhida pelo usuário, podendo ser em ordem crescente ou decrescente

    A função organiza os produtos ordenadamente com base na quantidade existente em estoque e exibe as informações tratadas na tela

    Args:
        None

    Returns:
        None
    '''
    ordem = input("Você deseja listar por ordem 'crescente' ou 'decrescente'? ")
    if not estoque:
        print("Nenhum produto cadastrado no estoque.")
        return
    if ordem.lower() not in ['crescente', 'decrescente']:
        print("Argumento inválido, tente novamente!")
        return
    ordem_crescente = True if ordem.lower() != "crescente" else False

    ordenar_estoque = sorted(estoque, key=lambda produto: produto['quantidade'], reverse=ordem_crescente)

    print(f"Produtos ordenador por quantidade em ordem {'crescente' if ordem_crescente else 'decrescente'} :")
    print("-" * 80)
    print(f"{'Descrição':<25} {'Código':<10} {'Quantidade':<15} {'Custo':<10} {'Preço de Venda':<15}")
    print("-" * 80)

    for produto in ordenar_estoque:
        print(f"{produto['descrição']:<25}| {produto['código']:<10}| {produto['quantidade']:<14}| "
              f"{produto['custo']:<8.2f}| {produto['preço de venda']:<15.2f}|")
    
    print("-" * 80)

'''
6. Busca de produtos: Implemente uma função para buscar produtos no estoque com base na descrição ou código do produto,
esta função deve receber parâmetros passados obrigatoriamente por palavra-chave.Caso o produto não seja encontrado,
exiba uma mensagem apropriada e caso mais de um produto seja encontrado as informações de todos devem ser exibidas.
'''

def buscar_produtos(estoque=estoque, descricao=None, codigo=None):
    '''
    Realiza a busca de produtos utilizando como parâmetros a descrição ou código

    O usuário escolhe a forma de busca, podendo ser por descrição ou código. Com base nisso, a função encontra produtos correspondentes no estoque,
    exibindo as informações em uma tabela.
    Se nenhum produto for encontrado, uma mensagem informando o caso será exibida.

    Args:
        estoque (list, opcional): Listagem de produtos no estoque, utilizada como padrão como a variável global 'estoque'.
        descrição(str, opcional): Termo para buscar por descrição.
        codigo(int, opcional): Termo para buscar por código.

    Returns: None
    '''
    produtos = []
    escolha_busca = input("Você gostaria de buscar o produto por 'descrição' ou 'código'? ")

    if escolha_busca.lower() not in ('descrição', 'código'):
        print('Busca inválida, tente novamente')
        buscar_produtos()
        return

    if escolha_busca.lower() == 'código':
        codigo = int(input("Digite o código que você gostaria de buscar: "))
        for produto in estoque:
            if int(produto['código']) == codigo:
                produtos.append(produto)
    
    if escolha_busca.lower() == 'descrição':
        descricao = input("Digite o nome do produto: ")
        for produto in estoque:
            if descricao.lower() in produto['descrição'].lower() or produto['descrição'].startswith(descricao):
                produtos.append(produto)

    if produtos:
        print("Produtos em estoque:")
        print("-" * 80)
        print(f"{'Descrição':<25} {'Código':<10} {'Quantidade':<15} {'Custo':<10} {'Preço de Venda':<15}")
        print("-" * 80)
        for produto in produtos:
            print(f"{produto['descrição']:<25}| {produto['código']:<10}| {produto['quantidade']:<14}|"
                f"{produto['custo']:<8.2f}| {produto['preço de venda']:<15.2f}|")
    
        print("-" * 80)
    if not produtos:
        print("Nenhum produto encontrado com os critérios informados.")

'''
7. Remoção de produtos: Adicione uma função que permita a remoção de um produto do sistema com base no código do produto.
'''

def remover_produto():
    '''
    Realiza a remoção de produtos do estoque.

    A função busca o produto com base no código informado pelo usuário e realiza a remoção do mesmo caso seja encontrado,
    e uma mensagem de confirmação será exibida, caso contrário, uma mensagem será exibida com a informação de que o produto não foi encontrado.

    Args: 
        None
    
    Returns:
        None
    '''
    codigo = int(input("Informe o código do produto a ser removido: "))
    for i, produto in enumerate(estoque):
        if int(produto['código'] == codigo):
            estoque.pop(i)
            print(f"Produto: '{produto['descrição']}' de 'Código: {codigo}' removido com sucesso")
            return
    print(f"Produto de código {codigo} não encontrado")

'''
8. Consulta de produtos esgotados: Crie uma funcionalidade que exiba todos os produtos com quantidade igual a zero (esgotados).
'''

def consulta_esgotados():
    #produtos_esgotados = [produto for produto in estoque if int(produto['quantidade']) == 0]
    '''
    Gera uma lista de produtos com estoque esgotado

    A função realiza um filtro de produtos onde a quantidade em estoque é igual a zero e exibe suas informações.
    Caso nenhum produto seja encontrado, uma mensagem será exibida.

    Args: 
        None
    
    Returns:
        None
    '''
    produtos_esgotados = list(filter(lambda produto: int(produto['quantidade']) == 0, estoque))

    if produtos_esgotados:
        print("Produtos em estoque:")
        print("-" * 80)
        print(f"{'Descrição':<25} {'Código':<10} {'Quantidade':<15} {'Custo':<10} {'Preço de Venda':<15}")
        print("-" * 80)
        for produto in produtos_esgotados:
            print(f"{produto['descrição']:<25}| {produto['código']:<10}| {produto['quantidade']:<14}|"
                f"{produto['custo']:<8.2f}| {produto['preço de venda']:<15.2f}|")
    
        print("-" * 80)
    if not list(produtos_esgotados):
        print("Nenhum produto encontrado com os critérios informados.")

'''
9. Filtro de produtos com baixa quantidade: Adicione uma função que permita filtrar os produtos com quantidade abaixo de um limite mínimo especificado pelo
usuário ou uma quantidade padrão caso o usuário não o forneça e gere um relatório com esses produtos.
'''

def filtro_baixa_quantidade():
    '''
    Gera uma lista de produtos com estoque esgotado

    A função realiza um filtro de produtos onde a quantidade em estoque é igual a uma quantidade mínima informada pelo usuário e exibe suas informações.
    Caso nenhum produto seja encontrado, uma mensagem será exibida.

    Args: 
        None
    
    Returns:
        None
    '''
    quantidade_minima = int(input("Qual a quantidade mínima de produtos? "))
    produtos_com_baixa_quantidade = filter(lambda produto: int(produto['quantidade']) < quantidade_minima, estoque)
    if produtos_com_baixa_quantidade:
        print("Produtos em estoque:")
        print("-" * 80)
        print(f"{'Descrição':<25} {'Código':<10} {'Quantidade':<15} {'Custo':<10} {'Preço de Venda':<15}")
        print("-" * 80)
        for produto in produtos_com_baixa_quantidade:
            print(f"{produto['descrição']:<25}| {produto['código']:<10}| {produto['quantidade']:<14}|"
                f"{produto['custo']:<8.2f}| {produto['preço de venda']:<15.2f}|")
    
        print("-" * 80)
    if not produtos_com_baixa_quantidade:
        print("Nenhum produto encontrado com os critérios informados.")
'''
10. Atualização de estoque: Crie uma função para atualizar a quantidade de um produto específico no estoque.
A atualização pode incluir tanto a entrada (aumento) de quantidade quanto a saída (diminuição) da quantidade de produtos.
'''

def atualizar_estoque():
    '''
    Atualiza a quantidade de um produto em estoque com base na entrada ou saída.

    A função solicita ao usuário o código do produto a ser atualizado, verifica a existência do mesmo e solicita ao usuário
    a informação se a atualização é de entrada ou saída de produtos. Caso o produto não seja encontrado ou a operação resulte
    em quantidade negativa, a função exibirá uma mensagem informativa.

    Args:
        None

    Returns:
        None
    '''
    codigo = int(input("Informe o código do produto a ser atualizado: "))
    if codigo not in [produto['código'] for produto in estoque]:
        print("Produto não encontrado")
        return
    else:
        entrada_saida = input("A atualização vai ser 'entrada' ou 'saída' de produtos? ")
        quantidade = int(input("Informe a quantidade de produtos no estoque a serem atualizados: "))
        for produto in estoque:
            if int(produto['código']) == codigo and produto['código']:
                if entrada_saida.lower() == 'entrada':
                    atualizacao_quantidade = int(produto['quantidade']) + quantidade
                elif entrada_saida.lower() == 'saída':
                    atualizacao_quantidade = int(produto['quantidade']) - quantidade
                else:
                    print("Entrada inválida")
                    return
                if atualizacao_quantidade >= 0:
                    produto['quantidade'] = atualizacao_quantidade
                    print(f"Quantidade de '{produto['descrição']}', de 'código {produto['código']}' atualizada para '{produto['quantidade']}'")
                else:
                    print("Quantidade de produto negativa, verifique os dados informados.")
                    return

'''
11. Atualização de preços: Implemente uma função que permita alterar o preço de venda de um produto específico.
'''

def atualizar_preco():
    '''
    Atualiza o preço de venda de um produto em estoque, podendo ser acréscimo ou desconto.

    A função solicita ao usuário o código do produto a ser atualizado, verifica a existência do mesmo e solicita ao usuário
    a informação se a atualização é de acréscimo ou desconto no produto. Caso o produto não seja encontrado ou a operação resulte
    em quantidade negativa, a função exibirá uma mensagem informativa.

    Args:
        None

    Returns:
        None
    '''

    codigo = int(input("Informe o código do produto a ser atualizado: "))
    if codigo not in [produto['código'] for produto in estoque]:
        print("Produto não encontrado")
        return
    else:
        entrada_saida = input("O preço vai 'subir' ou 'diminuir'? ")
        valor = float(input(f"Informe o valor a {'ser diminuido' if entrada_saida == 'diminuir' else 'ser acrescido'}: "))
        for produto in estoque:
            if int(produto['código']) == codigo:
                if entrada_saida.lower() == 'subir':
                    atualizacao_valor = float(produto['preço de venda']) + valor
                elif entrada_saida.lower() == 'diminuir':
                    atualizacao_valor = float(produto['preço de venda']) - valor
                else:
                    print("Entrada inválida")
                    return
                if atualizacao_valor >= 0:
                    produto['preço de venda'] = atualizacao_valor
                    print(f"valor de '{produto['descrição']}', de 'código {produto['código']}' atualizada para '{produto['preço de venda']}'")
                elif atualizacao_valor == produto['preço de venda']:
                    print("Não houve atualização de valores")
                else:
                    print("Valor de produto negativa, verifique os dados informados.")
                    return

'''
13. Calcular valor total do estoque: Crie uma função que calcule o valor total do estoque,
multiplicando a quantidade de cada produto pelo seu preço de venda.
'''

def valor_total_estoque():
    '''
    Calcula e exibe o valor total do estoque, usando como base a quantidade e o preço de venda dos produtos.

    A função itera entre todos os produtos, multiplicando a quantidade pelo preço de venda enquanto soma os valores na variável
    valor_total, em seguida exibe o valor formatado.

    Args:
        None

    Returns:
        None
    '''
    valor_total = 0
    for produto in estoque:
        valor_total += int(produto['quantidade']) * float(produto['preço de venda'])
    print(f"O valor total do estoque é de: R${valor_total:.2f}")

'''
14. Cálculo do lucro presumido: Crie uma função que calcule o lucro presumido do estoque,
considerando a diferença entre o preço de venda e o custo de cada item multiplicado pela
quantidade disponível. Exiba o lucro total do estoque no terminal.
'''
def valor_lucro_presumido():
    '''
    Calcula e exibe o lucro presumido do estoque.

    A função calcula o lucro subtraindo o valor total do custo e o valor total de venda.
    Usando a quantidade de produtos e o preço de venda para calculo do total e quantidade e custo para o valor a ser descontado
    O lucro é exibido formatado.

    Args:
        None
    
    Returns:
        None
    '''


    valor_total = sum(int(produto['quantidade']) * float(produto['preço de venda']) for produto in estoque)
    desconto_estoque = (sum(int(produto['quantidade']) * float(produto['custo']) for produto in estoque))
    lucro = valor_total - desconto_estoque
    print(f"O valor total do lucro é de: R${lucro:.2f}")
    
'''
16. Relatório geral do estoque: Desenvolva uma função que exiba um relatório geral no terminal,
incluindo a descrição, código, quantidade, custo, preço de venda, e o valor total por item (quantidade * preço).
O relatório deve usar os métodos .ljust(), .rjust(), método .format() ou métodos semelhantes para formatar a saída de forma organizada.
Ao final do relatório, exiba o custo total e o faturamento total do estoque.
'''
def gerar_relatorio():
    '''
    A função gera e exibe um relatório detalhado do estoque, com informações de descrição, código, quantidade, custo, preço de venda, valor total e faturamento.
    Além de calcular o custo total e faturamento.

    A função itera sobre os produtos no estoque e exibe um relatório formatado contendo as informações:
    - Descrição
    - Código
    - Quantidade em estoque
    - Custo de produção unitária
    - Preço de venda unitária
    - Valor total (quantidade * preço de venda)
    - Faturamento (valor total - custo total)

    Args:
        None
    
    Returns:
        None
    '''
    print("-" * 120)
    print("{:<30} {:<10} {:<12} {:<10} {:<15} {:<15} {:<15}".format(
        "Descrição", "Código", "Quantidade", "Custo", "Preço de Venda", "Valor Total", "Faturamento"))
    print("-" * 120) 
    
    custo_total = 0
    faturamento_total = 0
    
    for produto in estoque:
        valor_total_item = produto['quantidade'] * produto['preço de venda']
        custo_total_item = produto['quantidade'] * produto['custo']
        faturamento_total_item = valor_total_item - custo_total_item
        
        custo_total += custo_total_item
        faturamento_total += faturamento_total_item
        
        print("{:<30} {:<10} {:<12} {:<10.2f} {:<15.2f} {:<15.2f} {:<15.2f}".format(
            produto['descrição'].ljust(30),  # .ljust() alinha à esquerda
            produto['código'], 
            produto['quantidade'],
            produto['custo'], 
            produto['preço de venda'], 
            valor_total_item,
            faturamento_total_item
        ))
    
    print("-" * 120)
    print("{:<70} {:<15.2f}".format("Custo Total", custo_total))
    print("{:<70} {:<15.2f}".format("Faturamento Total", faturamento_total))
    print("-" * 120)
