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