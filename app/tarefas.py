tarefas = []
contador = 1

def adicionar_tarefa(titulo):
    global contador
    nova = {'id': contador, 'titulo': titulo}
    tarefas.append(nova)
    contador += 1
    return nova

def editar_tarefa(id, novo_titulo):
    for t in tarefas:
        if t['id'] == id:
            t['titulo'] = novo_titulo
            return t
    return None

def deletar_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
