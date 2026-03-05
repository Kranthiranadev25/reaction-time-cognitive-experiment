import pandas as pd

data = pd.read_csv("reaction_data.csv")

normal_mean = data["normal"].mean()
distraction_mean = data["distraction"].mean()

print("Average Reaction Time (Normal):", normal_mean)
print("Average Reaction Time (Distraction):", distraction_mean)
