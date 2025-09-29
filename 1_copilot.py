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

    def greet_students(student_list):
	    for name in student_list:
		    print(f"Hi {name}")

	greet_students(students)


>>>>>>> 3261b8e (Added Task A)
