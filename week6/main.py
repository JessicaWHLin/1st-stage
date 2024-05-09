from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="test2",
  password="1234",
  database="website"
  )
mycursor = mydb.cursor()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="myscret_")

def verify(request: Request, username: str, password: str):
        sql_verify="select id, name, username from member where username= %s and password=%s"
        val_verify=(username,password)
        mycursor.execute(sql_verify,val_verify)
        result_verify=mycursor.fetchone() 
        if result_verify:
                user_id, user_name,user_username = result_verify
                request.session["user_id"]=user_id
                request.session["user_name"]=user_name
                request.session["user_username"]=user_username
                return True
        else:
                return False

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
            request=request, name="index.html")

@app.post("/signup", response_class=RedirectResponse)
async def signup(request:Request, iniName : str=Form(...), iniUsername: str=Form(...), iniPassword: str=Form(...)):
        sql_check="SELECT * FROM member WHERE username = %s"
        val_check=(iniUsername,) 
        mycursor.execute(sql_check,val_check)
        check_result=mycursor.fetchone()
        if check_result == None:
                sql_add="insert into member(name,username,password)values( %s,%s,%s )"
                val_add=(iniName,iniUsername,iniPassword)
                mycursor.execute(sql_add,val_add)
                mydb.commit()
                return RedirectResponse(url="/",status_code=303)
        else:
                return RedirectResponse(url="/error?message=重複帳號", status_code=303)
        
@app.post("/signin" , response_class=RedirectResponse)
async def signin(request: Request, username : str=Form(None), password: str= Form(None)):
        veri=verify(request,username,password)
        if veri==True :
                return RedirectResponse(url="/member", status_code=303)
        else:
                return RedirectResponse(url="/error?message=帳號，或密碼錯誤", status_code=303)

@app.get("/error",response_class=HTMLResponse)
async def error(request: Request,message: str):
    return templates.TemplateResponse("error.html", {"request":request, "message": message})

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
        sql_query="select member.name,content from message join member on message.member_id=member.id order by message.id desc"
        mycursor.execute(sql_query)
        messages=mycursor.fetchall()
        meg=[{"name":x,"message":y} for x,y in messages]    
        if request.session.get("user_id")!=None:
                current_name=request.session.get("user_name")
                return templates.TemplateResponse("member.html",{"request":request, "current_name":current_name,"messages":meg})
        else:
                return RedirectResponse(url="/", status_code=303)        

@app.post("/createMessage", response_class=RedirectResponse)
async def read_message(request:Request, message :str=Form(None)):
       user_id=request.session.get("user_id")
       sql_insert="insert into message(member_id,content)values(%s,%s)"
       val_insert=(user_id,message)
       mycursor.execute(sql_insert,val_insert)
       mydb.commit()
       return RedirectResponse(url="/member",status_code=303)  

@app.get("/signout",response_class=RedirectResponse)
async def signout(request: Request):    
        request.session["user_id"]=None
        request.session["user_name"]=None
        request.session["user_username"]=None
        return RedirectResponse(url="/member", status_code=303)

   