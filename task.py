from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
db=[]
class Virat(BaseModel):
    id:int
    name:str
@app.get("/virat")
def getitems():
    return db
@app.get("/virat/{viratid}")
def getitem(viratid:int):
    for a in db:
        if(a.id==viratid):
            return a
    raise HTTPException(status_code=404,detail="Not Found")
@app.post("/virat")
def createitem(virat:Virat):
    db.append(virat)
    return db
@app.put("/virat/{viratid}")
def updateitem(viratid:int,updatess:Virat):
    for i,a in enumerate(db):
        if(a.id==viratid):
            db[i]=updatess
            return updatess
    raise HTTPException(status_code=404,detail="Not Found")
@app.delete("/virat/{viratid}")
def deleteb(viratid:int):
    for i,a in enumerate(db):
        if(a.id==viratid):
            del db[i]
            return {"message":"Item deleted"}
    raise HTTPException(status_code=404,detail="Not Found")