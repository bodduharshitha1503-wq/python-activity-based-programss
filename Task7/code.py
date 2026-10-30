

print("INTEGRATED MANUFACTURING PRODUCTION PLANNER")

materials = {
    "Steel": 500,
    "Plastic": 300,
    "Rubber": 200
}

required = {
    "Steel": 2,
    "Plastic": 1,
    "Rubber": 1
}

planned = int(input("Enter planned production quantity: "))
demand = int(input("Enter customer order demand: "))
defects = int(input("Enter defective products: "))

defect_limit = 5

if planned <= 0 or demand < 0 or defects < 0 or defects > planned:
    print("Invalid production or defect details!")

else:
    max_production = min(
        materials[m] // required[m]
        for m in materials
    )

    print("\n--- MATERIAL ANALYSIS ---")

    for material in materials:
        needed = planned * required[material]
        available = materials[material]

        print(material, "Available:", available)
        print("Required:", needed)

        if needed > available:
            print("Shortage:", needed - available)
        else:
            print("Status: Sufficient")

    print("\nMaximum Production:", max_production)

    if max_production >= planned:
        print("Material Status: Feasible")
    else:
        print("Material Status: Shortage")

    defect_percentage = (defects / planned) * 100

    print("\n--- QUALITY ANALYSIS ---")
    print("Defective Products:", defects)
    print("Defect Percentage:", round(defect_percentage, 2), "%")

    if defect_percentage > defect_limit:
        print("Quality Status: Violation")
    else:
        print("Quality Status: Accepted")

    good_products = min(max_production, planned) - defects

    print("\n--- ORDER ANALYSIS ---")
    print("Customer Demand:", demand)
    print("Good Products:", good_products)

    if good_products >= demand:
        print("Order Status: Demand Satisfied")
    else:
        print("Order Status: Production Shortage")
        print("Additional Units Needed:", demand - good_products)

    print("\n--- FINAL REPORT ---")

    if max_production >= planned and defect_percentage <= defect_limit and good_products >= demand:
        print("Production Status: SUCCESS")
    else:
        print("Production Status: NOT FEASIBLE")

print("\nProduction Analysis Completed.")

