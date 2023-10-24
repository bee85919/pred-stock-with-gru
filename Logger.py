import numpy as np

class Logger:
    @staticmethod
    def log(log_file, symbol, X_train, X_test, y_train, sc, pred_df):
        log_message = f"""
                        Symbol ({symbol}) processed.\n
                        Shape:
                        - X_train : {X_train.shape}\n
                        - y_train : {y_train.shape}\n
                        - X_test : {X_test.shape}\n
                        sc: 
                        - min_   : {sc.min_}\n
                        - scale_ : {sc.scale_}\n
                        NaN:
                        - X_train : {np.isnan(X_train).sum()}\n
                        - y_train : {np.isnan(y_train).sum()}\n
                        - X_test  : {np.isnan(X_test).sum()}\n
                        - pred_df : {pred_df.isna().sum().sum()}\n
                    """
        with open(log_file, 'a') as f:
            f.write(log_message)
            

    @staticmethod
    def err(log_file, symbol):
        log_message = f"""
                        {symbol} doesn't exist.\n
                    """
        with open(log_file, 'a') as f:
            f.write(log_message)
