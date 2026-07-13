from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon application EC2</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #f8fafc;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }}
        .card {{
            background: #1e293b;
            padding: 40px 60px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
            text-align: center;
        }}
        h1 {{
            color: #38bdf8;
            margin-bottom: 10px;
        }}
        p {{
            color: #cbd5e1;
            margin: 6px 0;
        }}
        .badge {{
            display: inline-block;
            background: #22c55e;
            color: #052e16;
            padding: 4px 12px;
            border-radius: 999px;
            font-weight: bold;
            margin-top: 10px;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Application déployée avec succès !</h1>
        <p>Nom du serveur : <strong>{hostname}</strong></p>
        <p>Heure du serveur : <strong>{time}</strong></p>
        <span class="badge">EN LIGNE</span>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return PAGE.format(
        hostname=socket.gethostname(),
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

if __name__ == "__main__":
    # L'application doit être accessible depuis l'extérieur de l'instance (0.0.0.0)
    # et sur un port bien identifiable dans l'URL du navigateur.
    app.run(host="0.0.0.0", port=5000)
