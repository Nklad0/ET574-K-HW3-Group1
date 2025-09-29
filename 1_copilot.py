students = ['Nico', 'Aiden', 'Vinicius']

# Add the new students
students.append('Sara')
students.append('Miko')

def greet_students(students):
    for student in students:
        print(f'Hi {student}')
    print("Total students:", len(students))

greet_students(students)