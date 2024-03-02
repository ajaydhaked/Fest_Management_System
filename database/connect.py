import psycopg2

conn=psycopg2.connect(
        database="techfest",user="postgres",password="Ajay@123",host="localhost",port="5432"
    )

if conn:
    print("connected to database")
else:
    print("not connected to database")
    