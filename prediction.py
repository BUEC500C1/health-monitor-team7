# Author: Elizabeth Slade

    # For my prediction algorithm, I used lqi25's "pulse, blood pressure, blood oxygen" csv file from team: health-monitor-HealthCover

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class predictor():
    pulseData = []
    bloodPressureData = []
    bloodOxygenData = []
    timeData = []
    pulseRegression = LinearRegression()
    bloodPressureRegression = LinearRegression()
    bloodOxygenRegression = LinearRegression()

    def __init__(self):
        healthData = pd.read_csv('healthData.csv')
        self.pulseData = healthData[ 'pulse' ].values
        self.bloodPressureData = healthData['bloodpressure' ].values
        self.bloodOxygenData = healthData[ 'bloodoxygen' ].values
        self.timeData = healthData[ 'time' ].values


    def appendData(self, measurement):
        np.append(self.pulseData, measurement['pulse'] )
        np.append(self.bloodPressureData, measurement['bloodPreSys'] )
        np.append(self.bloodOxygenData, measurement['bloodOx'] )
    

    def train(self):
        pulseData  = np.array([ self.pulseData ]).T
        bloodPressureData = np.array([ self.bloodPressureData ]).T
        bloodOxygenData = np.array([ self.bloodOxygenData ]).T
        timeData = np.array([ self.timeData ]).T

        self.pulseRegression.fit( timeData, pulseData )
        self.bloodPressureRegression.fit( timeData, bloodPressureData )
        self.bloodOxygenRegression.fit( timeData, bloodOxygenData )


    def predict(self, time):
        pulsePrediction = int(self.pulseRegression.predict(np.array([[time]])))
        bloodPressurePrediction = int(self.bloodPressureRegression.predict(np.array([[time]])))
        bloodOxygenPrediction = int(self.bloodOxygenRegression.predict(np.array([[time]])))
        
        return [pulsePrediction, bloodPressurePrediction, bloodOxygenPrediction]

