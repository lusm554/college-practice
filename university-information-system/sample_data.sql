CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    course,
    faculty_id,
    gender,
    birth_year,
    age,
    cnt_of_children,
    scholarship_amt
);

INSERT INTO students
VALUES
    (NULL, 1, 1, 'm', '2000', 21, 0, 0);

CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    faculty_id,
    category,
    gender,
    birth_year,
    age,
    cnt_of_children,
    salary_amt,
    is_graduate_student
);

INSERT INTO teachers
VALUES
    (NULL, 1, 'ассистент', 'm', '1990', 31, 0, 30000, 0);


CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name,
    course,
    faculty_id,
    department_id
);

INSERT INTO groups
VALUES
    (NULL, '11IS-18', 1, 1, 1);


CREATE TABLE dissertations (
    dissertation_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    author_id,
    defense_date,
    title
);

INSERT INTO dissertations
VALUES
    (NULL, 1, '2022', 'some title');


CREATE TABLE faculty (
    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);

INSERT INTO faculty
VALUES
    (NULL);


CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    faculty_id
);

INSERT INTO departments
VALUES
    (NULL, 1);


CREATE TABLE disciplines (
    discipline_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name
);

INSERT INTO disciplines
VALUES
    (NULL, 'some name');


CREATE TABLE disciplines_schedule (
    disciplines_schedule_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    discipline_id,
    semester_n,
    group_id,
    teacher_id,
    type,
    duration_time
);

INSERT INTO disciplines_schedule
VALUES
    (NULL, 1, 1, 18, 3, 'exam', '2h');


CREATE TABLE session (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    disciplines_schedule_id,
    discipline_id,
    grade
);

INSERT INTO session
VALUES
    (NULL, 1, 1, 5);


CREATE TABLE Graduate_works (
    gr_work_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id,
    leader_gw_id
);

INSERT INTO Graduate_works
VALUES
    (NULL, 1, 1);
