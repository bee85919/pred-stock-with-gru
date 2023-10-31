import os
from dotenv import load_dotenv


class envLoader:
    def __init__(self):
        load_dotenv()
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        

    def get_path(self, env_var):
        relative_path = os.getenv(env_var)
        if relative_path is None:
            return None
        return os.path.join(self.base_path, relative_path)
    

    def path(self):
        path = {
            'csv_path': self.get_path('csv_path'),
            'date_path': self.get_path('date_path'),
            'symbols_path': self.get_path('symbols_path'),
            'symbols_length_path': self.get_path('symbols_length_path'),
            'logs_path': self.get_path('logs_path'),
            'prep_path': self.get_path('prep_path'),
            'pred_path': self.get_path('pred_path'),
            'train_path': self.get_path('train_path'),
            'test_path': self.get_path('test_path'),
            'result_path': self.get_path('result_path'),
            'data_path': self.get_path('data_path')
        }
        return path