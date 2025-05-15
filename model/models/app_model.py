from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from config.postgresdb_config import Base
class AppModel(Base):
    __tablename__="apps"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String)
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
