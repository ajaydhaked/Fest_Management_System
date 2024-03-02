import psycopg2

conn=psycopg2.connect(
        database="techfest",user="postgres",password="Ajay@123",host="localhost",port="5432"
    )
# conn=psycopg2.connect(
#         database="21CS10033",user="21CS10033",password="21CS10033",host="10.5.18.68"
#     )
if conn:
    print("connected to database")
else:
    print("not connected to database")
    