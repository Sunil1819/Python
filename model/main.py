from fastapi import FastAPI
from config.postgresdb_config import Base, engine
from routes.app_routes import router
app=FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)
@app.get("/")
def read_root():
    return {"message":"Welcome to the FastAPI app!"}
