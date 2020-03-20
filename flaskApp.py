# Here is the skeleton flask app - I'll add everything when the moodules are done

import flask
from flask import render_template

# imports from other modules
import globals


app = flask.Flask(__name__)

@app.route(('/')
def main():

    # Call AI module to get prediction of BP1, BP2, Oxy Pulse

    # get new data of BP1, BP2, Oxy, Pulse from DB

    if globals.alert is True:
        # edit html to add warning to it
        #   - use values set in globals.py file


    # call Display module to get format the html

    html = "";

    return render_template(html)


if __name__ == "__main__":
    app.run()