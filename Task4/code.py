

print("COURIER CHARGE OPTIMIZATION")

weight = float(input("Enter parcel weight (kg): "))
length = float(input("Enter length (cm): "))
width = float(input("Enter width (cm): "))
height = float(input("Enter height (cm): "))

zone = input("Enter distance zone (Local/National/International): ").lower()
urgency = input("Enter urgency (Normal/Express): ").lower()
fragile = input("Is parcel fragile? (yes/no): ").lower()
restricted = input("Is item prohibited? (yes/no): ").lower()
budget = float(input("Enter your budget: "))

if (weight <= 0 or length <= 0 or width <= 0
        or height <= 0 or budget < 0):
    print("Invalid parcel details or budget!")

elif zone not in ["local", "national", "international"]:
    print("Invalid distance zone!")

elif urgency not in ["normal", "express"]:
    print("Invalid urgency!")

elif fragile not in ["yes", "no"] or restricted not in ["yes", "no"]:
    print("Invalid restriction input!")

elif restricted == "yes":
    print("Delivery not allowed for prohibited items!")

else:
    volumetric = (length * width * height) / 5000
    charge_weight = max(weight, volumetric)

    zones = {
        "local": 40,
        "national": 80,
        "international": 150
    }

    services = {
        "Standard": {"limit": 20, "extra": 0},
        "Premium": {"limit": 30, "extra": 50},
        "Express": {"limit": 25, "extra": 100}
    }

    print("\n--- COURIER SERVICE COMPARISON ---")

    eligible = []

    for name, service in services.items():

        if charge_weight <= service["limit"]:
            base = charge_weight * zones[zone]
            urgent_charge = 100 if urgency == "express" else 0
            fragile_charge = 30 if fragile == "yes" else 0

            total = (base + service["extra"]
                     + urgent_charge + fragile_charge)

            print("\nService:", name)
            print("Chargeable Weight:", charge_weight, "kg")
            print("Base Charge: Rs.", round(base, 2))
            print("Service Charge: Rs.", service["extra"])
            print("Urgency Charge: Rs.", urgent_charge)
            print("Fragile Charge: Rs.", fragile_charge)
            print("Total Charge: Rs.", round(total, 2))

            if total <= budget:
                eligible.append((total, name))

    if eligible:
        best = min(eligible)

        print("\n--- BEST COURIER SERVICE ---")
        print("Service Name:", best[1])
        print("Final Charge: Rs.", round(best[0], 2))
    else:
        print("\nNo eligible courier service found!")

print("\nOptimization Completed.")

