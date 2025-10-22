import pandas as pd

def analyze_expenses(config):
    df = pd.read_csv('data/expenses.csv')
    monthly_sum = df['amount'].sum()
    limit = config['expenses']['monthly_limit']
    alert = monthly_sum > limit
    summary = {
        'total_expenses': monthly_sum,
        'limit': limit,
        'alert': alert
    }
    df.to_csv('data/expenses_output.csv', index=False)
    return summary
