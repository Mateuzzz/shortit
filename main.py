from fastapi import FastAPI, Depends, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import engine
import random; import string
from fastapi.middleware.cors import CORSMiddleware


from app.database import SessionLocal
from app.models.clicks import Clicks
from app.models.urls import Urls
from pydantic import BaseModel


Clicks.metadata.create_all(bind=engine)
Urls.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Data(BaseModel):
    original_url: str
    short_code: str | None = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bizunowicz.pl"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/shortit")
def short_it(data: Data, request: Request, response: Response, db: Session = Depends(get_db)):
    if data.short_code == None:
        data.short_code = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    
    for link in db.query(Urls).all():
        if data.short_code == link.short_code:
            return {"Skrócony link już istnieje. Podaj inny"}

    new_link = Urls(short_code=data.short_code, original_url=data.original_url, ip_address=request.client.host)
    db.add(new_link);db.commit();db.refresh(new_link)

    return {"short_code": data.short_code}

@app.get("/shortit/{short_code}")
def get_short_link(short_code: str, request: Request, db: Session = Depends(get_db)):
    new_click = Clicks(ip_address=request.client.host, short_code=short_code)
    db.add(new_click);db.commit();db.refresh(new_click)

    return RedirectResponse('https://'+db.query(Urls).filter(Urls.short_code == short_code).all()[0].original_url)
