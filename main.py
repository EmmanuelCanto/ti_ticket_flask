from flask import Flask, render_template

app = Flask(__name__, template_folder='src/templates')

@app.route('/')
def index():
    name = 'emanuel'
    friends = ['Juan ', 'Pedro', 'Luis']
    return render_template('index.html', name=name, friends=friends)