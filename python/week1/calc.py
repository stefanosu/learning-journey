from dataclasses import dataclass
from enum import Enum

# Build a trade price calculator that:

# Creates at least 3 stock trades with ticker, price, and quantity
# Calculates each trade's total value
# Prints a formatted summary line per trade
# Prints the total portfolio value at the end

# Expected output:
# AAPL: 10 shares @ $182.50 = $1,825.00
# GOOG: 5 shares @ $140.25 = $701.25
# MSFT: 8 shares @ $415.00 = $3,320.00
# Total Portfolio Value: $5,846.25


@dataclass
class Stocks:
    ticker: str
    quantity: int
    price: int 


def price_calculator(trade: Stocks):
    return trade.quantity * trade.price


trade1 = Stocks(
ticker = "AAPL",
quantity= 10,
price = 182.50
)


trade2 = Stocks(
ticker = "GOOG",
quantity= 5,
price = 140.25
)


trade3 = Stocks(
ticker = "MSFT",
quantity= 8,
price = 415.00
)

trades = [trade1, trade2, trade3]

total = 0

for trade in trades:
        print(f"{trade.ticker}: {trade.quantity} shares @ ${trade.price:.2f} = ${price_calculator(trade):.2f}")
        total += price_calculator(trade)
print(f"The total portfolio value: ${total:.2f}")








