

products = ["Laptop", "Mobile", "Tablet", "Headphones"]

prices = [
    [40000, 42000, 45000, 48000],
    [15000, 14000, 16000, 18000],
    [20000, 21000, 20500, 22000],
    [2000, 2500, 3000, 2800]
]

threshold = float(input("Enter fluctuation threshold (%): "))

flagged = []
results = []

print("\n--- PRODUCT PRICE ANALYSIS ---")

for i in range(len(products)):

    changes = []

    for j in range(1, len(prices[i])):
        change = ((prices[i][j] - prices[i][j-1])
                  / prices[i][j-1]) * 100
        changes.append(change)

    maximum = max(changes)
    minimum = min(changes)

    fluctuation = max(abs(x) for x in changes)

    print("\nProduct:", products[i])
    print("Historical Prices:", prices[i])
    print("Percentage Changes:",
          [round(x, 2) for x in changes])
    print("Maximum Increase:", round(maximum, 2), "%")
    print("Maximum Decrease:", round(minimum, 2), "%")
    print("Maximum Fluctuation:", round(fluctuation, 2), "%")

    results.append((products[i], fluctuation))

    if fluctuation > threshold:
        flagged.append(products[i])
        print("Status: High Fluctuation")
    else:
        print("Status: Normal")

highest = max(results, key=lambda x: x[1])

print("\n--- FINAL REPORT ---")
print("Flagged Products:", flagged)
print("Highest Fluctuation Product:", highest[0])
print("Highest Fluctuation:", round(highest[1], 2), "%")

print("\nPrice Analysis Completed.")

