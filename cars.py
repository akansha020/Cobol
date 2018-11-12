import pandas as pd
path1 = "G:\DevopsSoftwares\Dockerfiles\Python\cars.csv"
cars = pd.read_csv(path1, "rb")
print(cars)
