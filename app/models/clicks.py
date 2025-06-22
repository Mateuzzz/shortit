from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
import datetime

class Clicks(Base):
    __tablename__ = "clicks"
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, nullable=False)
    clicked_at = Column(String, nullable=False, default=datetime.datetime.now)
    ip_address = Column(String, nullable=False)