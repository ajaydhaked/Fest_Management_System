import psycopg2
from psycopg2 import Error



# Note that response fetched from the database is a list of tuples
# Function to establish database connection
def connect_to_database():
    try:
        connection = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}")

# Query 1: Check if username exists in the A4_Student table
def check_username_in_student_table(connection, username):
    try:
        cursor = connection.cursor()
        query = f"SELECT COUNT(*) FROM A4_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 2: Check if username exists in the A4_Outsider table
def check_username_in_outsider_table(connection, username):
    try:
        cursor = connection.cursor()
        query = f"SELECT COUNT(*) FROM A4_Outsider WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 3: Check if username exists in the A4_Organizer_to_Student table
def check_username_in_organizer_to_student_table(connection, username):
    try:
        cursor = connection.cursor()
        query = f"SELECT COUNT(*) FROM A4_Organizer_to_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 4: Register an Outsider in A4_Outsider
def register_outsider(connection, name, username, password, college_id):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO A4_Outsider (name, username, password, college_id) VALUES ('{name}', '{username}', '{password}', {college_id});"
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 5: Register a student in A4_Student table
def register_student(connection, name, roll_number, username, password, only_student):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO A4_Student (name, roll_number, username, password, onlyStudent) VALUES ('{name}', '{roll_number}', '{username}', '{password}', {only_student});"
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 6: Register an Organizer in both A4_Student and A4_Organizer_to_Student tables
def register_organizer(connection, name, roll_number, username, password, only_student, organizer_id):
    try:
        cursor = connection.cursor()
        query1 = f"INSERT INTO A4_Student (name, roll_number, username, password, onlyStudent) VALUES ('{name}', '{roll_number}', '{username}', '{password}', {only_student});"
        query2 = f"INSERT INTO A4_Organizer_to_Student (organizer_id, username) VALUES ({organizer_id}, '{username}');"
        cursor.execute(query1)
        cursor.execute(query2)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 7: Fetch event name, type, and description from A4_Event table
def fetch_event_details(connection):
    try:
        cursor = connection.cursor()
        query = "SELECT name, type, description FROM A4_Event;"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 8: Register an outsider for an event in A4_Outsider_Participate_Event
def register_outsider_for_event(connection, event_id, username):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO A4_Outsider_Participate_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 9: Register a student for an event in A4_Student_Participate_Event
def register_student_for_event(connection, event_id, username):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO A4_Student_Participate_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 10: Allow student to volunteer in a given event in A4_Student_Volunteer_Event
def allow_student_to_volunteer(connection, event_id, username):
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO A4_Student_Volunteer_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 11: Allow organizer to view all participants for a particular event
# A list of names and usernames are returned 
def view_participants_for_event(connection, desired_event_id):
    try:
        cursor = connection.cursor()
        query_student = f"""
        SELECT name, username
        FROM A4_Student_Participate_Event spe
        JOIN A4_Student s ON spe.username = s.username
        WHERE spe.event_id = {desired_event_id};
        """
        cursor.execute(query_student)
        student_participants = cursor.fetchall()

        query_outsider = f"""
        SELECT name, username
        FROM A4_Outsider_Participate_Event ope
        JOIN A4_Outsider o ON ope.username = o.username
        WHERE ope.event_id = {desired_event_id};
        """
        cursor.execute(query_outsider)
        outsider_participants = cursor.fetchall()

        cursor.close()
        return student_participants, outsider_participants
    except Error as e:
        print(f"Error executing query: {e}")

# Query 12: Allow organizer to view all volunteers for an event
def view_volunteers_for_event(connection, desired_event_id):
    try:
        cursor = connection.cursor()
        query = f"""
        SELECT s.name, s.username
        FROM A4_Student_Volunteer_Event sve
        JOIN A4_Student s ON sve.username = s.username
        WHERE sve.event_id = {desired_event_id};
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 13: Allow organizer to change name, type, and description of an event
def change_event_details(connection, desired_event_id, new_event_name, new_event_type, new_event_description):
    try:
        cursor = connection.cursor()
        query = f"""
        UPDATE A4_Event
        SET name = '{new_event_name}', type = '{new_event_type}', description = '{new_event_description}'
        WHERE event_id = {desired_event_id};
        """
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Establish a connection to the database
connection = connect_to_database()

# Example usage:
result1 = check_username_in_student_table(connection, 'desired_username')
result2 = check_username_in_outsider_table(connection, 'desired_username')
result3 = check_username_in_organizer_to_student_table(connection, 'desired_username')
register_outsider(connection, 'outsider_name', 'outsider_username', 'outsider_password', college_id)
register_student(connection, 'student_name', 'student_roll_number', 'student_username', 'student_password', True)
register_organizer(connection, 'organizer_name', 'organizer_roll_number', 'organizer_username', 'organizer_password', False, organizer_id_value)
result7 = fetch_event_details(connection)
register_outsider_for_event(connection, event_id_value, 'outsider_username')
register_student_for_event(connection, event_id_value, 'student_username')
allow_student_to_volunteer(connection, event_id_value, 'student_username')
result11 = view_participants_for_event(connection, desired_event_id)
result12 = view_volunteers_for_event(connection, desired_event_id)
change_event_details(connection, desired_event_id, 'new_event_name', 'new_event_type', 'new_event_description')

# Close the connection when done
connection.close()
