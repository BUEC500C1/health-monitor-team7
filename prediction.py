
# Author: Elizabeth Slade

    # For my prediction algorithm, i used lqi25's healthData from team: health-monitor-HealthCover 

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class predictor():
    healthData = ""
    time = ""
    pulseData = []
    bloodPressureData = []
    bloodOxygenData = []
    timeData = []
    pulseRegression = LinearRegression()
    bloodPressureRegression = LinearRegression()
    bloodOxygenRegression = LinearRegression()

    def __init__(self):
        self.healthData = pd.read_csv('healthData.csv')
    
    def preprocessingData(self):
        pulseData = self.healthData[ 'pulse' ].values
        self.pulseData  = np.array([pulseData ]).T

        bloodPressureData = self.healthData['bloodpressure' ].values
        self.bloodPressureData = np.array([bloodPressureData]).T

        bloodOxygenData =self.healthData[ 'bloodoxygen' ].values
        self.bloodOxygenData = np.array([bloodOxygenData]).T

        timeData = self.healthData[ 'time' ].values
        self.timeData = np.array([ timeData ]).T

    def training(self):
        self.pulseRegression.fit(self.timeData,self.pulseData )
        self.bloodPressureRegression.fit(self.timeData,self.bloodPressureData)
        self.bloodOxygenRegression.fit(self.timeData,self.bloodOxygenData)

    def prediction(self, time):
        pulsePrediction = int(self.pulseRegression.predict(np.array([[time]])))
        print("Pulse Prediction: ",pulsePrediction)

        bloodPressurePrediction = int(self.bloodPressureRegression.predict(np.array([[time]])))
        print("Blood Pressure Prediction: ",bloodPressurePrediction)

        bloodOxygenPrediction = int(self.bloodOxygenRegression.predict(np.array([[time]])))
        print("Blood Oxygen Prediction: ",bloodOxygenPrediction)


p = predictor()
p.preprocessingData()
p.training()
p.prediction(5000)