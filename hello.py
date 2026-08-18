from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/status")
def status():
    return {"status": "online"}

@app.route("/tickets")
def tickets():
    return {
        "tickets": [
            {"id": 1, "titulo": "Erro no login", "status": "aberto"},
            {"id": 2, "titulo": "Lentidão no servidor", "status": "em andamento"},
            {"id": 3, "titulo": "Falha no backup", "status": "resolvido"}
        ]
    }

@app.route("/sobre")
def sobre():
    return {
        "nome": "opstrack-api",
        "descricao": "API para acompanhamento e gerenciamento de tickets de suporte",
        "versao": "1.0.0"
    }

if __name__ == "__main__":
    app.run(debug=True)