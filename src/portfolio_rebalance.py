import pandas as pd
from .config_loader import load_config

def rebalance(holdings_file):
    config = load_config()
    target = config["target_allocation"]

    df = pd.read_csv(holdings_file)
    df["CurrentWeight"] = df["Value"] / df["Value"].sum()

    df["TargetWeight"] = df["Asset"].map(target)
    df["Diff"] = df["TargetWeight"] - df["CurrentWeight"]

    df["Action"] = df["Diff"].apply(
        lambda x: "Buy" if x > 0.01 else ("Sell" if x < -0.01 else "Hold")
    )
    return df[["Asset", "CurrentWeight", "TargetWeight", "Diff", "Action"]]
