from sqlalchemy.orm import Session
from models.app_model import AppModel
from datetime import datetime
def create(db:Session,name:str,description:str):
    new_app=AppModel(name=name,description=description)
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app
def getAll(db:Session):
    return db.query(AppModel).all()
def getById(db:Session,app_id:int):
    return db.query(AppModel).filter(AppModel.id==app_id).first()
def update(db: Session,app_id:int,name:str,description:str):
    app=db.query(AppModel).filter(AppModel.id==app_id).first()
    if app:
        app.name=name
        app.description=description
        app.updated_at=datetime.utcnow()
        db.commit()
        db.refresh(app)
    return app
def delete(db:Session,app_id: int):
    app=db.query(AppModel).filter(AppModel.id==app_id).first()
    if app:
        db.delete(app)
        db.commit()
    return app
