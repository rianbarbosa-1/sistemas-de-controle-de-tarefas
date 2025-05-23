from sistema_tarefas.tarefa import adicionar_tarefa, listar_tarefas, marcar_concluida, remover_tarefa
from sistema_tarefas.arquivo import carregar_tarefas, salvar_tarefas

def menu():
    print("\n==== Sistema de Controle de Tarefas ====")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

def main():
    tarefas = carregar_tarefas()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            id_tarefa = int(input("Digite o ID da tarefa a marcar: "))
            marcar_concluida(tarefas, id_tarefa)
        elif escolha == '4':
            id_tarefa = int(input("Digite o ID da tarefa a remover: "))
            remover_tarefa(tarefas, id_tarefa)
        elif escolha == '5':
            salvar_tarefas(tarefas)
            print("Saindo... Tarefas salvas.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
