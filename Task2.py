from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = Fernet.generate_key()
f = Fernet(key)


@app.route('/')
def start_page():
    return 'Start page, please enter /encrypt or /decrypt in the search line'



@app.route('/encrypt/', methods=('GET', 'POST'))
def encrypt():
    '''
    When we in GET, we use form with input data
    for our POST, then this data we check is it empty or not
    and send it to Fernet
    '''
    if request.method == 'GET':
        return '<form method="POST">Enter the data: <input name="data"><input type="submit"></form>'
    else:
        data = request.form['data']
        if not data:
            return 'You don`t input anything'
        else:
            value_bytes = data.encode('UTF-8')
            token = f.encrypt(value_bytes)
            return render_template(
                'index.html',
                crypt = 'Encrypted',
                data = token)



@app.route('/decrypt/', methods=('GET', 'POST'))
def decrypt():
    '''
    When we in GET, we use form with input data
    for our POST, then this data we check is it empty or not
    and send it to Fernet
    '''
    if request.method == 'GET':
        return '<form method="POST">Enter the data: <input name="data"><input type="submit"></form>'
    else:
        data = request.form['data']
        if not data:
            return 'You don`t input anything'
        else:
            value_bytes = data.encode('UTF-8')
            value_bytes = f.encrypt(value_bytes)
            finish_data = f.decrypt(value_bytes)
            return render_template(
            'index.html',
            crypt='Decrypted',
            data=finish_data.decode())

if __name__ == '__main__':
    app.run(debug=True)
