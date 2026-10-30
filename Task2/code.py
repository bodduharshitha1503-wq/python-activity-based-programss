

from datetime import datetime, timedelta
import math

print("SMART PARKING FEE MANAGEMENT")

vehicle = input("Enter vehicle number: ")
category = input("Enter vehicle category (Bike/Car/Bus): ").lower()

rates = {
    "bike": 10,
    "car": 20,
    "bus": 40
}

if category not in rates:
    print("Invalid vehicle category!")
else:
    try:
        entry = input("Enter entry time (HH:MM): ")
        exit_time = input("Enter exit time (HH:MM): ")

        start = datetime.strptime(entry, "%H:%M")
        end = datetime.strptime(exit_time, "%H:%M")

        if end < start:
            end += timedelta(days=1)

        duration = (end - start).total_seconds() / 3600

        if duration == 0:
            hours = 0
        else:
            hours = math.ceil(duration)

        days = math.ceil(hours / 24)

        rate = rates[category]
        daily_limit = 200

        charge = hours * rate

        if days > 0:
            charge = min(charge, days * daily_limit)

        overnight = 0
        if end.date() > start.date() or (
            end.hour < start.hour and end.day > start.day
        ):
            overnight = 50

        penalty = 0
        if duration > 72:
            penalty = 100

        total = charge + overnight + penalty

        print("\n----- PARKING BILL -----")
        print("Vehicle Number:", vehicle)
        print("Category:", category.upper())
        print("Parking Hours:", hours)
        print("Hourly Rate: Rs.", rate)
        print("Parking Charge: Rs.", charge)
        print("Overnight Charge: Rs.", overnight)
        print("Penalty: Rs.", penalty)
        print("Total Fee: Rs.", total)

    except ValueError:
        print("Invalid time! Enter time in HH:MM format.")

print("\nThank you for using our parking system!")

