def display_menu():
    print("\n==== Student Record Management System ====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as f:
        f.write(f"{name},{roll},{marks}\n")

    print("✅ Student added successfully!")

def view_students():
    print("\n--- All Student Records ---")
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()
            if not data:
                print("No student records found.")
                return
            for line in data:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, roll, marks = parts
                    print(f"Name: {name}, Roll No: {roll}, Marks: {marks}")
                else:
                    print("⚠️ Skipping invalid line in file:", line.strip())
    except FileNotFoundError:
        print("⚠️ No data file found yet. Try adding a student first.")

def search_student():
    roll_no = input("Enter roll number to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, roll, marks = line.strip().split(",")
                if roll == roll_no:
                    print(f"\n🎯 Found: Name: {name}, Roll No: {roll}, Marks: {marks}")
                    found = True
                    break
        if not found:
            print("❌ Student not found.")
    except FileNotFoundError:
        print("⚠️ No data file found.")

def update_student():
    roll_no = input("Enter roll number to update: ")
    updated_data = []
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, roll, marks = line.strip().split(",")
                if roll == roll_no:
                    print(f"Found: Name: {name}, Roll No: {roll}, Marks: {marks}")
                    new_name = input("Enter new name: ")
                    new_marks = input("Enter new marks: ")
                    updated_data.append(f"{new_name},{roll},{new_marks}\n")
                    found = True
                else:
                    updated_data.append(line)
        if found:
            with open("students.txt", "w") as f:
                f.writelines(updated_data)
            print("✅ Student record updated.")
        else:
            print("❌ Student not found.")
    except FileNotFoundError:
        print("⚠️ No data file found.")

def delete_student():
    roll_no = input("Enter roll number to delete: ")
    new_data = []
    deleted = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, roll, marks = line.strip().split(",")
                if roll != roll_no:
                    new_data.append(line)
                else:
                    deleted = True
        if deleted:
            with open("students.txt", "w") as f:
                f.writelines(new_data)
            print("✅ Student record deleted.")
        else:
            print("❌ Student not found.")
    except FileNotFoundError:
        print("⚠️ No data file found.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter 1–6.")

# Run the program
main()
