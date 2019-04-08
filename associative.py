

import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd  
from apyori import apriori

#from google.colab import drive
#drive.mount('/content/drive')
data = pd.read_csv('store_data.csv')  
data

records = []  
for i in range(0, 20):  
    records.append([str(data.values[i,j]) for j in range(0, 20)])
print (records[0:4])

association_rules = apriori(records, min_support=0.0050, min_confidence=0.35, min_lift=3,min_length=1)  
association_results = list(association_rules)  
association_results

for item in association_results:

    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    print("Support: " + str(item[1]))


    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
