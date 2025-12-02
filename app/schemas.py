from pydantic import BaseModel
from datetime import date

class LedgerEntry(BaseModel):
    name: str
    description: str
    amount: float
    date: date
    category: str
