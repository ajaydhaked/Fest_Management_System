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

-- for inserting data into the table events
a4_event(name,date,type,description) VALUES('Megaevent',date '2020-12-12','Cultural','Megaevent is a cultural event with highteck facilities');

INSERT INTO A4_College (college_id, college_name) VALUES
(1, 'Indian Institute of Technology (IIT) Bombay'),
(2, 'Indian Institute of Technology (IIT) Delhi'),
(3, 'Indian Institute of Technology (IIT) Kanpur'),
(4, 'Indian Institute of Technology (IIT) Madras'),
(5, 'Indian Institute of Technology (IIT) Kharagpur'),
(6, 'Indian Institute of Technology (IIT) Roorkee'),
(7, 'Indian Institute of Technology (IIT) Guwahati'),
(8, 'Indian Institute of Technology (IIT) Hyderabad'),
(9, 'Indian Institute of Technology (IIT) Ropar'),
(10, 'Indian Institute of Technology (IIT) Gandhinagar');


INSERT INTO A4_Organizer_Role (organizer_id, enrollment_key, role, description) VALUES \
(1, 123, 'Admin', 'Administrator role'),
(2, 456, 'Editor', 'Editor role'),
(3, 789, 'Viewer', 'Viewer role'),
(4, 321, 'Moderator', 'Moderator role'),
(5, 654, 'Author', 'Author role'),
(6, 987, 'Contributor', 'Contributor role'),
(7, 659, 'Subscriber', 'Subscriber role'),
(8, 322, 'Guest', 'Guest role');