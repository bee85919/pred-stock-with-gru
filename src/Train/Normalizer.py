from sklearn.preprocessing import MinMaxScaler 
import numpy as np


arr = np.array
rsh = np.reshape


class Normalizer:            
    
    def __init__(self, train_data, test_data, step, period):        
        train_ts, test_ts = self.get_ts(train_data, test_data)
        sc, sc_train_ts = self.scale(train_ts, (0,1))
        X_train, y_train = self.get_ts_set(sc_train_ts, train_ts, step, period)
        inputs = self.input(train_ts, test_ts, step, sc)
        X_test = self.get_test(inputs, step, period)
        return X_train, y_train, X_test, sc
    
    
    def get_ts(self, train_data, test_data):
        train_ts = train_data.iloc[:, 1:2].values
        test_ts = test_data.iloc[:, 1:2].values
        return train_ts, test_ts
    
    
    def scale(self, train_ts, range=(0,1)):
        sc = MinMaxScaler(feature_range=range)
        sc_train_ts = sc.fit_transform(train_ts)
        return sc, sc_train_ts
    
    
    def get_ts_set(self, sc_train_ts, train_ts, s, p):
        X_train = []
        y_train = []
        for i in range(s, len(train_ts)-1):
            X_train.append(sc_train_ts[i-s:i, 0])
            y_train.append(sc_train_ts[i:i+p, 0])
        X_train = arr(X_train)
        y_train = arr(y_train)
        X_train = rsh(X_train, (X_train.shape[0], X_train.shape[1], 1))
        return X_train, y_train
    
    
    def input(self, train_ts, test_ts, step, sc):
        inputs = np.concatenate((train_ts, test_ts), axis=0)
        inputs = inputs[len(inputs)-len(test_ts)-step:]
        inputs = sc.transform(inputs.reshape(-1,1))
        return inputs
    
    
    def get_test(self, inputs, s, p):
        X_test = []
        for i in range(s, len(inputs) + s - p):
            X_test.append(inputs[i-s:i,0])
        X_test = arr(X_test)
        X_test = rsh(X_test, (X_test.shape[0], X_test.shape[1], 1))
        return X_test