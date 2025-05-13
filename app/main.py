from flask import Flask, request, jsonify
from .tarefas import tarefas, adicionar_tarefa, editar_tarefa, deletar_tarefa

app = Flask(__name__)

@app.route('/tarefas', methods=['GET'])
def listar():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar():
    dados = request.json
    nova = adicionar_tarefa(dados['titulo'])
    return jsonify(nova), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def editar(id):
    dados = request.json
    editada = editar_tarefa(id, dados['titulo'])
    return jsonify(editada)

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir(id):
    deletar_tarefa(id)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
