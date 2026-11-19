import json  # biblioteca para uso de arquivos JSON
from pathlib import Path
from datetime import datetime  # biblioteca para manipulação de datas


def load_tasks():
    # abre o arquivo tarefas.json para leitura como "read_data"
    try:
        file_path = Path.home() / 'Documents' / 'tasklist_data' / 'tasklist.json'
        with open(file_path, 'r', encoding="utf-8") as read_data:  
            # a variável "tasks" recebe o conteúdo do arquivo json
            tasks = json.load(read_data)  
    except:
        tasks = []
    return tasks


def show_menu():
    for i, item in enumerate(menu):
        print(f"{i + 1}. {item}")


def verify_data(area, objective):
    menu_loop = True
    while menu_loop:
        match objective:
            case "complete":
                list_tasks(area)
                interaction = input(
                    "Digite o ID da tarefa que deseja marcar como concluída (ou 0 para cancelar): "
                )
            case "remove":
                list_tasks(area)
                interaction = input(
                    "Digite o ID da tarefa que deseja remover (ou 0 para cancelar): "
                )
            case _:
                show_menu()
                interaction = input(
                    "Digite o número da opção desejada: "
                )
        if (interaction.isdigit()) or (interaction.strip() != ""):
            interaction = int(interaction)
            if 1 <= interaction <= len(area):
                menu_loop = False
                return interaction
            elif interaction == 0:
                print("Operação cancelada.\n")
                menu_loop = False
                return None
        print("Entrada inválida. Por favor, escolha entre os números exibidos no menu.\n")


def save_tasks(task_list):
    file_path = Path.home() / 'Documents' / 'tasklist_data' / 'tasklist.json'
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as write_data:
        json.dump(
            task_list, write_data, sort_keys=True, indent=4, ensure_ascii=False
        )  # salva a nova lista de tarefas no arquivo JSON


def add_task(task_list):
    menu_loop = True
    while menu_loop:
        description = input("Digite a descrição da tarefa (ou 0 para cancelar): ")
        if description.isdigit():
            description = int(description)
            if description == 0:
                print("Operação cancelada.\n")
                menu_loop = False
                return None
            else:
                print(f"Entrada inválida. '{description}' não é um valor válido para a descrição da tarefa.\n")
        elif description.strip() == "":
            print(f"Entrada inválida. '{description}' não é um valor válido para a descrição da tarefa.\n")
        else:
            menu_loop = False
    today = datetime.today().strftime(
        "%Y-%m-%d"
    )  # recebe a data atual formatada no exato momento em que o usuário adicionar a tarefa.
    task = {
        "id": len(task_list) + 1,
        "descricao": description,
        "concluida": False,
        "criada_em": today,
    }
    task_list.append(task)
    save_tasks(task_list)
    print("Tarefa adicionada com sucesso!\n")


def list_tasks(task_list):
    print("Lista de Tarefas:")
    if not task_list:
        print("Nenhuma tarefa encontrada.\n")
    else:
        for task in task_list:
            status = "Concluída" if task["concluida"] else "Pendente"
            print(
                f"{task['id']}. {task['descricao']} - {status} (Criada em: {task['criada_em']})"
            )


def complete_task(task_id, task_list):
    for task in task_list:
        if task["id"] == task_id:
            task["concluida"] = True
            save_tasks(task_list)
            print(f"Tarefa {task_id} marcada como concluída.")
            return
    print(f"Tarefa {task_id} não encontrada.\n")


def remove_task(task_id, task_list):
    new_list = []
    i = 0
    for task in task_list:
        if task["id"] == int(task_id):
            pass
        else:
            task["id"] = i + 1
            i += 1
            new_list.append(task)
    save_tasks(new_list)
    print(f"Tarefa {task_id} removida com sucesso.\n")


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
        task_list = load_tasks()
        print("=================================")
        print("Gerenciador de Tarefas")
        print("=================================")

        interaction = verify_data(menu, "menu")

        match interaction:
            case 1:
                add_task(task_list)
            case 2:
                list_tasks(task_list)
            case 3:
                interaction = verify_data(task_list, "complete")
                if interaction is None:
                    continue
                complete_task(interaction, task_list)
            case 4:
                interaction = verify_data(task_list, "remove")
                if interaction is None:
                    continue
                remove_task(interaction, task_list)
            case 5:
                print("Encerrando o programa...")
                main_loop = False