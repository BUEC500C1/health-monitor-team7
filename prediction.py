
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
        self.timeData = self.healthData.loc[ 0:self.healthData[ 'time' ].size-1,'time' ].values
    
    def preprocessingData(self):
        pulseData = self.healthData.loc[ 0:self.healthData[ 'pulse' ].size-1,'pulse'].values
        self.pulseData  = np.array([pulseData ]).T

        bloodPressureData = self.healthData.loc[ 0:self.healthData[ 'bloodpressure' ].size-1,'bloodpressure'].values
        self.bloodPressureData = np.array([bloodPressureData]).T

        bloodOxygenData =self.healthData.loc[ 0:self.healthData[ 'bloodoxygen' ].size-1,'bloodoxygen' ].values
        self.bloodOxygenData = np.array([bloodOxygenData]).T

        self.timeData = np.array([ self.timeData ]).T

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