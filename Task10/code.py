
records = [
    "REG101|Harshitha|harshi@gmail.com",
    "REG102|Anu|anu123@gmail.com",
    "REG103|Ravi|ravi@gmail.com",
    "REG101|Kiran|kiran@gmail.com",
    "R1|Sai|sai@gmail.com",
    "REG104|Priya|priyaemail.com",
    "REG105|Teja",
    "REG106|A|teja@gmail.com"
]

valid_records = []
seen_ids = set()
duplicates = []
errors = []

for record in records:
    fields = record.split("|")
    issues = []

    if len(fields) != 3:
        issues.append("Missing or extra fields")
    else:
        reg_id, name, email = fields

        if len(reg_id) != 6 or not reg_id.startswith("REG"):
            issues.append("Invalid registration ID")

        if len(name) < 2 or len(name) > 20:
            issues.append("Invalid name length")

        if "@" not in email or "." not in email.split("@")[-1]:
            issues.append("Invalid email format")

        if reg_id in seen_ids:
            duplicates.append(reg_id)
            issues.append("Duplicate registration ID")
        else:
            seen_ids.add(reg_id)

    if issues:
        errors.append((record, issues))
    else:
        valid_records.append(fields)

print("VALID REGISTRATION RECORDS:")
for item in valid_records:
    print("ID:", item[0], "| Name:", item[1],
          "| Email:", item[2])

print("\nDUPLICATE IDs:")
for item in duplicates:
    print(item)

print("\nERROR CLASSIFICATION:")
for record, issues in errors:
    print(record, ":", ", ".join(issues))

print("\nTOTAL RECORDS:", len(records))
print("VALID RECORDS:", len(valid_records))
print("INVALID RECORDS:", len(errors))
print("DUPLICATES:", len(duplicates))

