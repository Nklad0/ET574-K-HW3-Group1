
# Store students and their GPAs into two lists
students = ["Nico", "Aiden", "Vinicius"]
gpas = [3.8, 3.5, 3.9]

# Compute the average GPA and print it
average_gpa = sum(gpas) / len(gpas)
print("Average GPA:", average_gpa)

# Print all above average students
print("Above average students:")
for i in range(len(students)):
	if gpas[i] > average_gpa:
		print(students[i], gpas[i])

# Predict which students will earn a scholarship (GPA >= 3.5)
print("Scholarship students:")
for i in range(len(students)):
	if gpas[i] >= 3.5:
		print(students[i], "earned a scholarship.")


