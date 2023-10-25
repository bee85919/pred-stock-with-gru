from modules.Save.SavePred import SavePred


def save(y, m, d):
    SavePred(date=f'{y}-{m}-{d}').merge_csv_files()


if __name__ == "__main__":
    y, m, d = 2023, 9, 30
    save(y, m, d)