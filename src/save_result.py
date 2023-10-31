import os
from dotenv import load_dotenv
from Utils.envLoader import envLoader
from Utils.SavePred import SavePred
from Utils.txtReader import txtReader


get_path = envLoader().get_path
date_path = get_path('date_path')


get_list = txtReader().get_list
y, m, d, _ = get_list(date_path)


def save():
    SavePred(date=f'{y}-{m}-{d}').merge_csv_files()


if __name__ == "__main__":
    save()