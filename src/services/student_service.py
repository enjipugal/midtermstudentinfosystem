import json
import os
from datetime import datetime

from ..models.student import Student


class StudentService:
    def __init__(self, data_file='data/students.json'):
        self.data_file = data_file
        self._ensure_data_file()

    def _ensure_data_file(self):
        directory = os.path.dirname(self.data_file)

        if directory:
            os.makedirs(directory, exist_ok=True)

        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)

    def _load_students(self):
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_students(self, students):
        with open(self.data_file, 'w') as f:
            json.dump(students, f, indent=2)

    def add_student(self, student_data):
        students = self._load_students()

        student_id = str(
            student_data.get('student_id', '')
        ).strip()

        if not student_id.isdigit() or len(student_id) != 7:
            raise ValueError(
                "Student number must be exactly 7 digits."
            )

        if any(
            student['student_id'] == student_id
            for student in students
        ):
            raise ValueError(
                "Student number already exists."
            )

        student_data['student_id'] = student_id

        student = Student(**student_data)

        students.append(student.to_dict())
        self._save_students(students)

        return student.to_dict()

    def get_all_students(self):
        return self._load_students()

    def get_student(self, student_id):
        students = self._load_students()

        for student in students:
            if student['student_id'] == student_id:
                return student

        return None

    def search_students(self, search_term):
        students = self._load_students()

        search_term = str(search_term).lower().strip()

        results = []

        for student in students:
            if (
                search_term in student['student_id'].lower()
                or search_term in student['name'].lower()
                or search_term in student['email'].lower()
                or search_term in student['course'].lower()
            ):
                results.append(student)

        return results

    def update_student(self, student_id, update_data):
        students = self._load_students()

        for student in students:
            if student['student_id'] == student_id:
                student.update(update_data)
                student['updated_at'] = datetime.now().isoformat()

                self._save_students(students)

                return student

        return None

    def delete_student(self, student_id):
        students = self._load_students()

        original_count = len(students)

        students = [
            s for s in students
            if s['student_id'] != student_id
        ]

        self._save_students(students)

        return len(students) != original_count
 