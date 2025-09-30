# Store students in a dictionary: "Name": (GPA, Major)
students = {
    "Jon": (3.25, "Math"),
    "Kim": (2.25, "Biology"),
    "Lee": (2.30, "Math"),
    "Sara": (4.00, "Math"),
    "Miko": (1.90, "Math"),
    "Lin": (2.10, "Biology"),
    "Toby": (2.89, "Biology"),
    "Ben": (2.75, "Math"),
    "Mark": (2.34, "Math"),
    "Xia": (3.53, "Biology")
}

# 1. Compute average GPA
total_gpa = 0
count = 0

for gpa, major in students.values():
    total_gpa += gpa
    count += 1

average_gpa = total_gpa / count
print(f"Average GPA of all students: {average_gpa:.2f}\n")

# 2. Print students with above average GPA
print("Students with above average GPA:")
for name, (gpa, major) in students.items():
    if gpa > average_gpa:
        print(f"- {name} ({gpa}, {major})")
print()

# 3. Predict scholarships
print("Scholarship results:")
for name, (gpa, major) in students.items():
    if major == "Math" and gpa >= 3.5:
        print(f"{name} {gpa} {major} earned a scholarship.")
    elif major == "Biology" and gpa >= 2.75:
        print(f"{name} {gpa} {major} earned a scholarship.")
    else:
        print(f"{name} {gpa} {major} did not earn a scholarship.")