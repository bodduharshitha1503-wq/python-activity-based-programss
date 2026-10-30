

courses = [
    ("Python", 40),
    ("Mathematics", 60),
    ("English", 30),
    ("Web Development", 50),
    ("Physics", 80)
]

rooms = [
    ("Room A", 40),
    ("Room B", 60),
    ("Room C", 100)
]

periods = ("9AM", "10AM", "11AM")

timetable = []
unallocated = []

print("SMART CLASSROOM TIMETABLE")

for course, students in courses:
    allocated = False

    for period in periods:
        for room, capacity in rooms:

            clash = False

            for item in timetable:
                if item[1] == room and item[2] == period:
                    clash = True
                    break

            if capacity >= students and not clash:
                timetable.append(
                    (course, room, period, students)
                )
                allocated = True
                break

        if allocated:
            break

    if not allocated:
        unallocated.append(course)

print("\n--- FINAL TIMETABLE ---")

for item in timetable:
    print("Course:", item[0])
    print("Room:", item[1])
    print("Period:", item[2])
    print("Students:", item[3])
    print("-------------------")

print("\n--- ALLOCATION REPORT ---")

print("Allocated Courses:", len(timetable))
print("Unallocated Courses:", len(unallocated))

if unallocated:
    print("Courses not allocated:", unallocated)
else:
    print("All courses allocated successfully!")

print("\nTimetable Allocation Completed.")

