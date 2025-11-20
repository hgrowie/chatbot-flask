from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def home():
    return render_template("index1.html")  # Lädt die HTML-Datei aus dem templates-Ordner


