# DAY 2 - BUG FILE 4 of 6
import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

# "How did week 1 (days 1 to 7) compare with week 2 (days 8 to 14)?"
week1 = chat[0:6] + video[0:6] + study[0:6] + games[0:6]
week2 = chat[7:14] + video[7:14] + study[7:14] + games[7:14]

print("Week 1 total minutes:", week1.sum())
print("Week 2 total minutes:", week2.sum())
print("Change:", week2.sum() - week1.sum())
