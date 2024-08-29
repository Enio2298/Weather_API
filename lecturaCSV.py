import pandas as pd

df = pd.read_csv("Data_exercise/dictionary.csv")
definicion = df.loc[df["word"] == input("Introduce el input: ")]["definition"]
print(definicion)

