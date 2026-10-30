

households = []
total_revenue = 0

fixed_fee = 50
penalty_rate = 100
limit = 5000

def calculate_bill(units):
    charge = 0

    if units <= 1000:
        charge = units * 0.02

    elif units <= 3000:
        charge = 1000 * 0.02
        charge += (units - 1000) * 0.04

    elif units <= 5000:
        charge = 1000 * 0.02
        charge += 2000 * 0.04
        charge += (units - 3000) * 0.06

    else:
        charge = 1000 * 0.02
        charge += 2000 * 0.04
        charge += 2000 * 0.06
        charge += (units - 5000) * 0.08

    return charge

n = int(input("Enter number of households: "))

for i in range(n):
    print("\nHousehold", i + 1)

    name = input("Enter household name: ")
    usage = int(input("Enter water usage (litres): "))

    if usage < 0:
        print("Invalid water usage!")
        continue

    water_charge = calculate_bill(usage)
    penalty = 0

    if usage > limit:
        penalty = penalty_rate

    bill = water_charge + fixed_fee + penalty
    total_revenue += bill

    households.append((name, usage, bill))

    print("Water Charge: Rs.", round(water_charge, 2))
    print("Fixed Fee: Rs.", fixed_fee)
    print("Penalty: Rs.", penalty)
    print("Total Bill: Rs.", round(bill, 2))

print("\n--- HOUSEHOLD COMPARISON ---")

for h in households:
    print(h[0], "- Usage:", h[1], "litres")

    if h[1] > limit:
        print("Status: Excessive Usage")
    else:
        print("Status: Normal Usage")

if households:
    highest = max(households, key=lambda x: x[1])

    print("\nHighest Consumption:")
    print("Household:", highest[0])
    print("Usage:", highest[1], "litres")

print("\nTotal Revenue: Rs.", round(total_revenue, 2))
print("Analysis Completed.")

