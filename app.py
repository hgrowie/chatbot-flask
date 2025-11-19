from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def home():
    return render_template("index1.html")  # Lädt die HTML-Datei aus dem templates-Ordner

# API-Route für den Chatbot
@app.route('/send', methods=['POST'])


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Port für Render konfigurieren
    app.run(host="0.0.0.0", port=port, debug=True)
