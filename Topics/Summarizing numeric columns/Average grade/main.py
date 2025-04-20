# Your code here. The DataFrame is already loaded as grades
result = grades.mean(axis='columns', numeric_only=True)
print(result)