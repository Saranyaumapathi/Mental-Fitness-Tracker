import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

df["Mental_Fitness_Score"] = (
    df["Mood_Score"] + (10 - df["Stress_Level"]) + df["Sleep_Hours"]
) / 3

print(df)

average_scores = df.groupby("Name")["Mental_Fitness_Score"].mean()

print("\nAverage Mental Fitness Score:\n")
print(average_scores)

plt.figure()
average_scores.plot(kind="bar")
plt.xlabel("Name")
plt.ylabel("Average Mental Fitness Score")
plt.title("Mental Fitness Comparison")
plt.show()

