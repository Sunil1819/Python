from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from config.postgresdb_config import SessionLocal
import service.app_service as AppService
from pydantic import BaseModel
router=APIRouter()
class AppCreate(BaseModel):
    name:str
    description:str
class AppResponse(AppCreate):
    id: int
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/apps",response_model=AppResponse)
def create_app(app:AppCreate,db:Session=Depends(get_db)):
    return AppService.create(db,app.name,app.description)
@router.get("/apps", response_model=list[AppResponse])
def get_all_apps(db:Session=Depends(get_db)):
    return AppService.getAll(db)
@router.get("/apps/{app_id}", response_model=AppResponse)
def get_app_by_id(app_id: int,db:Session=Depends(get_db)):
    app=AppService.getById(db,app_id)
    if not app:
        raise HTTPException(status_code=404, detail="App not found")
    return app
@router.put("/apps/{app_id}",response_model=AppResponse)
def update_app(app_id: int,app_data:AppCreate,db:Session=Depends(get_db)):
    app=AppService.update(db,app_id,app_data.name,app_data.description)
    if not app:
        raise HTTPException(status_code=404,detail="App not found")
    return app
@router.delete("/apps/{app_id}")
def delete_app(app_id:int,db:Session=Depends(get_db)):
    app=AppService.delete(db, app_id)
    if not app:
        raise HTTPException(status_code=404,detail="App not found")
    return {"message": "App deleted successfully"}
