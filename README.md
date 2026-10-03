# Student Information System

A Python-based Student Information System developed as a midterm project to demonstrate CRUD operations, JSON data persistence, modular architecture, configuration management, error handling, logging, unit testing, and GitHub version control.

## Features

- Add student records
- View all student records
- View a student by Student ID
- Update student information
- Delete student records
- Search students by Student ID, name, email, or course
- Store student data using JSON
- 7-digit Student ID validation
- Duplicate Student ID prevention
- Error handling
- Application logging
- Unit testing
- Modular project structure
- Git branching and version control

## Project Structure

```text
midtermstudentinfosystem/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logger.py
│   ├── __init__.py
│   └── main.py
├── data/
│   └── students.json
├── config/
│   └── config.json
├── logs/
│   └── app.log
├── tests/
│   └── test_student_service.py
├── README.md
├── requirements.txt
└── .gitignore
