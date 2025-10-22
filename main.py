import yaml
from pathlib import Path
from finance.rebalancing import run_rebalancing
from finance.expenses import analyze_expenses
from finance.simulation import run_simulation
from reports.report_generator import generate_report

def load_config():
    config_path = Path("config.yaml")
    if not config_path.exists():
        raise FileNotFoundError("Brak pliku config.yaml w katalogu głównym projektu.")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    print("=== Personal Finance Automation ===")
    config = load_config()

    Path(config["report"]["output_dir"]).mkdir(parents=True, exist_ok=True)

    print("[1/3] Analiza portfela inwestycyjnego...")
    rebalancing_summary = run_rebalancing(config)

    print("[2/3] Analiza wydatków miesięcznych...")
    expenses_summary = analyze_expenses(config)

    print("[3/3] Symulacja długoterminowa...")
    simulation_summary, fig_path = run_simulation(config)

    print("Generowanie raportu PDF...")
    generate_report(config, rebalancing_summary, expenses_summary, simulation_summary, fig_path)

    print("✅ Raport wygenerowany pomyślnie i zapisany w folderze:", config["report"]["output_dir"])

if __name__ == "__main__":
    main()
