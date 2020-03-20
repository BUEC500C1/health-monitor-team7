import flask
from flask import render_template

# imports from other modules
from globals import alert


app = flask.Flask(__name__)

@app.route(('/')
def main():

    # Call AI module to get prediction of BP1, BP2, Oxy Pulse

    # get new data of BP1, BP2, Oxy, Pulse from DB

    if alert is True:
        # edit html to add warning to it
        alert = False

    # call Display function to get format the html

    html = "";

    return render_template(html)


if __name__ == "__main__":
    app.run()