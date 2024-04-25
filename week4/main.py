from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.add_middleware(SessionMiddleware, secret_key="myscret_")
sign_in=False
verify=None
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
        global sign_in
        if not username or not password:
               return RedirectResponse(url="/error?message=請輸入帳號或密碼", status_code=303)
        if verify==False :
                sign_in=False
                return RedirectResponse(url="/error?message=帳號，或密碼錯誤", status_code=303)
        if verify==True :
                sign_in=True
                return RedirectResponse(url="/member", status_code=303)
      
@app.get("/error")
async def error(request: Request,message: str):
    return templates.TemplateResponse("error.html", {"request":request, "message": message})
@app.get("/member", response_class=RedirectResponse)
async def success(request: Request):
        global sign_in
        if request.session["SIGNED-IN"]==False:
                return RedirectResponse(url="/signout", status_code=303)
        if request.session["SIGNED-IN"]==True:
                return templates.TemplateResponse("member.html", {"request": request})             

@app.get("/signout",response_class=RedirectResponse)
async def signout(request: Request):
        global sign_in
        print("第一次= ",sign_in)
        if sign_in==True :
                request.session["SIGNED-IN"]=True
                sign_in=False
                return RedirectResponse(url="/member", status_code=303)
        if sign_in==False :
                request.session["SIGNED-IN"]=False
                sign_in==False
                return RedirectResponse(url="/", status_code=303)
        
        
         
        
