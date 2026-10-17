
students = []

def add_student(students, name, marks):
    students.append([name, marks])

# ← YAHAN HAI show_students
def show_students(students):
    if len(students) == 0:          # NAYA: agar list khaali ho
        print("No students found")  # NAYA
        return                      # NAYA: function yahin khatam
    for s in students:
        print(f"Name: {s[0]}, Marks: {s[1]}")

def find_topper(students):
    if len(students) == 0:
        print("No students found")
        return
    top = students[0]
    for s in students:
        if s[1] > top[1]:
            top = s
    print(f"Topper: {top[0]} with {top[1]} marks")

def save_students(students):
    f = open("students.txt", "w")
    for s in students:
        f.write(f"{s[0]},{s[1]}\n")
    f.close()

def load_students(students):
    open("students.txt", "a").close()   # file na ho to bana do
    f = open("students.txt", "r")
    text = f.read()
    f.close()
    lines = text.split("\n")
    for line in lines:
        if line != "":
            parts = line.split(",")
            add_student(students, parts[0], int(parts[1]))

load_students(students)

while True:
    print("\n--- Student Record Manager ---")
    print("1. Add student")
    print("2. Show all students")
    print("3. Show topper")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        marks = int(input("Marks: "))
        add_student(students, name, marks)
        save_students(students)
        print("Student added")
    elif choice == "2":
        show_students(students)
    elif choice == "3":
        find_topper(students)
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid option")