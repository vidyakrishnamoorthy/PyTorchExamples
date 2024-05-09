import pandas as pd

# We will make more sense of these two lines of code in the read_csv() video
oo = pd.read_csv('../ExerciseFiles/data/olympics.csv', skiprows=4)
print(oo.head())
#print(oo)
print(oo.columns)
print(oo.Athlete, oo.NOC, oo.Sport)
print(oo[['City','Edition','Athlete']])
print(oo.Athlete[1])
print(type(oo))
print(type(oo.City))
print(type(oo[['City','Edition','Athlete']]))

print(oo.groupby('Sport')['City'].nunique().reset_index().sort_values('City', ascending=False).reset_index())
print(oo.groupby('Sport')['City'].nunique().reset_index().sort_values('City', ascending=False).reset_index().Sport[0])

# challenge
print()