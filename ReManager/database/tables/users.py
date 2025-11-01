from sqlalchemy import Column, String, Boolean
from ..base import Base

class Users(Base):
  user_id = Column(String, primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False)
  password_hash = Column(String, nullable=False)