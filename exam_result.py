print("📚 Exam Result Management System")

students = []

while True:
    print("\n1. Add Student Result")
    print("2. View Results")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Calculate Grade")
    print("6. Delete Result")
    print("7. Count Students")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add Student Result
    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")

        math = float(input("Enter Mathematics marks: "))
        science = float(input("Enter Science marks: "))
        english = float(input("Enter English marks: "))

        student = {
            "id": student_id,
            "name": name,
            "math": math,
            "science": science,
            "english": english
        }

        students.append(student)

        print("✅ Student result added successfully!")

    # View Results
    elif choice == "2":
        if len(students) == 0:
            print("❌ No student results found.")
        else:
            print("\n📋 Student Results")
            print("--------------------------")

            for student in students:
                total = student["math"] + student["science"] + student["english"]
                percentage = total / 3

                print("Student ID:", student["id"])
                print("Student Name:", student["name"])
                print("Mathematics:", student["math"])
                print("Science:", student["science"])
                print("English:", student["english"])
                print("Total:", total)
                print("Percentage:", percentage)

                if percentage >= 90:
                    grade = "A+"
                elif percentage >= 80:
                    grade = "A"
                elif percentage >= 70:
                    grade = "B"
                elif percentage >= 60:
                    grade = "C"
                elif percentage >= 50:
                    grade = "D"
                else:
                    grade = "F"

                print("Grade:", grade)
                print("--------------------------")

    # Search Student
    elif choice == "3":
        search_id = input("Enter student ID to search: ")

        found = False

        for student in students:
            if student["id"] == search_id:
                total = student["math"] + student["science"] + student["english"]
                percentage = total / 3

                print("\n✅ Student Found")
                print("Student ID:", student["id"])
                print("Student Name:", student["name"])
                print("Mathematics:", student["math"])
                print("Science:", student["science"])
                print("English:", student["english"])
                print("Total:", total)
                print("Percentage:", percentage)

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # Update Marks
    elif choice == "4":
        update_id = input("Enter student ID: ")

        found = False

        for student in students:
            if student["id"] == update_id:

                student["math"] = float(input("Enter new Mathematics marks: "))
                student["science"] = float(input("Enter new Science marks: "))
                student["english"] = float(input("Enter new English marks: "))

                print("✅ Marks updated successfully!")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # Calculate Grade
    elif choice == "5":
        grade_id = input("Enter student ID: ")

        found = False

        for student in students:
            if student["id"] == grade_id:

                total = student["math"] + student["science"] + student["english"]
                percentage = total / 3

                if percentage >= 90:
                    grade = "A+"
                elif percentage >= 80:
                    grade = "A"
                elif percentage >= 70:
                    grade = "B"
                elif percentage >= 60:
                    grade = "C"
                elif percentage >= 50:
                    grade = "D"
                else:
                    grade = "F"

                print("\n📊 Result")
                print("Total Marks:", total)
                print("Percentage:", percentage)
                print("Grade:", grade)

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # Delete Result
    elif choice == "6":
        delete_id = input("Enter student ID to delete: ")

        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)

                print("✅ Student result deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # Count Students
    elif choice == "7":
        print("👨‍🎓 Total Students:", len(students))

    # Exit
    elif choice == "8":
        print("Thank you for using Exam Result Management System! 📚")
        break

    else:
        print("❌ Invalid choice!")
