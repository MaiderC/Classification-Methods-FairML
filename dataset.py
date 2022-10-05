import pandas as pd

df = pd.read_csv("data/compas-scores-raw.csv")

def empiric_probs(col_y, val_y, col_a, val_a):
    n = len(df[df["ScoreText"] == "High"])
    a = len(df[(df["ScoreText"] == "High") & (df["Ethnic_Code_Text"] == "African-American")])
    b = len(df[(df["ScoreText"] == "High") & (df["Ethnic_Code_Text"] != "African-American")])

    print(f"* p({col_y}={val_y}|{col_a}={val_a})  = {a/n}")
    print(f"* p({col_y}={val_y}|{col_a}=!({val_a})) = {b/n}")

empiric_probs("ScoreText", "High", "Ethnic_Code_Text", "African-American")
