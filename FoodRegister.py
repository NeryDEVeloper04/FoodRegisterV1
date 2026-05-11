import os

restaurantes = [
    {"nome": "Pizzaria TOP", "categoria": "Italiana", "Ativo": True},
    {"nome": "Sushi Casa Verde", "categoria": "Japonesa", "Ativo": False},
    {"nome": "Méqui Donalds", "categoria": "Fast-Food", "Ativo": True}
]

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

    
def exibir_nome_do_programa():
    print("""
FoodRegister
""")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair \n")

def finalizar_app():
    exibir_subtitulo("Finalizando o programa... ")
    
def opcao_invalida():
    print("Opcao inválida!")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes: ")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite a categoria do restaurante, {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "Ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!!!")
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo("Listando os restauntes: ")
    print(f"{"Nome do restaurante:".ljust(22)} | {"Categoria:".ljust(20)} | {"Status:"}")
    for restaurante in restaurantes:
        nome_do_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        status = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f"- {nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {status}")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    os.system("cls")
    exibir_subtitulo("Alternando o estado do restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja Ativar/Desativar: ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante.upper() == restaurante["nome"].upper():
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            
            estado = "ativado" if restaurante["Ativo"] else "desativado"
            print(f"O restaurante {restaurante['nome']} foi {estado} com sucesso!")

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input("Aperte qualquer tecla para retornar ao menu principal: ")
    main()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)


def escolher_opcoes():
    try: #ele tenta executar o codigo quando o usuario digitar uma string e o execept ele voltar ao menu principal
        opcao_escolhida = int(input("Escolha uma opçao: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
            print("Listar restaurante")
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()


exibir_nome_do_programa()
exibir_opcoes()
escolher_opcoes()
listar_restaurante()
voltar_ao_menu_principal()
exibir_subtitulo()
alternar_estado_restaurante()
cadastrar_novo_restaurante()