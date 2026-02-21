from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base

class Memory(Base):
    __tablename__ = "memories"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    content = Column(Text)
    embedding = Column(Text)