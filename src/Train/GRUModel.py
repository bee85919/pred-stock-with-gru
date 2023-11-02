from keras.layers import Dense, GRU
from keras.models import Sequential
from keras.optimizers.legacy import SGD


class GRUModel:
    
    def __init__(self, X_train, y_train, X_test, sc, sym, i=0, size=0):
        model = self.initialize()
        pred = self.train()
        return pred


    def initialize(self):        
        model = Sequential()        
        model.add(GRU(units=50, 
                           return_sequences=True, 
                           activation='tanh'))        
        model.add(GRU(units=50, activation='tanh'))        
        model.add(Dense(units=2))        
        
        self.model.compile(optimizer=SGD(learning_rate=0.01, 
                                         decay=1e-7, 
                                         momentum=0.9, 
                                         nesterov=False), 
                           loss='mean_squared_error')
        return model


    def train(self, X_train, y_train, X_test, sc, model, sym, i, size):        
        print(f"Training for {sym}.. [{i}/{size}]")        
        self.model.fit(X_train, 
                       y_train, 
                       epochs=50, 
                       batch_size=100, 
                       verbose=0)
        # pred
        pred = self.model.predict(X_test)        
        pred = sc.inverse_transform(pred)
        return pred
    

    def get_model(self):        
        return self.model
