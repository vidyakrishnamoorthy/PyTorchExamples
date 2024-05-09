import pandas as pd

oo = pd.read_csv('../ExerciseFiles/data/olympics.csv', skiprows=4)
oo.head()

print(f"oo.Edition.value_counts(): \n {oo.Edition.value_counts()}")

print(f"oo.Gender.value_counts(ascending=True,dropna=False): \n{oo.Gender.value_counts(ascending=True,dropna=False)}")

print(f"oo[['Edition', 'Gender']].value_counts() : {oo[['Edition', 'Gender']].value_counts()}")

ath = oo.Athlete.sort_values()
print(f"ath: \n{ath}")

print(f"oo.sort_values(by=['Edition','Athlete']): \n{oo.sort_values(by=['Edition','Athlete'])}")

# boolean indexing AND&    OR|    NOT~
print(f"oo[(oo.Medal == 'Gold') & (oo.Gender == 'Women')]: \n{oo[(oo.Medal == 'Gold') & (oo.Gender == 'Women')]}")

print(f"oo[oo.Athlete.str.contains('Florence')]: \n{oo[oo.Athlete.str.contains('Florence')]}")

print(oo[oo.Athlete.str.contains('Jesse Owens')])