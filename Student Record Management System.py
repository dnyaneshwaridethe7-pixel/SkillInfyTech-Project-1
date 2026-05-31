# Student Record Management System
students = []
# Add Student
def add_student():
name = input("Enter student name: ")
age = input("Enter age: ")
marks = input("Enter marks: ")
subject = input("Enter subject: ")
student = {
"Name": name,
"Age": age,
"Marks": marks,
"Subject": subject
}
students.append(student)
print("Student added successfully!\n")
# View Students
def view_students():
if len(students) == 0:
print("No student records found.\n")
else:
print("\nStudent Records:")
for i, student in enumerate(students, start=1):
print(f"\nStudent {i}")
for key, value in student.items():
print(f"{key}: {value}")
# Edit Student
def edit_student():
view_students()
if len(students) == 0:
return
index = int(input("\nEnter student number to edit: ")) - 1
if 0 <= index < len(students):
students[index]["Name"] = input("Enter new name: ")
students[index]["Age"] = input("Enter new age: ")
students[index]["Marks"] = input("Enter new marks: ")
students[index]["Subject"] = input("Enter new subject: ")
print("Student record updated!\n")
else:
print("Invalid student number.\n")
# Delete Student
def delete_student():
view_students()
if len(students) == 0:
return
index = int(input("\nEnter student number to delete: ")) - 1
if 0 <= index < len(students):
students.pop(index)
print("Student deleted successfully!\n")
else:
print("Invalid student number.\n")
# Main Menu
while True:
print("===== Student Record Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Edit Student")
print("4. Delete Student")
print("5. Exit")
choice = input("Enter your choice: ")
if choice == "1":
add_student()
elif choice == "2":
view_students()
elif choice == "3":
edit_student()
elif choice == "4":
delete_student()
elif choice == "5":
print("Program exited.")
break
else:
print("Invalid choice! Try again.\n")
