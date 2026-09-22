from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    # Esto le dice a Python que envíe tu diseño web a quien visite la URL
    return send_file('hola.html')