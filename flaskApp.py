# Here is the skeleton flask app - I'll add everything when the moodules are done

import flask
from flask import render_template

# imports from other modules
import globals
import database
from prediction import predictor


app = flask.Flask(__name__)

@app.route('/')
def main():

    # Call AI module to get prediction of BP1, BP2, Oxy Pulse
    p = predictor()
    p.preprocessingData()
    p.training()
    predictedData = p.prediction(5000)

    # get new data of BP1, BP2, Oxy, Pulse from DB
    latestData = database.find()

    if globals.alert is True:
        # edit html to add warning to it
        #   - use values set in globals.py file
        print("HI")

    # call Display module to get format the html
    

    return render_template("welcome.html")


if __name__ == "__main__":
    # Start adding data to the db every 30 seconds
    database.timedDataInsert()

    # run the app
    app.run(debug=True)