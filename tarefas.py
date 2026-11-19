print("Let's Go!") # print de teste
from datetime import datetime # biblioteca para manipulação de datas
import json # biblioteca para uso de arquivos JSON

def carregar_tarefas():
    with open('tarefas.json') as data_file: # abre o arquivo tarefas.json para leitura como "data_file"
        tarefas = json.load(data_file) # a variável "tarefas" recebe o conteúdo do arquivo json
    return tarefas

def exibir_menu():
    for i, item in enumerate(menu):
            print(f"{i + 1}. {item}")

def verificar_escolha(escolha):
    if escolha.isdigit():
        escolha = int(escolha)
        if 1 <= escolha <= len(menu):
            return True
    return False

def salvar_tarefas(lista):
    with open('tarefas.json', 'w', encoding='utf-8') as outfile:
        json.dump(lista, outfile, sort_keys=True, indent=4) # salva a nova lista de tarefas no arquivo JSON

def adicionar_tarefa(descricao):
    data_atual = datetime.today().strftime('%Y-%m-%d') # recebe a data atual formatada no exato momento em que o usuário adicionar a tarefa.
    tarefa = {
        "id": len(tarefas) + 1, # Acho que isso aqui vai dar ruim já já
        "descricao": descricao,
        "concluida": False,
        "criada_em": data_atual
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    print("Lista de Tarefas:")
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in tarefas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['id']}. {tarefa['descricao']} - {status} (Criada em: {tarefa['criada_em']})")

def concluir_tarefa(tarefa_id):
    field_key = "id"
    for tarefa in tarefas:
        if tarefa[field_key] == tarefa_id:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            print(f"Tarefa {tarefa_id} marcada como concluída.")
            return
    print(f"Tarefa {tarefa_id} não encontrada.")
def remover_tarefa(tarefa_id):
    field_key = "id"
    new_tarefas = []
    tarefas_length = len(tarefas)
    i = 0
    for tarefa in tarefas:
        if tarefa[field_key] == int(tarefa_id):
            pass
        else:
            tarefa["id"] = i + 1
            i += 1
            new_tarefas.append(tarefa)
    salvar_tarefas(new_tarefas)
    print(f"Tarefa {tarefa_id} removida com sucesso.")
menu = ["Adicionar Tarefa", "Listar Tarefas", "Marcar como Concluída", "Remover Tarefas", "Sair"] # menu armazenado
mainLoop = True # variável de controle do loop principal
while mainLoop:
    menuLoop = True # variável de controle do loop de escolha de opções
    tarefas = carregar_tarefas()
    print("=================================")
    print("Gerenciador de Tarefas")
    print("=================================")
    print("Escolha uma opção:")
    exibir_menu()

    while menuLoop:
        selecao = input("Digite o número da opção desejada: ")
        if verificar_escolha(selecao):
            selecao = int(selecao)
            menuLoop = False
        else:
            print("Entrada inválida. Por favor, escolha entre os números exibidos no menu.")

    match selecao:
        case 1:
            adicionar_tarefa(input("Digite a descrição da tarefa: "))
        case 2:
            listar_tarefas()
        case 3:
            menuLoop = True
            while menuLoop:
                listar_tarefas()
                selecao = input("Digite o ID da tarefa que deseja marcar como concluída: ")
                verificar_escolha(selecao)
                if verificar_escolha(selecao):
                    selecao = int(selecao)
                    menuLoop = False
                else:
                    print("Entrada inválida. Por favor, digite um número válido de ID.")
            concluir_tarefa(selecao)
        case 4:
            menuLoop = True
            while menuLoop:
                listar_tarefas()
                selecao = input("Digite o ID da tarefa que deseja remover: ")
                verificar_escolha(selecao)
                if verificar_escolha(selecao):
                    selecao = int(selecao)
                    menuLoop = False
                else:
                    print("Entrada inválida. Por favor, digite um número válido de ID.")
            remover_tarefa(selecao)
        case 5:
            print("Encerrando o programa...")
            mainLoop = False
            break