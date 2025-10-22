import pandas as pd

def run_rebalancing(config):
    df = pd.read_csv('data/portfolio.csv')
    total_value = df['value'].sum()
    df['current_allocation'] = df['value'] / total_value

    target = config['portfolio']['target_allocation']
    df['target_allocation'] = df['asset'].map(target)
    df['difference'] = df['target_allocation'] - df['current_allocation']

    recommendations = df[['asset', 'value', 'current_allocation', 'target_allocation', 'difference']]
    recommendations.to_csv('data/rebalancing_output.csv', index=False)
    return recommendations
