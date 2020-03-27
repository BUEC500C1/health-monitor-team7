
# Author: Elizabeth Slade

    # For my prediction algorithm, I used lqi25's "pulse, blood pressure, blood oxygen" csv file from team: health-monitor-HealthCover 

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class predictor():
    time = ""
    pulseData = []
    bloodPressureData = []
    bloodOxygenData = []
    timeData = []
    pulseRegression = LinearRegression()
    bloodPressureRegression = LinearRegression()
    bloodOxygenRegression = LinearRegression()

    def __init__(self):
        healthData = pd.read_csv('healthData.csv')
        
        pulseData = healthData[ 'pulse' ].values
        self.pulseData  = np.array([pulseData ]).T

        bloodPressureData = healthData['bloodpressure' ].values
        self.bloodPressureData = np.array([bloodPressureData]).T

        bloodOxygenData = healthData[ 'bloodoxygen' ].values
        self.bloodOxygenData = np.array([bloodOxygenData]).T

        timeData = healthData[ 'time' ].values
        self.timeData = np.array([ timeData ]).T
    
    def appendDataAndRetrain(self):
        print("Pulse data:", len(self.pulseData))
        print("blood pressure:", len(self.bloodPressureData))
        print("blood oxy: ", len(self.bloodOxygenData))
        

    def train(self):
        self.pulseRegression.fit(self.timeData,self.pulseData )
        self.bloodPressureRegression.fit(self.timeData,self.bloodPressureData)
        self.bloodOxygenRegression.fit(self.timeData,self.bloodOxygenData)

# what will this time be?

    def predict(self, time):
        pulsePrediction = int(self.pulseRegression.predict(np.array([[time]])))
        print("Pulse Prediction: ",pulsePrediction)

        bloodPressurePrediction = int(self.bloodPressureRegression.predict(np.array([[time]])))
        print("Blood Pressure Prediction: ",bloodPressurePrediction)

        bloodOxygenPrediction = int(self.bloodOxygenRegression.predict(np.array([[time]])))
        print("Blood Oxygen Prediction: ",bloodOxygenPrediction)

        return [pulsePrediction, bloodPressurePrediction, bloodOxygenPrediction]


p = predictor()
p.appendDataAndRetrain()
p.train()
p.predict(5000)