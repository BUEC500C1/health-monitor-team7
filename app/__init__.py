from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/display')
def display():
    alert = {'bloodPressure': True, 'pulse': True, 'oxygenContent': True}
    data = {'pulse': [], 'bloodPressure': [], 'oxygenContent': []}
    AIdata = {'AIpulse': 0, 'AIbloodPressure': 0, 'AIoxygenContent': 0}
    return render_template('display.html', title='Display', alert=alert, data=data, AIdata=AIdata)
