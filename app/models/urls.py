from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
import datetime

class Urls(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(32), nullable=False)
    short_code = Column(String, nullable=False)
    created_at = Column(String, nullable=False, default=datetime.datetime.now)
    status = Column(Boolean, nullable=False, default=True)
    ip_address = Column(String, nullable=False) 