# Fest Management System

## Introduction

Fest Management System is a web application developed for managing university festivals, providing a centralized platform for event planning, participant management, and financial oversight.

## Currently hosted on

The application is currently hosted at https://fest-management-system.onrender.com/

## Deployment

To run this project on your local machine, follow these steps:

**Clone the repository:**
   ```bash
   git clone git@github.com:ajaydhaked/Fest_Management_System.git
   ```
**Enter Directory:**
   ```
   cd Fest_Management_System
   ```
## Deployment

To Run this project on your local machine


First open virtual env
```bash
  .\dbmsenv\Scripts\activate
```

Deploy your fastapi project
```bash
  uvicorn main:app --reload
```


## Technologies Used

* FastAPI
* PostgreSQL
* Jinja2 
* HTML CSS Javascript
* Tailwind CSS
## Features
**Fest Management System**
Fest Management System is designed to streamline the orchestration of university festivals. Key features include:

* Event Planning: Efficient scheduling and venue allocation through a user-friendly interface
* Participant Management: Online registration and engagement tools for students and outsiders
* Volunteer Coordination: Recruitment, role assignment, and tracking for volunteers

## Database Design
The project utilizes a relational database with the following main schemas:
* Student Table: Manages student data including names, roll numbers, usernames, passwords, and role flags
* College Table: Stores information about colleges participating in the festivals
* Outsider Table: Records information about non-student participants linked to specific colleges
* Event Table: Stores event details such as event ID, name, date, type, and description
* Organizer_Role Table: Manages roles of organizers with enrollment keys and descriptions
* Various Relationship Tables: Facilitate connections between students, organizers, outsiders, and events.
