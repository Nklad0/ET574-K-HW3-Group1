
students = ["Nico", "Aiden", "Vinicius"]
gpas = [3.8, 3.5, 3.9]

# Compute the average GPA and print it
average_gpa = sum(gpas) / len(gpas)
print("Average GPA:", average_gpa)

# Print all above-average students
print("Above average students:")
for i in range(len(students)):
	if gpas[i] > average_gpa:
		print(students[i], gpas[i])

# Predict which students will earn a scholarship (GPA >= 3.5)
print("Scholarship students:")
for i in range(len(students)):
	if gpas[i] >= 3.5:
		print(students[i], "earned a scholarship.")

Input: Nico 3.8
Output: Nico earned a scholarship.

Input: Aiden 3.5
Output: Aiden earned a scholarship.

Input: Vinicius 3.9
Output: Vinicius earned a scholarship.
