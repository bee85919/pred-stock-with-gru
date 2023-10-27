import ast

class TxtReader:
    @staticmethod
    def get_list(file_path):
        with open(file_path, 'r') as f:
            string = f.read()
        lst = ast.literal_eval(string.strip())
        return lst