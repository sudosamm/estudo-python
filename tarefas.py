import json  # biblioteca para uso de arquivos JSON
from datetime import datetime  # biblioteca para manipulação de datas


def carregar_tarefas():
    # abre o arquivo tarefas.json para leitura como "data_file"
    with open("tarefas.json", encoding="utf-8") as data_file:  
        # a variável "tarefas" recebe o conteúdo do arquivo json
        tarefas = json.load(data_file)  
    return tarefas


def exibir_menu():
    for i, item in enumerate(menu):
        print(f"{i + 1}. {item}")


def verificar_escolha(area, funcao):
    menu_loop = True
    while menu_loop:
        match funcao:
            case "concluir":
                listar_tarefas(area)
                escolha = input(
                    "Digite o ID da tarefa que deseja marcar como concluída (ou 0 para cancelar): "
                )
            case "remover":
                listar_tarefas(area)
                escolha = input(
                    "Digite o ID da tarefa que deseja remover (ou 0 para cancelar): "
                )
            case _:
                exibir_menu()
                escolha = input(
                    "Digite o número da opção desejada: "
                )
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(area):
                menu_loop = False
                return escolha
            elif escolha == 0:
                print("Operação cancelada.")
                menu_loop = False
                return None
        print("Entrada inválida. Por favor, escolha entre os números exibidos no menu.")


def salvar_tarefas(lista):
    with open("tarefas.json", "w", encoding="utf-8") as outfile:
        json.dump(
            lista, outfile, sort_keys=True, indent=4, ensure_ascii=False
        )  # salva a nova lista de tarefas no arquivo JSON


def adicionar_tarefa(descricao, lista):
    data_atual = datetime.today().strftime(
        "%Y-%m-%d"
    )  # recebe a data atual formatada no exato momento em que o usuário adicionar a tarefa.
    tarefa = {
        "id": len(lista) + 1,
        "descricao": descricao,
        "concluida": False,
        "criada_em": data_atual,
    }
    lista.append(tarefa)
    salvar_tarefas(lista)
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(lista):
    print("Lista de Tarefas:")
    if not lista:
        print("Nenhuma tarefa encontrada.")
    else:
        for tarefa in lista:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(
                f"{tarefa['id']}. {tarefa['descricao']} - {status} (Criada em: {tarefa['criada_em']})"
            )


def concluir_tarefa(tarefa_id, lista):
    for tarefa in lista:
        if tarefa["id"] == tarefa_id:
            tarefa["concluida"] = True
            salvar_tarefas(lista)
            print(f"Tarefa {tarefa_id} marcada como concluída.")
            return
    print(f"Tarefa {tarefa_id} não encontrada.")


def remover_tarefa(tarefa_id, lista):
    new_tarefas = []
    i = 0
    for tarefa in lista:
        if tarefa["id"] == int(tarefa_id):
            pass
        else:
            tarefa["id"] = i + 1
            i += 1
            new_tarefas.append(tarefa)
    salvar_tarefas(new_tarefas)
    print(f"Tarefa {tarefa_id} removida com sucesso.")


menu = [
    "Adicionar Tarefa",
    "Listar Tarefas",
    "Marcar como Concluída",
    "Remover Tarefas",
    "Sair",
]  # menu armazenado

if __name__ == "__main__":
    main_loop = True  # variável de controle do loop principal
    while main_loop:
        lista = carregar_tarefas()
        print("=================================")
        print("Gerenciador de Tarefas")
        print("=================================")
        print("Escolha uma opção:")

        selecao = verificar_escolha(menu, "menu")

        match selecao:
            case 1:
                adicionar_tarefa(input("Digite a descrição da tarefa: "), lista)
            case 2:
                listar_tarefas(lista)
            case 3:
                selecao = verificar_escolha(lista, "concluir")
                if selecao is None:
                    continue
                concluir_tarefa(selecao, lista)
            case 4:
                selecao = verificar_escolha(lista, "remover")
                if selecao is None:
                    continue
                remover_tarefa(selecao, lista)
            case 5:
                print("Encerrando o programa...")
                main_loop = False
