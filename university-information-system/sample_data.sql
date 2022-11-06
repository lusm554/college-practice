CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    course INTEGER,
    faculty_id INTEGER,
    gender TEXT,
    birth_year TEXT,
    age INTEGER,
    cnt_of_children INTEGER,
    scholarship_amt INTEGER
);

INSERT INTO students
VALUES
    (NULL, 1, 1, 'm', '2000', '21', 0, 0);

CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    faculty_id INTEGER,
    category TEXT,
    gender TEXT,
    birth_year TEXT,
    age INTEGER,
    cnt_of_children INTEGER,
    salary_amt INTEGER,
    is_graduate_student INTEGER
);

INSERT INTO teachers
VALUES
    (NULL, 1, 'ассистент', 'm', '1986', 36, 1, 10000, 0);

CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT,
    course INTEGER,
    faculty_id INTEGER,
    department_id INTEGER
);

INSERT INTO groups
VALUES
    (NULL, '11IS-18', 1, 1, 1);

CREATE TABLE dissertations (
    dissertation_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    author_id INTEGER, -- problem, because teacher and student id maybe the same
    defense_date TEXT,
    title TEXT
);

INSERT INTO dissertations
VALUES
    (NULL, 1, '2000', 'some title');

CREATE TABLE Faculty (
    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);
 
INSERT INTO Faculty
VALUES
    (NULL);

CREATE TABLE Departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    faculty_id INTEGER
);

INSERT INTO Departments
VALUES
    (NULL, 1);

CREATE TABLE Disciplines (
    discipline_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT
);

INSERT INTO Disciplines
VALUES
    (NULL, "CS");
