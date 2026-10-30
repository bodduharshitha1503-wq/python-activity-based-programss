
print("TELECOMMUNICATION COST OPTIMIZATION")

data = float(input("Enter required data (GB): "))
calls = int(input("Enter required calls (minutes): "))
validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget: "))

n = int(input("Enter number of mobile plans: "))
plans = []
for i in range(n):
    print("\nEnter Plan", i + 1, "details")
    name = input("Plan name: ")
    cost = float(input("Plan cost: "))
    pdata = float(input("Data limit (GB): "))
    pcalls = int(input("Call limit (minutes): "))
    days = int(input("Validity (days): "))
    dcharge = float(input("Extra data charge per GB: "))
    ccharge = float(input("Extra call charge per minute: "))

    extra_data = max(0, data - pdata)
    extra_calls = max(0, calls - pcalls)

    total = cost + extra_data * dcharge
    total += extra_calls * ccharge

    if days >= validity and total <= budget:
        plans.append((total, name, extra_data, extra_calls))

if plans:
    plans.sort()
    print("\nEligible Mobile Plans:")
    for p in plans:
        print(p[1], "Total Cost:", p[0])
        print("Extra Data:", p[2], "GB")
        print("Extra Calls:", p[3], "minutes")

    best = plans[0]
    print("\nMost Economical Plan:", best[1])
    print("Minimum Total Cost: Rs.", best[0])
else:
    print("\nNo eligible plan found!")

