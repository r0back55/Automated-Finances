import pandas as pd
import matplotlib.pyplot as plt

def run_simulation(config):
    df = pd.read_csv('data/simulation.csv')
    df['balance'] = df['balance'].cumsum()
    fig_path = 'reports/simulation_plot.png'
    plt.figure()
    plt.plot(df['month'], df['balance'])
    plt.title('Prognoza wartości portfela do 2032 r.')
    plt.xlabel('Miesiąc')
    plt.ylabel('Wartość portfela [PLN]')
    plt.savefig(fig_path)
    plt.close()
    return {'final_balance': df['balance'].iloc[-1]}, fig_path
