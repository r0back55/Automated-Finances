import pandas as pd
import numpy as np

def forecast_investment(monthly_contrib=10000, annual_return=0.06, years=7, growth_rate=0.05):
    months = years * 12
    balances = []
    balance = 0
    contrib = monthly_contrib

    for m in range(1, months + 1):
        balance *= (1 + annual_return / 12)
        balance += contrib
        if m % 12 == 0:
            contrib *= (1 + growth_rate)
        balances.append(balance)

    df = pd.DataFrame({"Month": range(1, months + 1), "Balance": balances})
    return df
