#Part A 
import pandas as pd
import numpy as np

df = pd.read_csv('day02_usage.csv')

chat = df['Chat'].to_numpy()
video = df['Video'].to_numpy()
study = df['Study'].to_numpy()
games = df['Games'].to_numpy()

#Part B
print("Total minutes over the thirty days:" , chat.sum() , video.sum() , study.sum() , games.sum())

#mean round to 1 decimal places
print("Mean minutes over the thirty days:" , round(chat.mean(), 1) , round(video.mean(), 1) , round(study.mean(), 1) , round(games.mean(), 1))
    
#Part C — One derived measure
balance = study - games

print(f"best day for study vs games: {int(balance.argmax())+1} with a balance of {balance.max()} minutes")

#Part D — Now the question changes direction
#D1 which app won each day
names = ["Chat", "Video", "Study", "Games"]
winners = []
for i in range(len(chat)):
    day_values = [chat[i], video[i], study[i], games[i]]   
    # rebuild a row by hand
    best = 0
    for j in range(1, 4):
        if day_values[j] > day_values[best]:
            best = j
    winners.append(names[best])

    '''Alernative for D1
    for i in range(len(df)):
        list = np.array([chat[i],video[i],study[i],games[i]])
        idx = int(list.argmax())
        print(names[idx])'''

#D2. What share of each day did each app take?    

app_totals = chat + video + study + games 

chat_share = (chat/app_totals)*100
video_share = (video/app_totals)*100
study_share = (study/app_totals)*100
games_share = (games/app_totals)*100

#chatgpt_share = (gpt/app_totals)*100

print("\nDay 1 shares:",
      round(chat_share[0], 1), round(video_share[0], 1),
      round(study_share[0], 1), round(games_share[0]))
