import psycopg2

conn=psycopg2.connect(
        database="techfest",user="postgres",password="Ajay@123",host="localhost",port="5432"
    )
# conn=psycopg2.connect(
#         database="21CS30002",user="21CS30002",password="21CS30002",host="10.5.18.70"
#     )
if conn:
    print("connected to database")
else:
    print("not connected to database")
    