import numpy as np

class Logger:
    
    @staticmethod
    def log(log, symbol, X_train, X_test, y_train, sc, pred_df):        
        log_message = f"""
                        Symbol ({symbol}) processed.
                        
                        Shape:
                        - X_train : {X_modules.Train.shape}
                        - y_train : {y_modules.Train.shape}
                        - X_test : {X_test.shape}
                        
                        sc: 
                        - min_   : {sc.min_}
                        - scale_ : {sc.scale_}
                        
                        NaN:
                        - X_train : {np.isnan(X_train).sum()}
                        - y_train : {np.isnan(y_train).sum()}
                        - X_test  : {np.isnan(X_test).sum()}
                        - pred_df : {pred_df.isna().sum().sum()}
                    """                    
        with open(log, 'a') as f:                                    
            f.write(log_message)
            

    @staticmethod
    def err(log, symbol):        
        log_message = f"""
                        {symbol} doesn't exist.\n
                    """                    
        with open(log, 'a') as f:            
            f.write(log_message)
