# students_scholarship_test.py
# Beginner-friendly script to read the CSV, compute average GPA,
# list above-average students, and predict scholarships.

import csv

csv_path = "students_test.csv"  # expects this file in same folder

# 1) Read CSV into a dictionary
students = {}
with open(csv_path, newline="") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # skip header line
    for row in reader:
        name = row[0].strip()
        gpa = float(row[1])
        major = row[2].strip()
        students[name] = (gpa, major)

# 2) Compute average GPA
total_gpa = 0.0
count = 0
for gpa, major in students.values():
    total_gpa += gpa
    count += 1

average_gpa = total_gpa / count if count > 0 else 0.0
print(f"Average GPA of all students: {average_gpa:.2f}\n")

# 3) Print students with above average GPA
print("Students with above average GPA:")
for name, (gpa, major) in students.items():
    if gpa > average_gpa:
        print(f"- {name} ({gpa}, {major})")
print()

# 4) Predict scholarships (step-by-step)
# Rules inferred from prompt examples:
# Math -> scholarship if GPA >= 3.5
# Biology -> scholarship if GPA >= 2.75
# Other majors -> assume no scholarship rule provided

print("Scholarship evaluations (step-by-step):")
earned = []
not_earned = []
for name, (gpa, major) in students.items():
    print(f"Evaluating {name}: GPA={gpa}, Major={major}")
    major_l = major.lower()
    if major_l == "math":
        threshold = 3.5
        print(f" - Rule: Math students need GPA >= {threshold}")
        if gpa >= threshold:
            print(" -> Result: earned a scholarship.")
            earned.append((name, gpa, major))
        else:
            print(" -> Result: did not earn a scholarship.")
            not_earned.append((name, gpa, major))
    elif major_l == "biology":
        threshold = 2.75
        print(f" - Rule: Biology students need GPA >= {threshold}")
        if gpa >= threshold:
            print(" -> Result: earned a scholarship.")
            earned.append((name, gpa, major))
        else:
            print(" -> Result: did not earn a scholarship.")
            not_earned.append((name, gpa, major))
    else:
        print(" - Rule: No scholarship rule for this major; assume no scholarship.")
        print(" -> Result: did not earn a scholarship.")
        not_earned.append((name, gpa, major))
    print()

# 5) Summary
print("Summary of scholarship results:")
print("Earned a scholarship:")
for name, gpa, major in earned:
    print(f"- {name} ({gpa}, {major})")
print()
print("Did NOT earn a scholarship:")
for name, gpa, major in not_earned:
    print(f"- {name} ({gpa}, {major})")
