from header import *


user_database = {
    "swadhin": {
        "username": "swadhin",
        "password": "swadhin"
    }
}


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "page": "home"})


@app.get("/events")
async def read_root(request: Request,message: str = None):
    if(request.cookies.get("token") is None):
        return RedirectResponse(url="/login?message=please login to see events page",status_code=status.HTTP_302_FOUND)
    cur = conn.cursor()
    cur.execute("SELECT * FROM A4_event")
    events = cur.fetchall()
    cur.close()
    for i in range(len(events)):
        events[i] = Event(event_id=events[i][0],name=events[i][1],date=events[i][2].strftime("%d-%m-%Y"),type=events[i][3],description=events[i][4])
    return templates.TemplateResponse("/events/events.html", {"request": request, "events": events,"message":message,"page":"events"})

@app.get("/about")
async def read_root(request: Request,message: str = None):
    return templates.TemplateResponse("about.html", {"request": request,"message":message, "page": "about"})

@app.get("/signup")
def v_signup(request: Request,message: str = None):
    return templates.TemplateResponse("signup.html", {"request": request,"message":message})


@app.get("/login")
def v_login(request: Request,message: str = None):
    print("inside login")
    print(message)
    if(message is not None):
        print("message is not none")
    else:
        print("message is none")
    return templates.TemplateResponse("login.html", {"request": request,"message":message})

@app.post("/signup")
async def signup(request: Request,message: str = None):
    data = await request.json()

    if data['type'] == 'organiser':
        user = Organiser_l(**data)
    elif data['type'] == 'student':
        user = Student_l(**data)
    elif data['type'] == 'outsider':
        user = Outsider_l(**data)
    else:
        return {"error": "Invalid user type"}

    # Store user data (you'll likely use a database here)
    print("User Data:", user)
    return {"message": "Signup successful"}

@app.post("/login")
async def login(user: User_l):
    if user.username in user_database:
        stored_user = user_database[user.username]
        if stored_user["password"] == user.password:
            token = user.username
            return {"token": token, "message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# @app.post("/student", status_code=status.HTTP_201_CREATED)
# async def new_student(student: Student):
#     cur = conn.cursor()
#     cur.execute(
#         f"INSERT INTO A4_student (name,username,roll_number,password,onlystudent) VALUES ('{student.name}', '{student.username}','{student.rollno}','{student.password}','{student.only_student}')")
#     cur.close()
#     conn.commit()
#     conn.close()
#     return

@app.get("/admin")
async def read_root(request: Request):
    token = request.cookies.get("token")
    cur = conn.cursor()
    cur.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cur.fetchall()
    for i in range(len(tables)):
        cur.execute(
            f"SELECT column_name FROM information_schema.columns WHERE table_name = '{tables[i][0]}'")
        temp1 = cur.fetchall()
        temp1 = [x[0] for x in temp1]
        print(temp1)
        cur.execute(f"SELECT * FROM {tables[i][0]}")
        temp2 = cur.fetchall()
        tables[i]=(tables[i][0],temp1,temp2)
    return templates.TemplateResponse("/admin/admin.html", {"request": request,"tables":tables,"page":"admin"})

