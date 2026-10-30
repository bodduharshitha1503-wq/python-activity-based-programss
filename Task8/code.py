

records = [
    ("B101", "Ravi", 10, 0, True),
    ("B102", "Sita", 18, 4, True),
    ("B103", "Kumar", 20, 6, False),
    ("B104", "Priya", 7, 0, True),
    ("B105", "Arun", 15, 2, True)
]

allowed_days = 14
fine_per_day = 5

total_fine = 0
overdue_books = []
available_books = []
borrowed_books = []

print("LIBRARY BORROWING REPORT")

for book in records:

    book_id, name, days, delay, returned = book

    overdue = max(0, days - allowed_days)
    fine = overdue * fine_per_day

    total_fine += fine

    print("\nBook ID:", book_id)
    print("Borrower:", name)
    print("Borrowing Days:", days)
    print("Overdue Days:", overdue)
    print("Fine: Rs.", fine)

    if overdue > 0:
        overdue_books.append(book_id)
        print("Status: Overdue")
    else:
        print("Status: Normal")

    if returned:
        available_books.append(book_id)
    else:
        borrowed_books.append(book_id)

print("\n--- OVERDUE BOOKS ---")
print(overdue_books)

print("\n--- BOOK AVAILABILITY ---")
print("Available Books:", available_books)
print("Borrowed Books:", borrowed_books)

print("\n--- FINAL RECONCILIATION ---")
print("Total Books:", len(records))
print("Available Count:", len(available_books))
print("Borrowed Count:", len(borrowed_books))
print("Total Fine: Rs.", total_fine)

print("\nLibrary Analysis Completed.")

