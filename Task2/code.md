

## 1. Problem Statement

Develop a Python program to calculate parking fees based on vehicle entry time, exit time, vehicle category, overnight parking, daily limits, and penalty conditions.

The program should:

- Accept vehicle details and entry and exit times.
- Validate the entered time format.
- Support different vehicle categories such as Bike, Car, and Bus.
- Calculate parking duration in hours.
- Apply different hourly charges based on vehicle category.
- Calculate overnight parking charges.
- Apply maximum daily parking limits.
- Add penalty charges for invalid parking conditions.
- Display the total parking fee and a detailed bill.

## 2. Algorithm

1. Start the program.
2. Enter vehicle number and vehicle category.
3. Enter vehicle entry time and exit time.
4. Validate the time format.
5. Check whether the exit time is earlier than the entry time. If so, consider overnight parking.
6. Calculate the total parking duration.
7. Calculate the parking charges based on vehicle category.
8. Calculate overnight charges if applicable.
9. Apply the maximum daily parking limit.
10. Check penalty conditions.
11. Calculate the final parking fee.
12. Display the parking bill.
13. Stop the program.

## 3. Flowchart 
```mermaid flowchart

flowchart TD
    A([Start]) --> B[/Enter vehicle details/]
    B --> C[/Enter entry and exit times/]
    C --> D{Valid time format?}
    D -->|No| E[Display invalid time]
    E --> C
    D -->|Yes| F{Exit before entry?}
    F -->|Yes| G[Calculate overnight duration]
    F -->|No| H[Calculate normal duration]
    G --> I[Calculate parking hours]
    H --> I
    I --> J[Select vehicle category]
    J --> K[Calculate hourly charges]
    K --> L[Apply daily maximum limit]
    L --> M{Penalty condition?}
    M -->|Yes| N[Add penalty charges]
    M -->|No| O[No penalty]
    N --> P[Calculate final fee]
    O --> P
    P --> Q[Display parking bill]
    Q --> R([Stop])


## 4. Sample Input

```
SMART PARKING FEE MANAGEMENT

Enter vehicle number: AP39AB1234
Enter vehicle category (Bike/Car/Bus): car
Enter entry time (HH:MM): 09:00
Enter exit time (HH:MM): 14:30
```

## 5. Sample Output

```
----- PARKING BILL -----
Vehicle Number: AP39AB1234
Category: CAR
Parking Hours: 6
Hourly Rate: Rs. 20
Parking Charge: Rs. 120
Overnight Charge: Rs. 0
Penalty: Rs. 0
Total Fee: Rs. 120

Thank you for using our parking system!
```

