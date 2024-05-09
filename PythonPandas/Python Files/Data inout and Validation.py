import pandas as pd

# read_csv()
# read_excel()
# read_json()
# read_sql_table()

oo = pd.read_csv("../ExerciseFiles/data/olympics.csv", skiprows = 4)
print(oo)

print(oo.shape[0], oo.shape[1])

print(oo.head(2))

print(oo.tail(3))

print(oo.info())

print(oo.iloc[1])