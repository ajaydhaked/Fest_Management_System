import psycopg2

conn=psycopg2.connect(
        database="ajaydb",user="ajaydb_owner",password="TyuU5Ozofs2Q",host="ep-solitary-field-a15p5upo.ap-southeast-1.aws.neon.tech",port="5432"
    )
# conn=psycopg2.connect(
#         database="21CS10033",user="21CS10033",password="21CS10033",host="10.5.18.68"
#     )
if conn:
    print("connected to database")
else:
    print("not connected to database")
    