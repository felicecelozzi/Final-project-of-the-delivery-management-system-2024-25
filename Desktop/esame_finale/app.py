from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registrazione_utente')
def registrazione_utente():
    return render_template('registrazione_utente.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/registrazione')
def registrazione():
    return render_template('registrazione.html')

if __name__ == '__main__':
    app.run(debug=True)
