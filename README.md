# Personal Finance Automation

Automatyzacja analizy finansów osobistych, inwestycji oraz generowania raportów PDF.

## 📂 Struktura projektu

```
personal_finance_automation/
├── main.py                  # Plik startowy projektu
├── config.yaml              # Konfiguracja projektu
├── requirements.txt         # Wymagane biblioteki Python
├── finance/
│   ├── rebalancing.py       # Analiza portfela i rekomendacje
│   ├── expenses.py          # Analiza wydatków
│   └── simulation.py        # Symulacje finansowe
├── reports/
│   └── report_generator.py  # Generowanie raportów PDF
├── data/
│   ├── portfolio.csv        # Dane portfela inwestycyjnego
│   ├── expenses.csv         # Dane wydatków
│   └── simulation.csv       # Dane do symulacji
└── fonts/
    └── DejaVuSans.ttf       # Czcionka Unicode do PDF
```

## 🚀 Uruchamianie przykładowego raportu

1. Aktywuj środowisko wirtualne:

```powershell
python -m venv venv
.env\Scripts\Activate
pip install -r requirements.txt
```

2. Uruchom projekt:

```powershell
python main.py
```

3. Raport PDF zostanie wygenerowany w folderze `reports/` jako `monthly_report.pdf`.  
   Zawiera:
   - podsumowanie portfela inwestycyjnego,
   - analizę wydatków miesięcznych,
   - symulację długoterminową i wykres.

## 📊 Przykładowe dane

### data/portfolio.csv

| asset | value |
|-------|-------|
| etf   | 75000 |
| bonds | 15000 |
| crypto| 10000 |

### data/expenses.csv

| category       | amount |
|----------------|--------|
| food           | 2000   |
| rent           | 3000   |
| transport      | 800    |
| entertainment  | 900    |
| subscriptions  | 300    |
| misc           | 500    |

### data/simulation.csv

| month | balance |
|-------|---------|
| 1     | 10000   |
| 2     | 10200   |
| 3     | 10450   |
| 4     | 10700   |
| 5     | 11000   |
