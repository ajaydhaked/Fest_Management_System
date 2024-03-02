from database.connect import conn
from psycopg2 import Error

# Query 1: Register a student in A4_Student table
def register_student(name, roll_number, username, password, only_student):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Student (name, roll_number, username, password, onlyStudent) VALUES ('{name}', '{roll_number}', '{username}', '{password}', {only_student});"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")


# Query 2: Register an Outsider in A4_Outsider
def register_outsider(name, username, password, college_id):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Outsider (name, username, password, college_id) VALUES ('{name}', '{username}', '{password}', {college_id});"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")
    
    
# Query 3: Register an Organizer in both A4_Student and A4_Organizer_to_Student tables
def register_organizer(name, roll_number, username, password, only_student, enrollment_key):

        
    try:
        cursor = conn.cursor()
        query0 = f"SELECT organizer_id FROM A4_Organizer_Role WHERE enrollment_key = '{enrollment_key}';"
        cursor.execute(query0)
        organizer_id = cursor.fetchone()[0]
        if organizer_id == None:
            return False
        query1 = f"INSERT INTO A4_Student (name, roll_number, username, password, onlyStudent) VALUES ('{name}', '{roll_number}', '{username}', '{password}', {only_student});"
        query2 = f"INSERT INTO A4_Organizer_to_Student (organizer_id, username) VALUES ({organizer_id}, '{username}');"
        cursor.execute(query1)
        conn.commit()
        cursor.execute(query2)
        conn.commit()
        cursor.close()
        return True
    except Error as e:
        print(f"Error executing query: {e}")
        
        
        

# Query 4: Register an outsider for an event in A4_Outsider_Participate_Event
async def register_outsider_for_event(event_id, username):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Outsider_Participate_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 5: Fetch event name, type, and description from A4_Event table
async def fetch_event_details():
    try:
        cursor = conn.cursor()
        query = "SELECT name, type, description FROM A4_Event;"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 6: Register a student for an event in A4_Student_Participate_Event
async def register_student_for_event(event_id, username):

    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Student_Participate_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 7: Allow student to volunteer in a given event in A4_Student_Volunteer_Event
async def allow_student_to_volunteer(event_id, username):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Student_Volunteer_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 8: Allow organizer to view all participants for a particular event
# A list of names and usernames are returned 
async def view_participants_for_event(desired_event_id):
    try:
        cursor = conn.cursor()
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


# Query 9: Allow organizer to view all volunteers for an event
async def view_volunteers_for_event(desired_event_id):

    try:
        cursor = conn.cursor()
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


# Query 10: Allow organizer to change name, type, and description of an event
async def change_event_details(desired_event_id, new_event_name, new_event_type, new_event_description):

    try:
        cursor = conn.cursor()
        query = f"""
        UPDATE A4_Event
        SET name = '{new_event_name}', type = '{new_event_type}', description = '{new_event_description}'
        WHERE event_id = {desired_event_id};
        """
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 11: Check if username exists in the A4_Student table
async def check_username_in_student_table(username):

    try:
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM A4_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 12: Check if username exists in the A4_Outsider table
async def check_username_in_outsider_table(username):

    try:
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM A4_Outsider WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

# Query 13: Check if username exists in the A4_Organizer_to_Student table
async def check_username_in_organizer_to_student_table(username):
    try:
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM A4_Organizer_to_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")
