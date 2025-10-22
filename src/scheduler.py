import schedule
import time
from pathlib import Path
from monitor_expenses import load_transactions, summarize_expenses, alert_if_over_budget
from portfolio_rebalance import rebalance
from forecast_model import forecast_investment
from generate_report import generate_report

def monthly_job():
    print("Running monthly finance automation...")

    # 1. Monitor wydatków
    transactions = Path("data/transactions/transactions_2025_10.csv")
    df_tx = load_transactions(transactions)
    summary = summarize_expenses(df_tx)
    alert_if_over_budget(summary)

    # 2. Rebalancing
    holdings = Path("data/portfolio/holdings_2025_Q4.csv")
    rebalance_result = rebalance(holdings)

    # 3. Prognoza
    forecast = forecast_investment()

    # 4. Raport
    summary_text = f"Expenses summary: {summary.tail(1).to_dict()}<br/>Rebalancing: {rebalance_result.to_dict('records')[:3]}"
    generate_report(summary_text)

schedule.every().month.do(monthly_job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)
