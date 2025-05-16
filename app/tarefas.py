import json
import os

tarefas = []

def salvar_tarefas(lista_tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4, ensure_ascii=False)

def carregar_tarefas():
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

tarefas = carregar_tarefas()

def adicionar_tarefa(titulo, lista_tarefas):
    tarefa = {
        "id": len(lista_tarefas) + 1,
        "titulo": titulo,
        "concluida": False
    }   
    lista_tarefas.append(tarefa)
    salvar_tarefas(lista_tarefas)
    return tarefa

nova_tarefa = adicionar_tarefa("Estudar Python", tarefas)
print(nova_tarefa)

def listar_tarefas(lista_tarefas):
    for tarefa in lista_tarefas:
        status = "✅" if tarefa["concluida"] else "❌"
        print(f"{tarefa['id']}: {tarefa['titulo']} {status}")
listar_tarefas(tarefas)

def concluir_tarefa(id, lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa["id"]== id:
            tarefa["concluida"] = True
             salvar_tarefas(lista_tarefas) 
            return 
    print ("Tarefa nao encontrada")

concluir_tarefa(1, tarefas)
listar_tarefas(tarefas)

def remover_tarefa(id, lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa["id"] == id:
            lista_tarefas.remove(tarefa)
            salvar_tarefas(lista_tarefas)
            return
    print("Tarefa nao encontrada")

remover_tarefa(1, tarefas)
listar_tarefas(tarefas)

def editar_tarefa (id, titulo, lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = titulo
            salvar_tarefas(lista_tarefas)
            return
    print("Tarefa nao encontrada")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Editar tarefa")
        print("6 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            titulo = input("Digite o titulo da tarefa: ")
            adicionar_tarefa(titulo, tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            id = int(input("Digite o id da tarefa: "))
            concluir_tarefa(id, tarefas)
        elif opcao == "4":
            id = int(input("Digite o id da tarefa: "))
            remover_tarefa(id, tarefas)
        elif opcao == "5":
            id = int(input("Digite o id da tarefa: "))
            titulo = input("Digite o novo titulo da tarefa: ")
            editar_tarefa(id, titulo, tarefas)
        elif opcao == "6":
            break
        else:
            print("Opcao invalida. Tente de novo.")