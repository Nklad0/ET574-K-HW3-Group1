# list of three students named Jon, Kim and Lee
students = ["Nico", "Aiden", "Vinicius"]

# function to print ‘Hi name’ for each student in the list
def greet_students(student_list):
	for name in student_list:
		print(f"Hi {name}")

# call the function
greet_students(students)
