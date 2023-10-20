from keras.layers import Dense, GRU
from keras.models import Sequential
from keras.optimizers.legacy import SGD

class GRUTrainer:
    def __init__(self):
        self.model = Sequential()
        self.model.add(GRU(units=50, 
                           return_sequences=True, 
                           activation='tanh'))
        self.model.add(GRU(units=50, activation='tanh'))
        self.model.add(Dense(units=2))
        
        # Compiling the RNN 
        self.model.compile(optimizer=SGD(learning_rate=0.01, 
                                         decay=1e-7, 
                                         momentum=0.9, 
                                         nesterov=False), 
                           loss='mean_squared_error')


    def train(self, X_train, y_train, X_test, sc):
        # Fitting to the training set 
        self.model.fit(X_train, 
                       y_train, 
                       epochs=50, 
                       batch_size=50, 
                       verbose=1)

        # pred
        pred = self.model.predict(X_test)
        pred = sc.inverse_transform(pred)

        return pred
    

    def get_model(self):
        return self.model
