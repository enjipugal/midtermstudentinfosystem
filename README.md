# Student Information System

A Python-based Student Information System developed as a midterm project to demonstrate CRUD operations, JSON data persistence, modular architecture, error handling, logging, and GitHub version control.

## Features

- Add student records
- View all student records
- View a student by Student ID
- Update student information
- Delete student records
- Store student data using JSON
- 7-digit Student ID validation
- Duplicate Student ID prevention
- Error handling
- Application logging
- Unit testing
- Modular project structure

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
