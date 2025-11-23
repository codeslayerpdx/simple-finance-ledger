from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app=FastAPI()

@app.get("/")
def home():
    return{"message":"Finance ledger API is running"}

class LedgerEntry(BaseModel):
    id:int
    name:str
    description:str
    amount:float
    date:date
    category:str

ledger=[]

@app.post("/add")
def add_entry(entry:LedgerEntry):
    ledger.append(entry)
    return{"message":"Entry added successfully"}

@app.get("/read")
def get_all_entries():
    return ledger