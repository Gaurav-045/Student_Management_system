students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for roll_no, student in students.items():
        print(f"\nRoll Number: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        student = students[roll_no]

        print("\nStudent Found!")
        print(f"Roll Number: {roll_no}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
    else:
        print("Student not found!")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    if roll_no not in students:
        print("Student not found!")
        return

    print("Enter new details:")

    students[roll_no]["name"] = input("Enter Name: ")
    students[roll_no]["age"] = input("Enter Age: ")
    students[roll_no]["course"] = input("Enter Course: ")
    students[roll_no]["marks"] = float(input("Enter Marks: "))

    print("Student details updated successfully!")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
