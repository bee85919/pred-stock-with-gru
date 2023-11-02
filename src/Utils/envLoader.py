import os
from dotenv import load_dotenv


load_dotenv()


class envLoader:
    def __init__(self):
        self.base = self.dir_name(3)
        
        
    def dir_name(n):
        path = os.path.abspath(__file__)
        for _ in range(n): path = os.path.dirname(path)
        return path
        

    def get_path(self, env):
        env_path = os.getenv(env)
        return os.path.join(self.base, env_path) if os.getenv(env) else None
    

    def path(self):
        get = self.get_path
        path = {
            'csvs': get('csvs_path'),
            'date': get('date_path'),
            'syms': get('syms_path'),
            'syms_lnth_path': get('syms_lnth_path'),
            'data': get('data_path'),
            'logs': get('logs_path'),
            'prep': get('prep_path'),
            'pred': get('pred_path'),
            'test': get('test_path'),
            'train': get('train_path'),
            'result': get('result_path')
        }
        return path