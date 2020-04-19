
import flask
from flask import render_template
import json
# imports from other modules
import globals
import database
from prediction import predictor


app = flask.Flask(__name__)

class dataPoint:
    def __init__(self, time, data):
        self.x = time
        self.y = data

@app.route('/')
def main():

    # Call AI module to get prediction of BP1, BP2, Oxy Pulse
    p = predictor()
    p.train()
    predictedData = p.predict(5000)

    # get new data of BP1, BP2, Oxy, Pulse from DB
    # latestData = database.find()

    # call Display module to get format the html

    #parse data into graphable format
    timeData = []
    pulseData = []
    bpSysData = []
    bpDiaData = []
    oxygenData = []

    for i in database.find_all():
        p.appendData(i)
        x_val = i['createAt']
        pulse_val = i['pulse']
        bp_sys_val = i['bloodPreSys']
        bp_dia_val = i['bloodPreDia']
        oxy_val = i['bloodOx']
        timeData.append(x_val)
        pulseData.append(pulse_val  )
        bpSysData.append(bp_sys_val)
        bpDiaData.append(bp_dia_val)
        oxygenData.append(oxy_val)

    p.train()
    predictedData = p.predict(5000) #5000 is time in the future

    alert = {'bloodPressureSys': globals.bp_sys_flag, 'bloodPressureDia': globals.bp_dia_flag,'pulse': globals.pulse_flag, 'oxygenContent': globals.oxygen_flag}
    data = {'time': timeData,'pulse': pulseData, 'bloodPressureSys': bpSysData, 'bloodPressureDia': bpDiaData,'oxygenContent': oxygenData}
    AIdata = {'AIpulse': predictedData[0], 'AIbloodPressure': predictedData[1], 'AIoxygenContent': predictedData[2]}
    return render_template('display.html', title='Display', alert=alert, data=data, AIdata=AIdata)


if __name__ == "__main__":
    # Start adding data to the db every 30 seconds
    database.timedDataInsert()

    #database.delete_all()
    # run the app
    app.run(debug=True)
