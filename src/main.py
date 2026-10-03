import logging

from src.services.student_service import StudentService


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)


class StudentInformationSystem:

    def __init__(self):
        self.student_service = StudentService()
        self.logger = logging.getLogger(__name__)

    def display_menu(self):
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Search Student")
        print("7. Exit")

    def add_student(self):
        print("\n--- Add New Student ---")

        student_id = input("Student ID: ")
        name = input("Name: ")
        email = input("Email: ")
        course = input("Course: ")
        year_level = input("Year Level: ")

        student_data = {
            "student_id": student_id,
            "name": name,
            "email": email,
            "course": course,
            "year_level": year_level
        }

        try:
            student = self.student_service.add_student(
                student_data
            )

            self.logger.info(
                f"Added student: {student['student_id']}"
            )

            print(
                f"Student added successfully! "
                f"ID: {student['student_id']}"
            )

        except Exception as e:
            self.logger.error(
                f"Error adding student: {e}"
            )
            print(f"Error adding student: {e}")

    def view_all_students(self):
        print("\n--- All Students ---")

        students = self.student_service.get_all_students()

        if not students:
            print("No students found.")
            return

        for student in students:
            print(
                f"ID: {student['student_id']}, "
                f"Name: {student['name']}, "
                f"Email: {student['email']}, "
                f"Course: {student['course']}, "
                f"Year Level: {student['year_level']}"
            )

    def view_student(self):
        print("\n--- View Student ---")

        student_id = input("Enter Student ID: ")

        student = self.student_service.get_student(
            student_id
        )

        if student:
            print("\nStudent Details:")
            print(f"ID: {student['student_id']}")
            print(f"Name: {student['name']}")
            print(f"Email: {student['email']}")
            print(f"Course: {student['course']}")
            print(f"Year Level: {student['year_level']}")
            print(f"GPA: {student['gpa']}")
            print(f"Created At: {student['created_at']}")
            print(f"Updated At: {student['updated_at']}")
        else:
            print("Student not found.")

    def update_student(self):
        print("\n--- Update Student ---")

        student_id = input("Enter Student ID: ")

        student = self.student_service.get_student(
            student_id
        )

        if not student:
            print("Student not found.")
            return

        print(
            "\nLeave a field blank to keep "
            "the current value."
        )

        name = input(
            f"Name [{student['name']}]: "
        )

        email = input(
            f"Email [{student['email']}]: "
        )

        course = input(
            f"Course [{student['course']}]: "
        )

        year_level = input(
            f"Year Level [{student['year_level']}]: "
        )

        update_data = {}

        if name:
            update_data["name"] = name

        if email:
            update_data["email"] = email

        if course:
            update_data["course"] = course

        if year_level:
            update_data["year_level"] = year_level

        if not update_data:
            print("No changes made.")
            return

        try:
            updated_student = (
                self.student_service.update_student(
                    student_id,
                    update_data
                )
            )

            if updated_student:
                self.logger.info(
                    f"Updated student: {student_id}"
                )

                print(
                    "Student updated successfully."
                )
            else:
                print("Student not found.")

        except Exception as e:
            self.logger.error(
                f"Error updating student: {e}"
            )
            print(
                f"Error updating student: {e}"
            )

    def delete_student(self):
        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID: ")

        student = self.student_service.get_student(
            student_id
        )

        if not student:
            print("Student not found.")
            return

        print(f"Student: {student['name']}")

        confirmation = input(
            "Are you sure you want to delete "
            "this student? (y/n): "
        )

        if confirmation.lower() != "y":
            print("Delete cancelled.")
            return

        try:
            deleted = (
                self.student_service.delete_student(
                    student_id
                )
            )

            if deleted:
                self.logger.info(
                    f"Deleted student: {student_id}"
                )

                print(
                    "Student deleted successfully."
                )
            else:
                print("Student not found.")

        except Exception as e:
            self.logger.error(
                f"Error deleting student: {e}"
            )
            print(
                f"Error deleting student: {e}"
            )

    def search_student(self):
        print("\n--- Search Student ---")

        search_term = input(
            "Enter Student ID, Name, Email, "
            "or Course: "
        )

        students = (
            self.student_service.search_students(
                search_term
            )
        )

        if not students:
            print("No students found.")
            return

        print("\n--- Search Results ---")

        for student in students:
            print(
                f"ID: {student['student_id']}, "
                f"Name: {student['name']}, "
                f"Email: {student['email']}, "
                f"Course: {student['course']}, "
                f"Year Level: {student['year_level']}"
            )

    def run(self):
        while True:
            self.display_menu()

            choice = input(
                "Enter your choice (1-7): "
            )

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_all_students()

            elif choice == "3":
                self.view_student()

            elif choice == "4":
                self.update_student()

            elif choice == "5":
                self.delete_student()

            elif choice == "6":
                self.search_student()

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print(
                    "Invalid choice. Please try again."
                )


if __name__ == "__main__":
    app = StudentInformationSystem()
    app.run()
    