execucao = True
while execucao:
    nome = input("insira seu nome: ")
    if all(c.isalpha() or c.isspace() for c in nome):
        execucao = False
    else:
        print("Caracter invalido detectado, por favor insira apenas letras.")
        continue
    print("ola", nome, "seja bem vindo/a ao sistema de educação EAD da Unip")

    while True:
        idade = input("Nos diga quantos anos você tem: ")
        if idade.isdigit():
            idade = int(idade)
            break
        else:
            print("Por favor digite apenas numeros na idade.")

    opcao = input(
        'Antes de continuarmos você aceita que seus dados pessoais sejam utilizados para fins de analises de estatisticas: \n[n/s]: ').upper()
    if opcao == 'N':
        execucao = True
    elif opcao == 'S':
        execucao = False

        print(
            "Primeiramente devemos saber o que é tecnologia da informação e para que ela serve.\n\nO que é Tecnologia da Informação?\nTecnologia da Informação, ou simplesmente TI, é o uso de computadores, programas e redes para guardar, organizar, compartilhar e proteger informações. Ela está presente em quase tudo que usamos hoje em dia: no celular, no caixa eletrônico, nos aplicativos de banco, nas redes sociais e até quando pedimos comida por delivery.\n\nA principal função da TI é ajudar pessoas e empresas a usarem melhor as informações para tomar decisões, resolver problemas e facilitar tarefas do dia a dia. Por exemplo, em uma empresa, a TI pode organizar os dados dos clientes, controlar o estoque, ou até ajudar nas vendas online.\n\nTI não é só 'mexer com computador'. Ela envolve várias áreas, como:\nSuporte técnico: quem ajuda a consertar ou configurar computadores e redes.\n\nDesenvolvimento de sistemas: quem cria programas e aplicativos.\n\nSegurança da informação: quem protege os dados contra ataques e vazamentos.\n\nAnálise de dados: quem organiza e interpreta informações para ajudar nas decisões.\n\nHoje, a TI é essencial em quase todas as profissões. Saber um pouco sobre ela pode abrir muitas portas no mercado de trabalho e facilitar a vida no dia a dia.")
        opcao = input("\n\nDeseja continuar para a proxima parte?\n[s/n]: ").upper()
        if opcao == 'N':
            execucao = True
        elif opcao == 'S':
            execucão = True

            while execucão:
                opcao = input("\n\nescolha uma das opções abaixo \nPseudocodigo ou Fluxograma: ").upper()
                if opcao == "PSEUDOCODIGO":
                    print(
                        "\nPseudocódigo é uma ferramenta que descreve os algoritmos de uma forma descritiva, com uma forma de linguagem que se aproxima da humana (geralmente uma criação moldada na lingua portuguesa ou em inglêsa) não levando em conta a sintaxe de uma linguagem de programação específica.\nO principal propósito do pseudocódigo é organizar e planejar um programa ou sistema através do raciocínio lógico do pensamento antes de implementá-lo por meio da programação. Sendo assim, o pseudocódigo deve ser compreensível para programadores e para pessoas que não têm conhecimento na área de computação.")
                elif opcao == 'FLUXOGRAMA':
                    print(
                        "\nUm fluxograma é, basicamente, um jeito visual de mostrar como um processo ou algoritmo funciona. Ele usa símbolos bem específicos e padronizados para representar cada etapa, tornando mais fácil entender a sequência de ações que levam a um determinado resultado.\nEsse tipo de representação é utilizada, principalmente quando se quer enxergar com clareza a lógica por trás de um programa. Ajuda muito na hora de planejar, entender o que está acontecendo e identificar possíveis erros no caminho.\n\nAlguns símbolos que aparecem com frequência:\n\nElipse (ou oval): marca o ponto de partida ou de encerramento do processo.\n\nRetângulo: representa uma ação, como um comando, cálculo ou atribuição.\n\nLosango: esse é o símbolo das decisões. Sabe aquele 'se... então...' típico da programação? Pois é.\n\nSetas: indicam o sentido do fluxo, mostrando a ordem em que tudo deve acontecer.")
                else:
                    print("\nOpção invalida por favor tente denovo.")
                    continue

                opcao = input(
                    "\nDeseja continuar para a proxima etapa ou voltar para ver a outra opção? \n\nvoltar/continuar:")
                if opcao == "continuar":
                    execucão = False
                    opcao = input(
                        "\nMuito obrigado por usar nosso sistema esperamos que tenha tido uma otima experiencia, deseja sair agora?: \n[s/n]:")
                    if opcao == 's':
                        execucao = True
                    else:
                        execucão = True
    else:
        print("Opção invalida tente novamente.")