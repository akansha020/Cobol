import pandas as pd
import numpy as np

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns =['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df.to_csv('G:\DevopsSoftwares\Dockerfiles\Python\example.csv')

rd = pd.read_csv('G:\DevopsSoftwares\Dockerfiles\Python\example.csv',index_col='FIRST_NAME', names =['UID','FIRST_NAME', 'LAST_NAME', 'AGE', 'PRETESTSCORE','POSTTESTSCORE'])
print(rd.iloc[2])
print(rd.loc['Jason'])

