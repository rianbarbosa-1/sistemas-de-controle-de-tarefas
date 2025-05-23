def adicionar_tarefa(tarefas, descricao):
    nova_tarefa = {
        'id': len(tarefas) + 1,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for tarefa in tarefas:
        status = '✔️' if tarefa['concluida'] else '❌'
        print(f"{tarefa['id']}. [{status}] {tarefa['descricao']}")

def marcar_concluida(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefa['concluida'] = True
            print(f"Tarefa '{tarefa['descricao']}' marcada como concluída.")
            return
    print("Tarefa não encontrada.")

def remover_tarefa(tarefas, id_tarefa):
    for tarefa in tarefas:
        if tarefa['id'] == id_tarefa:
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa['descricao']}' removida com sucesso.")
            return
    print("Tarefa não encontrada.")
