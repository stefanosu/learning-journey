from dataclasses import dataclass
from enum import Enum

# Build a simple trade price calculator
# Write a Python script from scratch that:

# Takes a list of trades — each trade has a stock symbol, quantity, and price
# Calculates the total value of each trade (quantity × price)
# Calculates the overall portfolio total
# Prints a clean summary

# Example input:
# trades = [
#     ("AAPL", 10, 182.50),
#     ("GOOG", 5, 140.25),
#     ("MSFT", 8, 415.00)
# ]


# Expected output:
# AAPL: 10 shares @ $182.50 = $1,825.00
# GOOG: 5 shares @ $140.25 = $701.25
# MSFT: 8 shares @ $415.00 = $3,320.00
# Total Portfolio Value: $5,846.25

class Stocks:
    def __init__(self, ticker: str, price: float, quantity: int):
        self.ticker = ticker
        self.price = price
        self.quantity = quantity

class Stock_Result:
    total_val: int


def price_calculator(trade: Stocks) -> Stock_Result:
    trade_value = trade.quantity * trade.price
    return trade_value 

trade1 = Stocks(
    ticker= "APPL",
    price= 182.50,
    quantity= 10
)

trade2 = Stocks(
    ticker= "GOOG",
    price= 140.25,
    quantity= 5
)

trade3 = Stocks(
    ticker= "MSFT",
    price= 415.00,
    quantity= 8
)

trades = [trade1, trade2, trade3]

total = 0

for trade in trades:
    print(f"{trade.ticker}: {trade.quantity} shares @ ${trade.price:.2f} = ${price_calculator(trade)}")
    total += price_calculator(trade)
print(f"Total Portfolio Value: ${total:.2f}")