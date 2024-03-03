from header import *

@app.get("/")
async def read_root(request: Request):
    user= getfrontenduser(request.cookies.get("token"))
    return templates.TemplateResponse("index.html", {"request": request, "page": "home","user":user})

@app.get("/events")
def read_root(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    events = getalleventstable()
    return templates.TemplateResponse("/events/events.html", {"request": request, "events": events,"message":message,"page":"events","user":user})

@app.get("/about")
def read_root(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    return templates.TemplateResponse("about.html", {"request": request,"message":message, "page": "about","user":user})

@app.get("/accomodation")
def read_root(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_outsider == 0):
        return RedirectResponse("/events?message=You are not authorized to view this page",status_code=302)
    hallname = gethallname(user.username)
    return templates.TemplateResponse("accomodation.html", {"request": request,"message":message, "page": "accomodation","user":user,"hallname":hallname})

@app.get("/profile")
def read_root(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_logged_in == 0):
        return RedirectResponse("/events?message=Please login to see this page",status_code=302)
    if(user.is_student == 1):
        temp= getstudentdetails(user.username)
    elif user.is_organiser == 1:
        temp = getorganiserdetails(user.username)
    elif user.is_outsider == 1:
        temp = getoutsiderdetails(user.username)
    return templates.TemplateResponse("profile.html", {"request": request,"message":message, "page": "profile","user":user,"profile":temp})

@app.get("/participants")
def read_root(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_logged_in == 0):
        return RedirectResponse("/events?message=Please login to see this page",status_code=302)
    if(user.is_organiser == 0):
        return RedirectResponse("/events?message=You are not authorized to view this page",status_code=302)
    students = getallstudents()
    outsiders = getalloutsiders()
    organisers = getallorganisers()
    return templates.TemplateResponse("/admin/participants.html", {"request": request,"message":message, "page": "participants","user":user,"students":students,"outsiders":outsiders,"organisers":organisers})

@app.get("/create_user")
def read_root(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_organiser == 0):
        return RedirectResponse("/events?message=You are not authorized to view this page",status_code=302)
    keys = getallenrollments()
    colleges = getallcollegenames()
    return templates.TemplateResponse("/admin/createuser.html", {"request": request,"message":message, "page": "create_user","user":user,"colleges":colleges,"keys":keys})

@app.get("/signup")
def v_signup(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_logged_in == 1):
        return RedirectResponse("/events?message=You are already logged in or log out to sign up",status_code=302)
    colleges = getallcollegenames()
    return templates.TemplateResponse("signup.html", {"request": request,"message":message,"colleges":colleges,"user":user})


@app.get("/login")
def v_login(request: Request,message: str = None):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_logged_in == 1):
        return RedirectResponse("/events?message=You are already logged in or log out to log in",status_code=302)
    print("inside login")
    print(message)
    if(message is not None):
        print("message is not none")
    else:
        print("message is none")
    return templates.TemplateResponse("login.html", {"request": request,"message":message,"user":user})

@app.post("/deleteuser/{username}")
async def deleteuser(request: Request,username:str):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_organiser == 0):
        return {"message": "You are not authorized to delete", "status": 0}
    data = await request.json()
    temp = data['type']
    if temp == 1:
        print("deleting student")
        delete_a_student(username)
        return {"message": "Deleted successfully", "status": 1}
    elif temp == 2:
        print("deleting outsider")
        delete_a_outsider(username)
        return {"message": "Deleted successfully", "status": 1}
    elif temp == 3:
        print("deleting organiser")
        delete_a_organiser(username)
        return {"message": "Deleted successfully", "status": 1}
    
    return {"message": "Unable to delete", "status": 0}

@app.post("/signup")
async def signup(request: Request):
    data = await request.json()
    if data['type'] == 'organiser':
        user = Organiser_l(**data)
        temp = checkfororganiser(user)
        if temp == 1:
            return {"message": "Username already exists", "status": 0}
        elif temp == 2:
            return {"message": "Roll number already exists", "status": 0}
        elif temp == 3:
            return {"message": "Enrollment key does not exist", "status": 0}
        register_organizer(user.name,user.roll_no,user.username,user.password,False,user.enrollment_key)
        return {"message": "Signup successful", "status": 1,"token":user.username}
    elif data['type'] == 'student':
        user = Student_l(**data)
        temp = checkforstudent(user)
        if temp == 1:
            return {"message": "Username already exists", "status": 0}
        elif temp == 2:
            return {"message": "Roll number already exists", "status": 0}
        register_student(user.name,user.roll_no,user.username,user.password,True)
        return {"message": "Signup successful", "status": 1,"token":user.username}
    elif data['type'] == 'outsider':
        user = Outsider_l(**data)
        temp = checkforoutsider(user)
        if temp == 1:
            return {"message": "Username already exists", "status": 0}
        register_outsider(user.name,user.username,user.password,user.college)
        allocate_outsider_to_hall(user.username)
        return {"message": "Signup successful", "status": 1,"token":user.username}
    else:
        return {"message": "Invalid user type", "status": 0}


@app.post("/login")
async def login(user: User_l):
    temp = checkforuser(user)
    print(temp)
    if temp == 1:
        return {"message": "Invalid username or password", "status": 0}
    else:
        return {"message": "Login successful", "status": 1,"token":user.username}


@app.get("/admin")
async def read_root(request: Request):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_organiser == 0):
        return RedirectResponse("/events?message=You are not authorized to view this page",status_code=302)
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
    return templates.TemplateResponse("/admin/admin.html", {"request": request,"tables":tables,"user":user,"page":"admin"})

@app.get("/event_analytics/{event_id}")
async def read_root(request: Request,event_id:int):
    user= getfrontenduser(request.cookies.get("token"))
    if(user.is_organiser == 0):
        return RedirectResponse("/events?message=You are not authorized to view this page",status_code=302)
    event = geteventdetails(event_id)
    Student, Outsider,volunteers = getalleventparticipants(event_id)
    return templates.TemplateResponse("/admin/event_analytics.html", {"request": request,"event":event,"participants":Student,"outsiders":Outsider,"volunteers":volunteers,"user":user,"page":"eventdetails"})

@app.post("/register_event")
async def read_root(request: Request):
    try:
        data = await request.json()
        username = data['token']
        type = data['type']
        event_id = data['event_id']
        is_student = data['is_student']
        if(type==1):
            if is_student:
                register_student_for_event(event_id,username)
                return {"message": "Registered successfully", "status": 1}
            else:
                register_outsider_for_event(event_id,username)
                return {"message": "Registered successfully", "status": 1}
        # register
        else:
            allow_student_to_volunteer(event_id,username)
            return {"message": "Volunteered successfully", "status": 2}
    except:
        return {"message": "Error", "status": 0}     
    # volunteer
    

# @app.post("/register_outsider_for_event",status_code=status.HTTP_201_CREATED)
# async def read_root(request=Request,event_id=int, username=str):
#     register_outsider_for_event(event_id, username)
    
# @app.get("/fetch_event_details",status_code=status.HTTP_200_OK)
# async def read_root():
#     fetch_event_details()
    
# @app.post("/register_student_for_event",status_code=status.HTTP_201_CREATED)
# async def read_root(request=Request,event_id=int, username=str):
#     register_student_for_event(event_id, username)
    
# @app.post("/allow_student_to_volunteer",status_code=status.HTTP_201_CREATED)
# async def read_root(request=Request,event_id=int, username=str):
#     allow_student_to_volunteer(event_id, username)
    
# @app.get("/view_participants_for_event",status_code=status.HTTP_200_OK)
# async def read_root(request=Request,desired_event_id=int):
#     view_participants_for_event(desired_event_id)
    
# @app.get("/view_volunteers_for_event",status_code=status.HTTP_200_OK)
# async def read_root(request=Request,desired_event_id=int):
#     view_volunteers_for_event(desired_event_id)
    
# @app.post("/change_event_details",status_code=status.HTTP_201_CREATED)
# async def read_root(request=Request,desired_event_id=int, new_event_name=str, new_event_type=str, new_event_description=str):
#     change_event_details(desired_event_id, new_event_name, new_event_type, new_event_description)
    
# @app.get("/check_username_in_student_table",status_code=status.HTTP_200_OK)
# async def read_root(request=Request,username=str):
#     check_username_in_student_table(username)
    
# @app.get("/check_username_in_outsider_table",status_code=status.HTTP_200_OK)
# async def read_root(request=Request,username=str):
#     check_username_in_outsider_table(username)
    
# @app.get("/check_username_in_organizer_to_student_table",status_code=status.HTTP_200_OK)
# async def read_root(request=Request,username=str):
#     check_username_in_organizer_to_student_table(username)
    