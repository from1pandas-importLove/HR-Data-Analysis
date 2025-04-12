import pandas as pd

def merge_data(user_info : pd.DataFrame, emails : pd.DataFrame) -> pd.DataFrame:
    return user_info.merge(emails)