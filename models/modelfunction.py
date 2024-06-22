from database.connect import conn
from psycopg2 import Error
from models.allmodels import *

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
def register_outsider(name, username, password, collegename):
    try:
        cursor = conn.cursor()
        # get college_id from collegename
        query = f"SELECT college_id FROM A4_College WHERE college_name = '{collegename}';"
        cursor.execute(query)
        college_id = cursor.fetchone()[0]
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
def register_outsider_for_event(event_id, username):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Outsider_Participate_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 5: Fetch event name, type, and description from A4_Event table
def fetch_event_details():
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
def register_student_for_event(event_id, username):

    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Student_Participate_Event (event_id, username) VALUES ({event_id}, '{username}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")

# Query 7: Allow student to volunteer in a given event in A4_Student_Volunteer_Event
def allow_student_to_volunteer(event_id, username):
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
def view_participants_for_event(desired_event_id):
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
def view_volunteers_for_event(desired_event_id):

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
def change_event_details(desired_event_id, new_event_name, new_event_type, new_event_description):

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
def check_username_in_student_table(username):

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
def check_username_in_outsider_table(username):

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
def check_username_in_organizer_to_student_table(username):
    try:
        cursor = conn.cursor()
        query = f"SELECT COUNT(*) FROM A4_Organizer_to_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")

def checkfororganiser(user=Organiser_l):
    # check for user.username
    # return 1 for username already exists
    # return 2 for roll number already exists
    # return 3 for enrollment key does not exist
    # return 0 for success
    try:
        cursor = conn.cursor()
        queryusername = f"SELECT username FROM A4_Student WHERE username = '{user.username}';"
        cursor.execute(queryusername)
        result = cursor.fetchall()
        if len(result) > 0:
            return 1
        queryrollno = f"SELECT roll_number FROM A4_Student WHERE roll_number = '{user.roll_no}';"
        cursor.execute(queryrollno)
        result = cursor.fetchall()
        if len(result) > 0:
            return 2
        # find the enrollment key
        queryenroll = f"SELECT enrollment_key FROM A4_Organizer_Role WHERE enrollment_key = '{user.enrollment_key}';"
        cursor.execute(queryenroll)
        result = cursor.fetchall()
        if len(result) == 0:
            return 3
        cursor.close()
        return 0
    except Error as e:
        print(f"Error executing query: {e}")
        
def checkforstudent(user=Student_l):
    # check for user.username
    # return 1 for username already exists
    # return 2 for roll number already exists
    # return 0 for success
    try:
        cursor = conn.cursor()
        queryusername = f"SELECT username FROM A4_Student WHERE username = '{user.username}';"
        cursor.execute(queryusername)
        result = cursor.fetchall()
        print(result)
        if len(result) > 0:
            return 1
        queryrollno = f"SELECT roll_number FROM A4_Student WHERE roll_number = '{user.roll_no}';"
        cursor.execute(queryrollno)
        result = cursor.fetchall()
        if len(result) > 0:
            return 2
        cursor.close()
        return 0
    except Error as e:
        print(f"Error executing query: {e}")
        
def checkforoutsider(user=Outsider_l):
    # check for user.username
    # return 1 for username already exists
    # return 0 for success
    try:
        cursor = conn.cursor()
        queryusername = f"SELECT username FROM A4_Outsider WHERE username = '{user.username}';"
        cursor.execute(queryusername)
        result = cursor.fetchall()
        if len(result) > 0:
            return 1
        cursor.close()
        return 0
    except Error as e:
        print(f"Error executing query: {e}")
        
def checkforuser(user=User_l):
    # check for user.username and user.password
    # return 1 for invalid username or password
    # return 0 for success
    try:
        cursor = conn.cursor()
        query = f"SELECT username FROM A4_Student WHERE username = '{user.username}' AND password = '{user.password}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Student")
            cursor.close()
            return 0
        query = f"SELECT username FROM A4_Outsider WHERE username = '{user.username}' AND password = '{user.password}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Outsider")
            cursor.close()
            return 0
        query = f"SELECT username FROM A4_Organizer_to_Student WHERE username = '{user.username}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            print("Organiser")
            cursor.close()
            return 0
        cursor.close()
        return 1
    except Error as e:
        print(f"Error executing query: {e}")
        
def getfrontenduser(token):
    if token is None:
        return frontenduser(is_logged_in=0, username=None, is_organiser=0, is_student=0, is_outsider=0, participate_events=[], volunteer_events=[])
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM A4_Organizer_to_Student WHERE username = '{token}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            cursor.close()
            return frontenduser(is_logged_in=1, username=token, is_organiser=1, is_student=0, is_outsider=0, participate_events=[], volunteer_events=[])
        query = f"SELECT * FROM A4_Student WHERE username = '{token}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            participated_events = []
            volunteer_events = []
            query = f"SELECT event_id FROM A4_Student_Participate_Event WHERE username = '{token}';"
            cursor.execute(query)
            result = cursor.fetchall()
            for i in range(len(result)):
                participated_events.append(result[i][0])
            query = f"SELECT event_id FROM A4_Student_Volunteer_Event WHERE username = '{token}';"
            cursor.execute(query)
            result = cursor.fetchall()
            for i in range(len(result)):
                volunteer_events.append(result[i][0])
            cursor.close()
            return frontenduser(is_logged_in=1, username=token, is_organiser=0, is_student=1, is_outsider=0, participate_events=participated_events, volunteer_events=volunteer_events)
        
        query = f"SELECT * FROM A4_Outsider WHERE username = '{token}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if len(result) > 0:
            participated_events = []
            query = f"SELECT event_id FROM A4_Outsider_Participate_Event WHERE username = '{token}';"
            cursor.execute(query)
            result = cursor.fetchall()
            for i in range(len(result)):
                participated_events.append(result[i][0])
            cursor.close()
            return frontenduser(is_logged_in=1, username=token, is_organiser=0, is_student=0, is_outsider=1, participate_events=participated_events, volunteer_events=[])
        cursor.close()
        return frontenduser(is_logged_in=0, username=None, is_organiser=0, is_student=0, is_outsider=0, participate_events=[], volunteer_events=[])
    except Error as e:
        print(f"Error executing query: {e}")
        return frontenduser(is_logged_in=0, username=None, is_organiser=0, is_student=0, is_outsider=0, participate_events=[], volunteer_events=[])
    
    
def getalleventstable():
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM A4_Event;"
        cursor.execute(query)
        result = cursor.fetchall()
        events = []
        for i in range(len(result)):
            temp = geteventwinners(result[i][0])
            windecl=0
            if len(temp)>0:
                windecl=1
            events.append(Event(event_id=result[i][0], name=result[i][1], date=result[i][2].strftime("%d-%m-%Y"), type=result[i][3], description=result[i][4],winner_declared=windecl, winners=temp))
        cursor.close()
        return events
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    
def getallcollegenames():
    try:
        cursor = conn.cursor()
        query = "SELECT college_name FROM A4_College;"
        cursor.execute(query)
        result = cursor.fetchall()
        colleges = []
        for i in range(len(result)):
            colleges.append(result[i][0])
        cursor.close()
        return colleges
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    
def getalleventparticipants(event_id):
    try:
        cursor = conn.cursor()
        query = f"SELECT username FROM A4_Student_Participate_Event WHERE event_id = {event_id};"
        cursor.execute(query)
        result = cursor.fetchall()
        students = []
        for i in range(len(result)):
            students.append(result[i][0])
        query = f"SELECT username FROM A4_Outsider_Participate_Event WHERE event_id = {event_id};"
        cursor.execute(query)
        result = cursor.fetchall()
        outsiders = []
        for i in range(len(result)):
            outsiders.append(result[i][0])
        # volunteers also
        query = f"SELECT username FROM A4_Student_Volunteer_Event WHERE event_id = {event_id};"
        cursor.execute(query)
        result = cursor.fetchall()
        volunteers = []
        for i in range(len(result)):
            volunteers.append(result[i][0])
        cursor.close()
        return students, outsiders, volunteers 
    except Error as e:
        print(f"Error executing query: {e}")
        return [], []
    
def geteventdetails(event_id):
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM A4_Event WHERE event_id = {event_id};"
        cursor.execute(query)
        result = cursor.fetchall()
        eventwinr=geteventwinners(event_id)
        windecl=0
        if len(eventwinr)>0:
            windecl=1
        event = Event(event_id=result[0][0], name=result[0][1], date=result[0][2].strftime("%d-%m-%Y"), type=result[0][3], description=result[0][4], winner_declared=windecl, winners=eventwinr)
        cursor.close()
        return event
    except Error as e:
        print(f"Error executing query: {e}")
        return Event()
    
def geteventwinners(event_id):
    try:
        cursor = conn.cursor()
        query = f"SELECT username, rank FROM A4_winners_student WHERE event_id = {event_id};"
        cursor.execute(query)
        result = cursor.fetchall()
        students = []
        for i in range(len(result)):
            students.append([result[i][0], result[i][1]])
        query = f"SELECT username, rank FROM A4_winners_outsider WHERE event_id = {event_id};"
        cursor.execute(query)
        result = cursor.fetchall()
        for i in range(len(result)):
            students.append([result[i][0],result[i][1]])
        cursor.close()
        # sort according to rank
        if len(students) == 0:
            return students
        students.sort(key = lambda x: x[1])
        for i in range(len(students)):
            students[i][1] = i+1
        return students
    except Error as e:
        print(f"Error executing query: {e}")
        return [], []
    
def allocate_outsider_to_hall(username):
    try:
        cursor = conn.cursor()
        # count of users in outsider table
        query = "SELECT COUNT(*) FROM A4_Outsider;"
        cursor.execute(query)
        count = cursor.fetchone()
        count = int(count[0])
        hall_id = count/3 + 1
        hall_id = int(hall_id)
        # get hall name
        query = f"SELECT hall_name FROM A4_Halls WHERE hall_id = {hall_id};"
        cursor.execute(query)
        hall_name = cursor.fetchone()[0]
        # allocate hall to user
        query = f"INSERT INTO A4_outsider_accomodation (username,accomodation_place,MerchTaken) VALUES ('{username}','{hall_name}',0);"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")
        
def gethallname(username):
    try:
        cursor = conn.cursor()
        query = f"SELECT accomodation_place FROM A4_outsider_accomodation WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()
        if(result != None):
            return result[0]
        cursor.close()
        return result
    except Error as e:
        print(f"Error executing query: {e}")
        return None
    
def getstudentdetails(username):
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM A4_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()
        temp = profile(name=result[0], username=result[2], rollno=result[1], collegename="IIT Kharagpur", merchtaken=0, rolename="", roledesc="")
        cursor.close()
        return temp
    except Error as e:
        print(f"Error executing query: {e}")
        return profile()
    
def getorganiserdetails(username):
    try:
        cursor = conn.cursor()
        query = f"SELECT name,username,roll_number FROM A4_Student WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()
        temp = profile(name=result[0], username=result[1], rollno=result[2], collegename="IIT Kharagpur", merchtaken=0, rolename="", roledesc="")
        query = f"SELECT organizer_id FROM A4_Organizer_to_Student WHERE username = '{username}';"
        cursor.execute(query)
        organiser_id = cursor.fetchone()[0]
        query = f"SELECT role,description FROM A4_Organizer_Role WHERE organizer_id = {organiser_id};"
        cursor.execute(query)
        result = cursor.fetchone()
        temp.rolename = result[0]
        temp.roledesc = result[1]
        cursor.close()
        return temp
    except Error as e:
        print(f"Error executing query: {e}")
        return profile()
    
def getoutsiderdetails(username):
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM A4_Outsider WHERE username = '{username}';"
        cursor.execute(query)
        result = cursor.fetchone()
        temp = profile(name=result[0], username=result[1], rollno="", collegename="", merchtaken=0, rolename="", roledesc="")
        college_id = result[3]
        query = f"SELECT college_name FROM A4_College WHERE college_id = {college_id};"
        cursor.execute(query)
        temp.collegename = cursor.fetchone()[0]
        cursor.close()
        return temp
    except Error as e:
        print(f"Error executing query: {e}")
        return profile()
    
def getallstudents():
    try:
        cursor = conn.cursor()
        query = "SELECT username FROM A4_Student WHERE onlyStudent = True;"
        cursor.execute(query)
        result = cursor.fetchall()
        students = []
        for i in range(len(result)):
            students.append(result[i][0])
        cursor.close()
        return students
    except Error as e:
        print(f"Error executing query: {e}")
        return []

def getallorganisers():
    try:
        cursor = conn.cursor()
        query = "SELECT username FROM A4_Organizer_to_Student;"
        cursor.execute(query)
        result = cursor.fetchall()
        organisers = []
        for i in range(len(result)):
            organisers.append(result[i][0])
        cursor.close()
        return organisers
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    
def getalloutsiders():
    try:
        cursor = conn.cursor()
        query = "SELECT username FROM A4_Outsider;"
        cursor.execute(query)
        result = cursor.fetchall()
        outsiders = []
        for i in range(len(result)):
            outsiders.append(result[i][0])
        cursor.close()
        return outsiders
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    
    
    
def delete_a_student(username):
    try:
        cursor = conn.cursor()
        query = f"DELETE FROM A4_winners_student WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_Student_Participate_Event WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_Student_Volunteer_Event WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_Student WHERE username = '{username}';"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")


def delete_a_organiser(username):
    try:
        cursor = conn.cursor()
        # WE NEED TO DELETE THE STUDENT INSTANCE FROM ALL TABLES
        query = f"DELETE FROM A4_Organizer_to_Student WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_Student WHERE username = '{username}';"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")


def delete_a_outsider(username):
    try:
        cursor = conn.cursor()
        query = f"DELETE FROM A4_winners_outsider WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_outsider_accomodation WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_Outsider_Participate_Event WHERE username = '{username}';"
        cursor.execute(query)
        query = f"DELETE FROM A4_Outsider WHERE username = '{username}';"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")
        
        
def getallenrollments():
    try:
        cursor = conn.cursor()
        query = "SELECT enrollment_key, role FROM A4_Organizer_Role;"
        cursor.execute(query)
        result = cursor.fetchall()
        enrollments = []
        for i in range(len(result)):
            enrollments.append([result[i][0], result[i][1]])
        cursor.close()
        return enrollments
    except Error as e:
        print(f"Error executing query: {e}")
        return []
    
def declarewinnersforanevent(event_id, winners):
    try:
        cursor = conn.cursor()
        er=-1
        for i in range(len(winners)):
            query = f"SELECT COUNT(*) FROM a4_student_participate_event WHERE username='{winners[i]}';"
            cursor.execute(query)
            result = int(cursor.fetchone()[0])
            if result > 0:
                continue
            # check if outsider
            query = f"SELECT COUNT(*) FROM a4_outsider_participate_event WHERE username='{winners[i]}';"
            cursor.execute(query)
            result = int(cursor.fetchone()[0])
            if result > 0:
                continue
            er=i
            break    

        if er!=-1:
            conn.commit()
            cursor.close()
            return er
        for i in range(len(winners)):
            # check if student
            query = f"SELECT COUNT(*) FROM a4_student_participate_event WHERE username='{winners[i]}';"
            cursor.execute(query)
            result = int(cursor.fetchone()[0])
            if result > 0:
                query = f"INSERT INTO a4_winners_student (event_id, username, rank) VALUES ({event_id}, '{winners[i]}', {i+1});"
                cursor.execute(query)
                continue
            # check if outsider
            query = f"SELECT COUNT(*) FROM a4_outsider_participate_event WHERE username='{winners[i]}';"
            cursor.execute(query)
            result = int(cursor.fetchone()[0])
            if result > 0:
                query = f"INSERT INTO A4_winners_outsider (event_id, username, rank) VALUES ({event_id}, '{winners[i]}', {i+1});"
                cursor.execute(query)
                continue
        conn.commit()
        cursor.close()
        return -1
    except Error as e:
        print(f"Error executing query: {e}")
        
        
def createevent(name, date, type, description):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO A4_Event (name, date, type, description) VALUES ('{name}', '{date}', '{type}', '{description}');"
        cursor.execute(query)
        conn.commit()
        cursor.close()
    except Error as e:
        print(f"Error executing query: {e}")