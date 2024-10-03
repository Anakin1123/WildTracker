from fastapi import APIRouter, Query
from models import table  # Assuming 'table' is your database model
from sqlalchemy.orm import Session
from database import get_db  # Assuming you have a function to get the DB session

router = APIRouter(
    prefix="/operations",
    tags=["Operations"]
)

@router.get("/")
async def get_operations(animal: str = Query(...), db: Session = Depends(get_db)):
    # Corrected SQL query to use parameterized queries
    query = f"SELECT * FROM animal WHERE name = :animal"
    result = db.execute(query, {"animal": animal}).fetchall()
    
    # Convert result to a list of dictionaries if necessary
    return [dict(row) for row in result]