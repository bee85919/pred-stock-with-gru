from keras.layers import Dense, GRU
from keras.models import Sequential
from keras.optimizers.legacy import SGD


class GRUTrainer:
    def __init__(self, idx=0, len_symbols=0):
        self.model = None
        self.idx = idx
        self.len_symbols = len_symbols


    def initialize_model(self):
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


    def train(self, X_train, y_train, X_test, sc, symbol):
        print(f"Training started for {symbol}.. [{self.idx}/{self.len_symbols}]")
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
