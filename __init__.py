from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Génération de la clé et création de l'objet Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()              # Convertit la valeur en bytes
    token = f.encrypt(valeur_bytes)             # Chiffre la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token sous forme de string

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()            # Convertit le token en bytes
        valeur_decryptee = f.decrypt(token_bytes)  # Déchiffre le token
        return f"Valeur décryptée : {valeur_decryptee.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
