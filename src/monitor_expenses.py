import pandas as pd
from pathlib import Path

def load_transactions(file_path: Path):
    df = pd.read_csv(file_path)
    df["Category"] = df["Description"].apply(categorize_transaction)
    return df

def categorize_transaction(desc: str) -> str:
    rules = {
        "Biedronka": "Groceries",
        "Shell": "Transport",
        "Netflix": "Entertainment",
    }
    for key, value in rules.items():
        if key.lower() in desc.lower():
            return value
    return "Other"

def summarize_expenses(df: pd.DataFrame):
    df["Date"] = pd.to_datetime(df["Date"])
    monthly = df.groupby(pd.Grouper(key="Date", freq="M"))["Amount"].sum().reset_index()
    return monthly

def alert_if_over_budget(monthly, limit=8000):
    latest = monthly.iloc[-1]["Amount"]
    if latest > limit:
        print(f"⚠️  Alert: spending {latest:.2f} exceeds limit {limit}")
