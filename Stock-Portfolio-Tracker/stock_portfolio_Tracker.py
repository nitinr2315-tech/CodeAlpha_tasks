# ==========================================
# ADVANCED STOCK PORTFOLIO TRACKER
# ==========================================

import csv

# Hardcoded Stock Prices
stock_prices = {
    "AAPL": 180,    # Apple
    "TSLA": 250,    # Tesla
    "GOOGL": 140,   # Google
    "MSFT": 320,    # Microsoft
    "AMZN": 150,    # Amazon
    "META": 310,    # Meta
    "NFLX": 450,    # Netflix
    "NVDA": 900,    # Nvidia
    "AMD": 170,     # AMD
    "INTC": 35,     # Intel
    "ORCL": 120,    # Oracle
    "IBM": 190,     # IBM
    "ADBE": 550,    # Adobe
    "CRM": 270,     # Salesforce
    "UBER": 75,     # Uber
    "PYPL": 65,     # PayPal
    "SHOP": 85,     # Shopify
    "BABA": 80,     # Alibaba
    "SONY": 95,     # Sony
    "DIS": 105      # Disney
}

portfolio = {}
total_investment = 0

print("=" * 50)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 50)

print("\nAvailable Stocks:\n")

for stock, price in stock_prices.items():
    print(f"{stock:<8} : ${price}")

num_stocks = int(input("\nHow many different stocks do you own? "))

for i in range(num_stocks):
    print(f"\nStock {i+1}")

    stock_name = input("Enter Stock Symbol: ").upper()

    if stock_name not in stock_prices:
        print("❌ Stock not found in database!")
        continue

    quantity = int(input("Enter Quantity: "))

    portfolio[stock_name] = quantity

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

print("\n")
print("=" * 70)
print("PORTFOLIO SUMMARY")
print("=" * 70)

print(f"{'Stock':<10}{'Quantity':<10}{'Price($)':<12}{'Value($)':<12}")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity

    print(
        f"{stock:<10}{quantity:<10}{stock_prices[stock]:<12}{value:<12}"
    )

print("-" * 70)
print(f"TOTAL PORTFOLIO VALUE = ${total_investment}")
print("-" * 70)

# Save Data Option
save = input("\nDo you want to save the report? (yes/no): ").lower()

if save == "yes":

    # TXT Report
    with open("portfolio_report.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 50 + "\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity

            file.write(
                f"{stock} | Qty: {quantity} | "
                f"Price: ${stock_prices[stock]} | "
                f"Value: ${value}\n"
            )

        file.write("\n")
        file.write(f"Total Portfolio Value = ${total_investment}")

    # CSV Report
    with open("portfolio_report.csv", "w", newline="") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Investment Value"]
        )

        for stock, quantity in portfolio.items():
            writer.writerow(
                [
                    stock,
                    quantity,
                    stock_prices[stock],
                    stock_prices[stock] * quantity
                ]
            )

        writer.writerow([])
        writer.writerow(
            ["Total Portfolio Value", "", "", total_investment]
        )

    print("\n✅ Report saved successfully!")
    print("📄 portfolio_report.txt")
    print("📊 portfolio_report.csv")

print("\nThank you for using Stock Portfolio Tracker!")