-- Create A4_Student table
CREATE TABLE A4_Student (
    name VARCHAR(255),
    roll_number CHAR(9) UNIQUE,
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    onlyStudent BOOLEAN
);

-- Create A4_College table
CREATE TABLE A4_College (
    college_id INT PRIMARY KEY,
    college_name VARCHAR(255)
);

-- Create A4_Outsider table
CREATE TABLE A4_Outsider (
    name VARCHAR(255),
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    college_id INT,
    FOREIGN KEY (college_id) REFERENCES A4_College(college_id)
);

--Create A4_outsider_accomodation table
CREATE TABLE A4_outsider_accomodation (
    username VARCHAR(255),
    accomodation_place VARCHAR(255),
    MerchTaken INT,
    FOREIGN KEY (username) REFERENCES A4_Outsider(username)
);

-- Create A4_Halls table
CREATE TABLE A4_Halls (
    hall_id INT PRIMARY KEY,
    hall_name VARCHAR(255)
);

-- Create A4_Event table
CREATE TABLE A4_Event (
    event_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date DATE,
    type VARCHAR(255),
    description VARCHAR(255)
);

-- Create A4_Organizer_Role table
CREATE TABLE A4_Organizer_Role (
    organizer_id INT PRIMARY KEY,
    enrollment_key INT UNIQUE,
    role VARCHAR(255) UNIQUE,
    description VARCHAR(255)
);

-- Create A4_Organizer_to_Student table
CREATE TABLE A4_Organizer_to_Student (
    organizer_id INT,
    username VARCHAR(255),
    FOREIGN KEY (organizer_id) REFERENCES A4_Organizer_Role(organizer_id),
    FOREIGN KEY (username) REFERENCES A4_Student(username)
);

-- Create A4_winners_student table
CREATE TABLE A4_winners_student (
    event_id INT,
    username VARCHAR(255),
    rank INT,
    FOREIGN KEY (event_id) REFERENCES A4_Event(event_id),
    FOREIGN KEY (username) REFERENCES A4_Student(username)
);

-- Create A4_winners_outsider table
CREATE TABLE A4_winners_outsider (
    event_id INT,
    username VARCHAR(255),
    rank INT,
    FOREIGN KEY (event_id) REFERENCES A4_Event(event_id),
    FOREIGN KEY (username) REFERENCES A4_Outsider(username)
);
-- Create A4_Student_Participate_Event table
CREATE TABLE A4_Student_Participate_Event (
    event_id INT,
    username VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES A4_Event(event_id),
    FOREIGN KEY (username) REFERENCES A4_Student(username)
);

-- Create A4_Outsider_Participate_Event table
CREATE TABLE A4_Outsider_Participate_Event (
    event_id INT,
    username VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES A4_Event(event_id),
    FOREIGN KEY (username) REFERENCES A4_Outsider(username)
);

-- Create A4_Student_Volunteer_Event table
CREATE TABLE A4_Student_Volunteer_Event (
    event_id INT,
    username VARCHAR(255),
    FOREIGN KEY (event_id) REFERENCES A4_Event(event_id),
    FOREIGN KEY (username) REFERENCES A4_Student(username)
);

-- insert into A4_Student
INSERT INTO A4_Student (name, roll_number, username, password, onlyStudent) VALUES
('Ajay', '123456789', 'ajay123', 'ajay123', TRUE),
('Vijay', '987654321', 'vijay123', 'vijay123', TRUE)
;

-- insert into A4_Outsider
INSERT INTO A4_Outsider (name, username, password, college_id) VALUES
('Outsider', 'outsider', 'outsider', 1)
;

-- for inserting data into the table events
INSERT INTO a4_event(name,date,type,description) VALUES
('Megaevent',date '2020-12-12','Cultural','Megaevent is a cultural event with highteck facilities'),
('Dance War',date '2020-12-12','Cultural','Dance is a cultural event with highteck facilities'),
('Code Hackathon',date '2020-12-12','Technical','Hackathon is a technical event with highteck facilities'),
('Music Beats',date '2020-12-12','Cultural','Music is a cultural event with highteck facilities'),
('Robotics',date '2020-12-12','Technical','Robotics is a technical event with highteck facilities'),
('Drama Competition',date '2020-12-12','Cultural','Drama is a cultural event with highteck facilities'),
('Coding Challenge',date '2020-12-12','Technical','Coding is a technical event with highteck facilities'),
('Painting Competition',date '2020-12-12','Cultural','Painting is a cultural event with highteck facilities'),
('Web Development',date '2020-12-12','Technical','Web Development is a technical event with highteck facilities');
;

INSERT INTO A4_College (college_id, college_name) VALUES
(1, 'Indian Institute of Technology (IIT) Bombay'),
(2, 'Indian Institute of Technology (IIT) Delhi'),
(3, 'Indian Institute of Technology (IIT) Kanpur'),
(4, 'Indian Institute of Technology (IIT) Madras'),
(5, 'Indian Institute of Technology (IIT) Roorkee'),
(6, 'Indian Institute of Technology (IIT) Guwahati'),
(7, 'Indian Institute of Technology (IIT) Hyderabad'),
(8, 'Indian Institute of Technology (IIT) Ropar'),
(9, 'Indian Institute of Technology (IIT) Gandhinagar');


INSERT INTO A4_Organizer_Role (organizer_id, enrollment_key, role, description) VALUES
(1, 123, 'Admin', 'Administrator role'),
(2, 456, 'Editor', 'Editor role'),
(3, 789, 'Viewer', 'Viewer role'),
(4, 321, 'Moderator', 'Moderator role'),
(5, 654, 'Author', 'Author role'),
(6, 987, 'Contributor', 'Contributor role'),
(7, 659, 'Subscriber', 'Subscriber role'),
(8, 322, 'Guest', 'Guest role');


INSERT INTO A4_Student_Participate_Event (event_id, username) VALUES
(1, 'ajay123'),
(2, 'ajay123'),
(3, 'ajay123'),
(6, 'ajay123'),
(7, 'ajay123');

INSERT INTO A4_Student_Volunteer_Event (event_id, username) VALUES
(4, 'ajay123'),
(5, 'ajay123');

-- insert into A4_Halls
INSERT INTO A4_Halls (hall_id, hall_name) VALUES
(1, 'Hall 1'),
(2, 'Hall 2'),
(3, 'Hall 3'),
(4, 'Hall 4'),
(5, 'Hall 5'),
(6, 'Hall 6'),
(7, 'Hall 7'),
(8, 'Hall 8'),
(9, 'Hall 9'),
(10, 'Hall 10');

-- insert into A4_outsider_accomodation
INSERT INTO A4_outsider_accomodation (username, accomodation_place, MerchTaken) VALUES
('outsider', 'Hall 1', 0);


-- insert into A4_winners_student
INSERT INTO A4_winners_student (event_id, username, rank) VALUES
(1, 'ajay123', 1);

-- insert into A4_winners_outsider
INSERT INTO A4_winners_outsider (event_id, username, rank) VALUES
(1, 'outsider', 2);