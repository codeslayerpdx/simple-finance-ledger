from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Transactions(Base):
    _tablename_ = "ledger_entries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    category = Column(String, nullable=True)