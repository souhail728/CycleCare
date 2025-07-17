from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Test Flask App</h1><p>L\'application fonctionne!</p>'

if __name__ == '__main__':
    print("Démarrage de l'application de test...")
    app.run(host='127.0.0.1', port=5000, debug=True)
