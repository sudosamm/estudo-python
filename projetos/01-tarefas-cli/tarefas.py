print("Let's Go!") # print de teste
from datetime import datetime # biblioteca para manipulação de datas
import json 
with open('tarefas.json') as data_file:
    ler_tarefas = json.load(data_file)

data_atual = datetime.today().strftime('%Y-%m-%d') # recebe a data atual formatada
menu = ["Adicionar Tarefa", "Listar Tarefas", "Remover Tarefas", "Sair"] # menu armazenado
tarefas = ler_tarefas # carrega o conteúdo do arquivo JSON em uma variável
loop = True # variável de controle do loop
while loop:
    print("Escolha uma opção:")
    for i, item in enumerate(menu):
        print(f"{i + 1}. {item}")

    selecao = int(input("Digite o número da opção desejada: "))
    match selecao:
        case 1:
            titulo = input("Digite a descrição da tarefa: ")
            tarefa = {
                "id": len(tarefas) + 1,
                "descricao": titulo,
                "concluida": False,
                "criada_em": data_atual
            }
            tarefas.append(tarefa)
            with open('tarefas.json', 'w') as outfile:
                json.dump(tarefas, outfile, sort_keys=True, indent=4) # salva a nova lista de tarefas no arquivo JSON
            print("Tarefa adicionada com sucesso!")
        case 2:
            print("Lista de Tarefas:")
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                for tarefa in tarefas:
                    status = "Concluída" if tarefa["concluida"] else "Pendente"
                    print(f"{tarefa['id']}. {tarefa['descricao']} - {status} (Criada em: {tarefa['criada_em']})")
        case 3:
            print("Remover tarefa, sei fazer ainda não")
        case 4:
            print("Encerrando o programa...")
            loop = False