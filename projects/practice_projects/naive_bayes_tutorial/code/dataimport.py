'''
Solution
'''

import pandas as pd

# Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
DF = pd.read_table('smsspamcollection/SMSSpamCollection',
sep='\t', 
names=cols)

# Output printing out first 5 columns
THING = DF.head()
print(THING.values[0])