from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        password = generate_password(length)
    return render_template('index.html', password=password)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password = password + random.choice(characters)
    return password


if __name__ == '__main__':
    app.run(debug=True)
