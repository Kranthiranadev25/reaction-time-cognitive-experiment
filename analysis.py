import pandas as pd

data = pd.read_csv("reaction_data.csv")

normal_mean = data["normal"].mean()
distraction_mean = data["distraction"].mean()

normal_std = data["normal"].std()
distraction_std = data["distraction"].std()

print("Average Reaction Time (Normal):", normal_mean)
print("Average Reaction Time (Distraction):", distraction_mean)

print("Standard Deviation (Normal):", normal_std)
print("Standard Deviation (Distraction):", distraction_std)
