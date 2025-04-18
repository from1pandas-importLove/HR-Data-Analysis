# your code here. the dataset is already loaded as food_calories_df.
list_of_needed_products = ['CARROTS,RAW', 'BREAD,WHEAT', 'CRANBERRIES,RAW', 'SUGARS,MAPLE', 'WATER,TAP,WELL']
result = food_calories_df[food_calories_df['Shrt_Desc'].isin(list_of_needed_products)]['Energ_Kcal'].sum()
print(result)