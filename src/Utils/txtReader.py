import ast


class txtReader:
    @staticmethod
    def get_list(file_path):
        with open(file_path, 'r') as f:
            string = f.read()
        lst = ast.literal_eval(string.strip()) # 보안 이슈로 literal_eval 사용
        return lst