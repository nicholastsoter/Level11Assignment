import pandas as pd

videogame_data = pd.read_csv("video_games_raw.csv")

#Select a game
select = int(input("Choose a selected game: "))
print("Selected Game: ")
print(videogame_data.iloc[select])
print()

#Add column and change data
videogame_data["Recommended"] = "No"
videogame_data.loc[
    (videogame_data["Rating"] >= 8) & (videogame_data["Price"] <= 40),
    "Recommended"
] = "Yes"

#Alter status for selected game
status = input("Set a new status: ")
videogame_data.at[select, "Status"] = status

#Sort by spec
recommended_games = videogame_data.query("Recommended == 'Yes'")
print(recommended_games)

#Create new CSV
videogame_data.to_csv('video_games_cleaned.csv', index = False)
print("\nThe catalog has been updated.")
print("Saved as video_games_cleaned.csv")