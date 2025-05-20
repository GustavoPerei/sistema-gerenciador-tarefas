import sys
import os
import pytest

# Adiciona a pasta raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_criar_listar_excluir(client):
    # Criar
    resposta = client.post('/tarefas', json={'titulo': 'Estudar Flask'})
    assert resposta.status_code == 201
    tarefa = resposta.get_json()
    assert tarefa['titulo'] == 'Estudar Flask'

    # Listar
    resposta = client.get('/tarefas')
    assert resposta.status_code == 200
    assert len(resposta.get_json()) >= 1

    # Excluir
    resposta = client.delete(f"/tarefas/{tarefa['id']}")
    assert resposta.status_code == 204

def adicionar_tarefa(titulo, prioridade="média"):
    global contador
    nova = {'id': contador, 'titulo': titulo, 'prioridade': prioridade}
    tarefas.append(nova)
    contador + 1
    return nova

def contar_tarefas():
    return len(tarefas)

