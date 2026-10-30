
data = float(input("Enter required data (GB): "))
calls = int(input("Enter required call minutes: "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget: "))

plans = [
    {"name": "Basic", "price": 199, "data": 2,
     "calls": 200, "days": 28, "extra_data": 20,
     "extra_call": 1},

    {"name": "Smart", "price": 299, "data": 4,
     "calls": 500, "days": 28, "extra_data": 15,
     "extra_call": 0.5},

    {"name": "Premium", "price": 399, "data": 8,
     "calls": 1000, "days": 56, "extra_data": 10,
     "extra_call": 0.5},

    {"name": "Unlimited", "price": 599, "data": 15,
     "calls": 1500, "days": 84, "extra_data": 5,
     "extra_call": 0.25}
]

eligible = []

print("\n--- Mobile Plan Comparison ---")

for p in plans:
    excess_data = max(0, data - p["data"])
    excess_calls = max(0, calls - p["calls"])

    extra_cost = (excess_data * p["extra_data"] +
                  excess_calls * p["extra_call"])

    total = p["price"] + extra_cost

    print("\nPlan:", p["name"])
    print("Base Price:", p["price"])
    print("Extra Charges:", extra_cost)
    print("Total Cost:", total)

    if (p["data"] >= data and
        p["calls"] >= calls and
        p["days"] >= validity and
        total <= budget):

        eligible.append((total, p["name"]))

if eligible:
    best = min(eligible)

    print("\n--- Best Economical Plan ---")
    print("Plan Name:", best[1])
    print("Total Cost: Rs.", best[0])
else:
    print("\nNo eligible plan found!")

print("\nOptimization Completed.")

