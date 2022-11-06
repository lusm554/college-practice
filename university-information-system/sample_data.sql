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


INSERT INTO students VALUES
    (null, 1, 2, 'm', '2000', 21, 0, 0),
    (null, 1, 2, 'm', '2000', 21, 0, 0)