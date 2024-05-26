from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

mydb = {
  "host":"localhost",
  "user":"test2",
  "password":"1234",
  "database":"website"
}
pool=mysql.connector.pooling.MySQLConnectionPool(
pool_name="mypool",
pool_size=15,
**mydb
)
connection=pool.get_connection()
mycursor = connection.cursor()
mycursor.execute("select * from member")
results=mycursor.fetchall()
for i in results:
        print(i)
mycursor.close()
connection.close()



app = FastAPI()

origins=[
        "http://127.0.0.1:8001",
       
]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

app.mount("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
        return templates.TemplateResponse(
            request=request, name="index.html")
@app.get("/example", response_class=JSONResponse)
async def example():
        return {"message":"Hello"}


