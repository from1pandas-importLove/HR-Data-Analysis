import pandas as pd
from typing import Dict

def create_series(capitals:Dict[str, str])->pd.Series:
    return pd.Series(capitals, name='Capitals of the world')
