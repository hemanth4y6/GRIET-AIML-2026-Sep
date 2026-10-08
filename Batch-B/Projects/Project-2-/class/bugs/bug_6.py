# DAY 2 - BUG FILE 6 of 6
# Hardest. Runs, prints, looks reasonable, answers the WRONG question.
import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
day = df["Day"].to_numpy()
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

# "On which day did Study beat Games by the largest margin?"
study_advantage = games - study
best = study_advantage.argmax()

print("Best study day:", day[best])
print("Study minutes that day:", study[best])
print("Games minutes that day:", games[best])
print("Margin:", study_advantage[best])
