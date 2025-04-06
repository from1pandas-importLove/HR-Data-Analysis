import pandas as pd
from typing import List

def create_series(foods:List[str], calories:List[int])->pd.Series:
    # write your code here ....
    return pd.Series(calories, index=foods, name='Calorie content')