import pandas as pd

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")
print (wine_reviews)
print (wine_reviews.shape)
print (wine_reviews.shape[0])
print (wine_reviews.shape[1])
print ('\n\t head \n')
print (wine_reviews.head)

wine_reviews.to_csv('wines.csv')
