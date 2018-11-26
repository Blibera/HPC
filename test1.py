import pandas as pd
df = pd.read_csv("C:/Users/Slayer/Desktop/NPB_19_18_45/bt_collect.csv")
saved_column = df.User #you can also use df['column_name']

names = df.Names

print(saved_column)