import pandas as pd

def drop_record(olympics:pd.Series)->pd.Series:
    new_olympics = olympics.drop(index=2020)
    return  new_olympics