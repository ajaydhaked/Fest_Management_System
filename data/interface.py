# NAME SWADHIN SATYAPRAKASH MAJHI
# ROLL-NO 21CS10067
# DBMS ASSIGNMENT 3
import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def query_output(rows, query_number : int):
    print("\n********************************************************************************************\n")
    if(query_number == 1):
        print("\033[1mQUERY {query_number} OUTPUT\033[0m\n")
        print("\033[1mRoll of Student\t\tName of Student\033[0m")
        for row in rows:
            print(str(row[0])+"\t\t\t"+str(row[1]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 2):
        print("\033[1mQUERY 2 OUTPUT\033[0m\n")
        print("\033[1mRoll of Student\t\tName of Student\033[0m")
        for row in rows:
            print(str(row[0])+"\t\t\t"+str(row[1]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 3):
        print("\033[1mQUERY 3 OUTPUT\033[0m\n")
        print("\033[1mName of Participant\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 4):
        print("\033[1mQUERY 4 OUTPUT\033[0m\n")
        print("\033[1mName of College\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 5):
        print("\033[1mQUERY 5 OUTPUT\033[0m\n")
        print("\033[1mName of Event\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 6):
        print("\033[1mQUERY 6 OUTPUT\033[0m\n")
        print("\033[1mName of Student\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 7):
        print("\033[1mQUERY 7 OUTPUT\033[0m\n")
        print("\033[1mName of Event\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 8):
        print("\033[1mQUERY 8 OUTPUT\033[0m\n")
        print("\033[1mName of college\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 9):
        print("\033[1mQUERY 9 OUTPUT\033[0m\n")
        print("\033[1mName of college\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    elif(query_number == 10):
        print("\033[1mQUERY 10 OUTPUT\033[0m\n")
        print("\033[1mName of Department\033[0m")
        for row in rows:
            print(str(row[0]))
        print(f"( Total {len(rows)} rows )")
    else:
        print("\033[1mQUERY 11 OUTPUT\033[0m\n")
        print("\033[1mRoll of Student\t\tName of Student\033[0m")
        for row in rows:
            print(str(row[0])+"\t\t\t"+str(row[1]))
        print(f"( Total {len(rows)} rows )")
    print("\n********************************************************************************************\n")

def query_process(query_number : int, event_t = None):
    query_list = [
        '''
        SELECT S.ROLL,
        S.NAME
        FROM STUDENT S
        JOIN EVENT E ON S.EID = E.EID
        WHERE E.ENAME = 'Megaevent';
        ''',
        '''
        SELECT S.ROLL,S.NAME
        FROM STUDENT S JOIN ROLE R ON S.RID = R.RID
        JOIN EVENT E ON S.EID = E.EID
        WHERE R.RNAME = 'Secretary'
        AND E.ENAME = 'Megaevent';
        ''',
        '''
        SELECT P.PNAME
        FROM PARTICIPANT P
        JOIN COLLEGE C ON P.CID = C.CID
        JOIN EVENT E ON P.EID = E.EID
        WHERE C.NAME = 'IITB'
        AND E.ENAME = 'Megaevent';
        ''',
        '''
        SELECT DISTINCT C.NAME
        FROM COLLEGE C
        JOIN PARTICIPANT P ON C.CID = P.CID
        JOIN EVENT E ON P.EID = E.EID
        WHERE E.ENAME = 'Megaevent';
        ''',
        '''
        SELECT DISTINCT E.ENAME
        FROM EVENT E
        JOIN STUDENT S ON E.EID = S.EID
        JOIN ROLE R ON S.RID = R.RID
        WHERE R.RNAME = 'Secretary';
        ''',
        '''
        SELECT S.NAME
        FROM STUDENT S
        JOIN VOLUNTEER V ON S.ROLL = V.ROLL
        JOIN EVENT E ON V.EID = E.EID
        WHERE S.DEPT = 'CSE'
        AND E.ENAME = 'Megaevent';
        ''',
        '''
        SELECT DISTINCT E.ENAME
        FROM EVENT E
        JOIN VOLUNTEER V ON E.EID = V.EID
        JOIN STUDENT S ON V.ROLL = S.ROLL
        WHERE S.DEPT = 'CSE';
        ''',
        '''
        SELECT C.NAME
        FROM COLLEGE C
        JOIN PARTICIPANT P ON C.CID = P.CID
        JOIN EVENT E ON P.EID = E.EID
        WHERE E.ENAME = 'Megaevent'
        GROUP BY C.NAME
        ORDER BY COUNT(*) DESC
        LIMIT 1;
        ''',
        '''
        SELECT C.NAME
        FROM COLLEGE C
        JOIN PARTICIPANT P ON C.CID = P.CID
        GROUP BY C.NAME
        ORDER BY COUNT(*) DESC
        LIMIT 1;
        ''',
        '''
        SELECT S.DEPT
        FROM STUDENT S
        JOIN VOLUNTEER V ON S.ROLL = V.ROLL
        JOIN EVENT E ON V.EID = E.EID
        JOIN PARTICIPANT P ON E.EID = P.EID
        JOIN COLLEGE C ON P.CID = C.CID
        WHERE C.NAME = 'IITB'
        GROUP BY S.DEPT
        ORDER BY COUNT(DISTINCT V.ROLL) DESC
        LIMIT 1;
        ''',
        f'''
        SELECT S.ROLL,
        S.NAME
        FROM STUDENT S
        JOIN EVENT E ON S.EID = E.EID
        WHERE E.ENAME = '{event_t}';
        '''
    ]
    print("The query is: ")
    print(query_list[query_number-1])
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query_list[query_number-1])
                rows = cur.fetchall()
                query_output(rows, query_number)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':

    while True:
        # Menu
        print("The following queries are suppported in the database: ")
        print("1. Roll number and name of all the students who are managing the \"Megaevent\"")
        print("2. Roll number and name of all the students who are managing \"Megevent\" as an \"Secretary\"")
        print("3. Name of all the participants from the college \"IITB\" in \"Megaevent\"")
        print("4. Name of all the colleges who have at least one participant in \"Megaevent\"")
        print("5. Name of all the events which is managed by a \"Secretary\"")
        print("6. Name of all the \"CSE\" department student volunteers of \"Megaevent\"")
        print("7. Name of all the events which has at least one volunteer from \"CSE\"")
        print("8. Name of the college with the largest number of participants in \"Megaevent\"")
        print("9. Name of the college with largest number of participant over all")
        print("10. Name of the department with the largest number of volunteers in all the events which has at least one participant from \"IITB\"")
        print("11. Roll number and name of all the students who are managing a certain event")
        print("12. Quit the program")
        print("********************************************************************************************")

        try:
            option = int(input("Choose one query: "))
            print("********************************************************************************************")
            if(option < 1 or option > 12):
                print("The query number chosen in not valid. Please retry")
                print("********************************************************************************************")
                continue
            if(option == 12):
                break
            if(option == 11):
                event_type = input("Enter the type of the event: ")
                query_process(option, event_type)
            else:
                query_process(option)
            print("********************************************************************************************")
        except ValueError:
            print("Not a valid input")
            print("********************************************************************************************")
            continue
