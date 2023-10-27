import os
from dotenv import load_dotenv
from modules.etc.TxtReader import TxtReader
from modules.etc.SavePred import SavePred


load_dotenv()
date_path = os.getenv('date_path')


get = TxtReader().get_list
y, m, d, _ = get(date_path)


def save():
    SavePred(date=f'{y}-{m}-{d}').merge_csv_files()


if __name__ == "__main__":
    save()