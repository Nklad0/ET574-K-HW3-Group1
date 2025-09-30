<<<<<<< HEAD
<<<<<<< HEAD
students = ['Nico', 'Aiden', 'Vinicius']

# change Nic to Nico
# students[0] is already 'Nico', so no change needed

# Add the new students
students.append('Sara')
students.append('Miko')

def greet_students(students):
    for student in students:
        print(f'Hi {student}')
    print("Total students:", len(students))

greet_students(students)
=======
# list of three students named Nico, Aiden and Vinicius
students = ["Nico", "Aiden", "Vinicius"]
gpas = [3.8, 3.5, 3.9]  
# Example GPAs for each student

# Print all above average students
average_gpa = sum(gpas) / len(gpas)
print("Above average students:")
for i, gpa in enumerate(gpas):
    if gpa > average_gpa:
        print(f"{students[i]}: {gpa}")

# Predict scholarship students (GPA >= 3.5)
print("Scholarship students:")
for i, gpa in enumerate(gpas):
    if gpa >= 3.5:
        print(f"{students[i]}: {gpa}")

    def greet_students(student_list):
	    for name in student_list:
		    print(f"Hi {name}")

	greet_students(students)
=======
>>>>>>> 633a16f (Task E Complete)


>>>>>>> 3261b8e (Added Task A)

