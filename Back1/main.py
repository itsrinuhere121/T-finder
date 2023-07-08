from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:3000",  # Add the URL of your frontend application
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def read_root():
    return {"Hello": "World"}
@app.get("/location/{q}")
def read_item(q:str):
    data = dict()
    ls =  list()
    data["city"]="hyderabad"
    data["locations"]=["charminar","golcondafort","hussainsagar"] 
    ls.append(data)
    data = dict()
    data["city"] = "warangal"
    data["locations"]=["fort","Khila","100 pillers temple"]
    ls.append(data)
    print(ls)
    for i in ls : 
        if i["city"] == q:
            return i
    return {}
