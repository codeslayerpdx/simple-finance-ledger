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

@app.put("/update/{entry_id}")
def update_entry(entry_id:int,updated_entry:LedgerEntry):
    for index, entry in enumerate(ledger):
        if entry.id==entry_id:
            ledger[index]=updated_entry
            return{"message":"entry updated successfully"}
    return{"error":"entry not found"}


@app.delete("/delete/{entry_id}")
def delete_entry(entry_id:int):
    for index,entry in enumerate(ledger):
        if entry.id==entry_id:
            ledger.pop(index)
            return{"message":"entry deleted successfully"}
        return{"error":"entry not found"}
