from header import *

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
    cur = conn.cursor()
    cur.execute("SELECT college_name FROM A4_college")
    colleges = cur.fetchall()
    for i in range(len(colleges)):
        colleges[i] = colleges[i][0]
    return templates.TemplateResponse("signup.html", {"request": request,"message":message,"colleges":colleges})


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
        register_organizer(user.name,user.roll_no,user.username,user.password,False,user.enrollment_key)
    elif data['type'] == 'student':
        user = Student_l(**data)
        register_student(user.name,user.roll_no,user.username,user.password,True)
    elif data['type'] == 'outsider':
        user = Outsider_l(**data)
        register_outsider(user.name,user.username,user.password,user.college)
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


@app.post("/register_outsider_for_event",status_code=status.HTTP_201_CREATED)
async def read_root(request=Request,event_id=int, username=str):
    register_outsider_for_event(event_id, username)
    
@app.get("/fetch_event_details",status_code=status.HTTP_200_OK)
async def read_root():
    fetch_event_details()
    
@app.post("/register_student_for_event",status_code=status.HTTP_201_CREATED)
async def read_root(request=Request,event_id=int, username=str):
    register_student_for_event(event_id, username)
    
@app.post("/allow_student_to_volunteer",status_code=status.HTTP_201_CREATED)
async def read_root(request=Request,event_id=int, username=str):
    allow_student_to_volunteer(event_id, username)
    
@app.get("/view_participants_for_event",status_code=status.HTTP_200_OK)
async def read_root(request=Request,desired_event_id=int):
    view_participants_for_event(desired_event_id)
    
@app.get("/view_volunteers_for_event",status_code=status.HTTP_200_OK)
async def read_root(request=Request,desired_event_id=int):
    view_volunteers_for_event(desired_event_id)
    
@app.post("/change_event_details",status_code=status.HTTP_201_CREATED)
async def read_root(request=Request,desired_event_id=int, new_event_name=str, new_event_type=str, new_event_description=str):
    change_event_details(desired_event_id, new_event_name, new_event_type, new_event_description)
    
@app.get("/check_username_in_student_table",status_code=status.HTTP_200_OK)
async def read_root(request=Request,username=str):
    check_username_in_student_table(username)
    
@app.get("/check_username_in_outsider_table",status_code=status.HTTP_200_OK)
async def read_root(request=Request,username=str):
    check_username_in_outsider_table(username)
    
@app.get("/check_username_in_organizer_to_student_table",status_code=status.HTTP_200_OK)
async def read_root(request=Request,username=str):
    check_username_in_organizer_to_student_table(username)