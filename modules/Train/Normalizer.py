from sklearn.preprocessing import MinMaxScaler 
import numpy as np

class Normalizer:
    def __init__(self, train_data, test_data, time_steps, for_periods):
        self.train_data = train_data
        self.test_data = test_data
        self.time_steps = time_steps
        self.for_periods = for_periods
        self.X_train, self.y_train, self.X_test, self.sc = self.normalize()

    def normalize(self):
        ts_train = self.train_data.iloc[:,1:2].values
        ts_test = self.test_data.iloc[:,1:2].values

        sc = MinMaxScaler(feature_range=(0,1))
        ts_train_scaled = sc.fit_transform(ts_train)

        X_train, y_train = [], []
        for i in range(self.time_steps, len(ts_train)-1):
            X_modules.Train.append(ts_train_scaled[i-self.time_steps:i, 0])
            y_modules.Train.append(ts_train_scaled[i:i+self.for_periods, 0])
        X_train, y_train = np.array(X_train), np.array(y_train)
        X_train = np.reshape(X_train, (X_modules.Train.shape[0], X_modules.Train.shape[1], 1))

        inputs = np.concatenate((ts_train, ts_test), axis=0)
        inputs = inputs[len(inputs)-len(ts_test)-self.time_steps:]
        inputs = sc.transform(inputs.reshape(-1,1))

        X_test = []
        for i in range(self.time_steps, len(ts_test) + self.time_steps - self.for_periods):
            X_test.append(inputs[i-self.time_steps:i,0])
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        
        return X_train, y_train, X_test, sc