from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/data_list')
def data_list():
    return render_template('data_list.html')

