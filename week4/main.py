from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="myscret_")

def verify_password(username: str, password: str):
    if username == "test" and password == "1234":
        return True
    return False

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
            request=request, name="index.html")
        
@app.post("/signin" , response_class=RedirectResponse)
async def signin(request: Request, username : str=Form(None), password: str= Form(None)):
        verify=verify_password(username,password)
        if not username or not password:
                request.session["signed_in"]=False
                return RedirectResponse(url="/error?message=請輸入帳號或密碼", status_code=303)
        if verify==False :
                request.session["signed_in"]=False
                return RedirectResponse(url="/error?message=帳號，或密碼錯誤", status_code=303)
        if verify==True :
                request.session["signed_in"]=True
                return RedirectResponse(url="/member", status_code=303)
      
@app.get("/error",response_class=HTMLResponse)
async def error(request: Request,message: str):
    return templates.TemplateResponse("error.html", {"request":request, "message": message})
@app.get("/member", response_class=RedirectResponse)
async def success(request: Request):
        if request.session.get("signed_in")==True:
                return templates.TemplateResponse(request=request, name="member.html")
        else: 
                return RedirectResponse(url="/", status_code=303) #未登入者連進來才不會異常          

@app.get("/signout",response_class=RedirectResponse)
async def signout(request: Request):    
        if request.session.get("signed_in")==True : #點擊登出系統，要將status改為登出
                request.session["signed_in"]=False
                return RedirectResponse(url="/", status_code=303)
        else:
               return RedirectResponse(url="/member", status_code=303) #未登入者連進來才不會異常

# task4  
@app.get("/square/{integer}",response_class=HTMLResponse)
async def calculate_square(request: Request, integer : int): 
       square_result=integer**2
       return templates.TemplateResponse("square.html",{ "request":request, "integer": integer,"square_result":square_result})
