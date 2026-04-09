from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Permite que o frontend acesse esta API
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Nossos dados mockados exigidos pelo professor
clientes_mock = [
    {"id": 1, "nome": "Yasmim Fernandes", "email": "yasmim@email.com", "telefone": "(11) 99999-1111"},
    {"id": 2, "nome": "Maria Eduarda", "email": "maria@email.com", "telefone": "(21) 99999-2222"},
    {"id": 3, "nome": "Julia Silva", "email": "julia@email.com", "telefone": "(31) 99999-3333"}
]

funcionarios_mock = [
    {"id": 101, "nome": "Jorge", "cargo": "Desenvolvedora Sênior", "departamento": "Tecnologia"},
    {"id": 102, "nome": "Vitoria", "cargo": "Analista de Suporte", "departamento": "Operações"},
    {"id": 103, "nome": "Daniela", "cargo": "Gerente de Projetos", "departamento": "Gestão"}
]

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return jsonify(clientes_mock), 200

@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    return jsonify(funcionarios_mock), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)