students = []

def add_student(students, name, marks):
    students.append([name, marks])

def show_students(students):
    for s in students:
        print(f"Name: {s[0]}, Marks: {s[1]}")

add_student(students, "Ali", 80)
add_student(students, "Sara", 90)

show_students (students)