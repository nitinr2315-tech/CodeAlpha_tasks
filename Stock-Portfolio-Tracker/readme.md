# 📈 Stock Portfolio Tracker

## Overview

Stock Portfolio Tracker is a Python-based application that helps users calculate the total value of their stock investments. The program uses a predefined database of stock prices, allows users to enter stock quantities, and generates portfolio reports in both TXT and CSV formats.

---

## Features

* User-friendly command-line interface
* Predefined stock price database
* Portfolio value calculation
* Investment summary display
* TXT report generation
* CSV report generation
* Invalid stock symbol handling
* Supports multiple stocks in a portfolio

---

## Technologies Used

* Python 3
* Dictionary Data Structure
* Loops and Conditional Statements
* File Handling
* CSV Module

---

## Available Stocks

| Stock Symbol | Company    |
| ------------ | ---------- |
| AAPL         | Apple      |
| TSLA         | Tesla      |
| GOOGL        | Google     |
| MSFT         | Microsoft  |
| AMZN         | Amazon     |
| META         | Meta       |
| NFLX         | Netflix    |
| NVDA         | Nvidia     |
| AMD          | AMD        |
| INTC         | Intel      |
| ORCL         | Oracle     |
| IBM          | IBM        |
| ADBE         | Adobe      |
| CRM          | Salesforce |
| UBER         | Uber       |
| PYPL         | PayPal     |
| SHOP         | Shopify    |
| BABA         | Alibaba    |
| SONY         | Sony       |
| DIS          | Disney     |

---

## Project Structure

```text
StockPortfolioTracker/
│
├── stock_portfolio_tracker.py
├── portfolio_report.txt
├── portfolio_report.csv
└── README.md
```

---

## How to Run

### Step 1: Open Terminal / PowerShell

Navigate to the project directory:

```bash
cd path/to/project
```

### Step 2: Run the Program

```bash
python stock_portfolio_tracker.py
```

or

```bash
py stock_portfolio_tracker.py
```

---

## Sample Execution

```text
How many different stocks do you own? 3

Enter Stock Symbol: AAPL
Enter Quantity: 10

Enter Stock Symbol: TSLA
Enter Quantity: 5

Enter Stock Symbol: NVDA
Enter Quantity: 2
```

### Output

```text
PORTFOLIO SUMMARY

Stock     Quantity   Price($)   Value($)
AAPL      10         180        1800
TSLA      5          250        1250
NVDA      2          900        1800

TOTAL PORTFOLIO VALUE = $4850
```

---

## Generated Files

After saving the report, the program creates:

### portfolio_report.txt

Contains a text-based summary of the portfolio.

### portfolio_report.csv

Contains portfolio data in CSV format for spreadsheet applications such as Microsoft Excel.

---

## Learning Concepts Demonstrated

* Dictionaries
* User Input and Output
* Loops
* Conditional Statements
* Arithmetic Operations
* File Handling
* CSV Processing

---

## Future Improvements

* Real-time stock price integration
* Profit/Loss calculation
* Portfolio performance analysis
* Graphical User Interface (GUI)
* Database integration

---

## Author

**Nitin Rajawat**

B.Tech (Artificial Intelligence & Data Science)

CodeAlpha Python Programming Internship Project
