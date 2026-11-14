# Portfolio Tracker
# Maine ye apne stocks ka profit/loss check karne ke liye banaya hai

import csv

print("=== Stock Portfolio Performance Tracker ===")
print("")

# yahan pe hum saare stocks save karenge
stocks = []

# pehle user se input lena hai
while True:
    ticker = input("Ticker: ")
    if ticker == "":
        break
    ticker = ticker.upper()

    buy_price = float(input("Buy Price: "))
    shares = int(input("Shares: "))
    print("")

    stocks.append([ticker, buy_price, shares])

if len(stocks) == 0:
    print("Koi stock add nahi kiya.")
else:
    # ab csv file se current price dhoondne ki koshish karenge
    prices = {}
    try:
        file = open("sp500_prices.csv")
        reader = csv.DictReader(file)
        for row in reader:
            # csv me alag alag naam ho sakte hain, is liye dono check kiye
            t = row.get("Ticker") or row.get("Symbol") or row.get("ticker")
            p = row.get("Price") or row.get("Close") or row.get("price")
            if t and p:
                prices[t.upper()] = float(p)
        file.close()
        print("CSV file mil gayi.")
    except:
        print("CSV file nahi mili, is liye current price khud se puchenge.")

    print("\n--- Result ---")
    total_cost = 0
    total_value = 0

    for s in stocks:
        ticker = s[0]
        buy = s[1]
        share = s[2]
        cost = buy * share

        # agar price csv me mil gayi to wo, warna user se puch lo
        if ticker in prices:
            current = prices[ticker]
        else:
            current = float(input(f"{ticker} ki current price kya hai? "))

        value = current * share
        profit = value - cost
        percent = (profit / cost) * 100 if cost != 0 else 0

        print(f"{ticker} | Cost: {cost} | Abhi: {value} | Profit: {profit} | {percent:.2f}%")

        total_cost = total_cost + cost
        total_value = total_value + value

    print("\nTotal Cost:", total_cost)
    print("Total Value:", total_value)
    print("Total Profit:", total_value - total_cost)