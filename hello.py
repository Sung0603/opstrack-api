from flask import Flask
import random

app = Flask(__name__)

frases = [
    "Bem-vindo ao OpsTrack API 🚀",
    "Monitorando seus chamados com eficiência.",
    "Simplicidade e organização em um só lugar.",
    "Sua central de suporte, sempre online."
]

estilo_base = """
<html>
    <head>
        <title>OpsTrack API</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; padding: 60px;">
        <h1 style="color: #2c3e50;">{titulo}</h1>
        {conteudo}
        <hr style="width: 200px; border: 1px solid #ddd; margin: 20px auto;">
        <p style="font-size: 14px; color: #999;">OpsTrack API · v1.0.0</p>
    </body>
</html>
"""

@app.route("/")
def hello_world():
    frase = random.choice(frases)
    conteudo = f'<p style="font-size: 18px; color: #555;">{frase}</p>'
    return estilo_base.format(titulo="OpsTrack API", conteudo=conteudo)

@app.route("/status")
def status():
    conteudo = '<p style="font-size: 18px; color: #27ae60;">✅ Serviço online</p>'
    return estilo_base.format(titulo="Status", conteudo=conteudo)

@app.route("/tickets")
def tickets():
    lista_tickets = [
        {"id": 1, "titulo": "Erro no login", "status": "aberto"},
        {"id": 2, "titulo": "Lentidão no servidor", "status": "em andamento"},
        {"id": 3, "titulo": "Falha no backup", "status": "resolvido"}
    ]

    linhas = ""
    for t in lista_tickets:
        linhas += f"""
        <li style="font-size: 16px; color: #555; margin-bottom: 8px;">
            #{t['id']} — {t['titulo']} <strong>({t['status']})</strong>
        </li>
        """

    conteudo = f'<ul style="list-style: none; padding: 0;">{linhas}</ul>'
    return estilo_base.format(titulo="Tickets", conteudo=conteudo)

@app.route("/sobre")
def sobre():
    conteudo = """
    <p style="font-size: 16px; color: #555;">
        <strong>Nome:</strong> opstrack-api<br>
        <strong>Descrição:</strong> API para acompanhamento e gerenciamento de tickets de suporte<br>
        <strong>Versão:</strong> 1.0.0
    </p>
    """
    return estilo_base.format(titulo="Sobre", conteudo=conteudo)

if __name__ == "__main__":
    app.run(debug=True)