from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date
from app.schemas import LedgerEntry
from app.models import Transactions
from app.database import get_db
from app import models


app=FastAPI()

@app.get("/")
def home():
    return{"message":"Finance ledger API is running"}

@app.post("/add")
def add_entry(entry: LedgerEntry, db: Session = Depends(get_db)) -> dict:
    new_txn = Transactions(
        name=entry.name,
        description=entry.description,
        amount=entry.amount,
        date=entry.date,
        category=entry.category,
    )
    db.add(new_txn)
    db.commit()
    db.refresh(new_txn)

    return {"message": "Entry added successfully", "id": new_txn.id}

@app.get("/entries")
def get_all_entries(db: Session = Depends(get_db)):
    return db.query(Transactions).all()

@app.put("/entries/{entry_id}")
def update_entry(entry_id: int, updated_entry: LedgerEntry, db: Session = Depends(get_db)):
    txn = db.query(Transactions).filter(Transactions.id == entry_id).first()

    if not txn:
        return {"error": "Entry not found"}
    txn.name = updated_entry.name
    txn.description = updated_entry.description
    txn.amount = updated_entry.amount
    txn.date = updated_entry.date
    txn.category = updated_entry.category

    db.commit()
    db.refresh(txn)

    return txn


@app.delete("/entries/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    txn = db.query(Transactions).filter(Transactions.id == entry_id).first()
    if not txn:
        return {"error": "Entry not found"}
    db.delete(txn)
    db.commit()
    return {"message": "Entry deleted successfully"}
