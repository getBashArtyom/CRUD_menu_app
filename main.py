from fastapi import FastAPI, Depends
from schemas import MenuCreate
from sqlalchemy.orm import Session
from db import get_db
from models import Menu

app = FastAPI()

@app.post("/menu")
def create(details: MenuCreate, db: Session = Depends(get_db)):
    to_create = Menu(
        name=details.name
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
