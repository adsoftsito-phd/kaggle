import pandas as pd

serie1 = pd.Series([1, 2, 3, 4, 5])
print(serie1)

serie2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print('\n')
print(serie2)
