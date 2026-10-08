# DAY 2 - BUG FILE 5 of 6
import numpy as np
import pandas as pd

df = pd.read_csv("day02_usage.csv")
day = df["Day"].to_numpy()
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

# "How many minutes of Video did I watch on weekends only?"
weekend_video = 0
for i in range(len(day)):
    if day[i] % 7 == 6 or day[i] % 7 == 0:
        weekend_video = video[i]

print("Weekend Video minutes:", weekend_video)
print("Weekday Video minutes:", video.sum() - weekend_video)
