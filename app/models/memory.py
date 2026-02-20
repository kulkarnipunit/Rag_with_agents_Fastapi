from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    content = Column(String)
    embedding = Column(String)