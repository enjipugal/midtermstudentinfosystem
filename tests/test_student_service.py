import os
import tempfile
import unittest

from src.services.student_service import StudentService


class TestStudentService(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".json"
        )
        self.temp_file.close()

        self.service = StudentService(self.temp_file.name)

    def tearDown(self):
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_add_student(self):
        student_data = {
            "student_id": "2401478",
            "name": "Test Student",
            "email": "test@example.com",
            "course": "BSIT",
            "year_level": "3"
        }

        student = self.service.add_student(student_data)

        self.assertEqual(student["student_id"], "2401478")
        self.assertEqual(student["name"], "Test Student")

    def test_get_student(self):
        student_data = {
            "student_id": "2401478",
            "name": "Test Student",
            "email": "test@example.com",
            "course": "BSIT",
            "year_level": "3"
        }

        self.service.add_student(student_data)

        student = self.service.get_student("2401478")

        self.assertIsNotNone(student)
        self.assertEqual(student["student_id"], "2401478")

    def test_update_student(self):
        student_data = {
            "student_id": "2401478",
            "name": "Test Student",
            "email": "test@example.com",
            "course": "BSIT",
            "year_level": "3"
        }

        self.service.add_student(student_data)

        updated = self.service.update_student(
            "2401478",
            {"name": "Updated Student"}
        )

        self.assertIsNotNone(updated)
        self.assertEqual(updated["name"], "Updated Student")

    def test_delete_student(self):
        student_data = {
            "student_id": "2401478",
            "name": "Test Student",
            "email": "test@example.com",
            "course": "BSIT",
            "year_level": "3"
        }

        self.service.add_student(student_data)

        deleted = self.service.delete_student("2401478")

        self.assertTrue(deleted)
        self.assertIsNone(
            self.service.get_student("2401478")
        )


if __name__ == "__main__":
    unittest.main()
    