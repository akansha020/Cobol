dict = {"country" : ["Brazil", "Russia" , "India" , "China", "South Africa"],
        "capital" : ["Brasilia" , "Moscow" , "New Delhi", "Beijing" , "Pretoria"],
        "area" : [8.56, 7.89, 56.56, 758.66, 553.78],
        "population" : [200.4, 143.5, 123.5, 241.7, 543.7] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
        
