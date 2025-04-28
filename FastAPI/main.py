import requests
from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import engine,get_db
from models import Base,User
from schema import CreateUser

# Initialize Database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI with Swagger metadata
app = FastAPI(
    title="User Management API",
    description="An API to manage users. You can create, read, update, and delete users using this API.",
    version="1.0.0"
)

@app.get("/users",tags=["Users"],summary="get all the users",description="Fetches all users from the database.")
def get_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return {"message":users}


@app.post("/users",tags=["Users"],summary="create new user",description="Creates a new user with email and name.")
def create_user(payload:CreateUser,db:Session=Depends(get_db)):
    new_user = User(email=payload.email,name=payload.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":new_user}


@app.get("/users/{userId}", tags=["Users"], summary="Get user by ID", description="Fetches a user by their ID.")
def get_user_by_id(userId:int,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == userId).first()
    return {"message":user}


@app.put("/users/{userId}", tags=["Users"], summary="Update user by ID", description="Updates the email and name of a user by ID.")
def update_user(userId:int,payload:CreateUser,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id==userId).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    user.email = payload.email
    user.name = payload.name
    db.commit()
    db.refresh(user)
    return {"message":user}


@app.delete("/users/{userId}", tags=["Users"], summary="Delete user by ID", description="Deletes a user by their ID.")
def delete_user(userId:int,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == userId).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message":user}



@app.get("/products",tags=["Products"],summary="get all the products",description="Fetch all the products from the fakestore.api")
def get_products():
    request = requests.get("https://fakestoreapi.com/products")
    response = request.json()
    return {"message":response}

@app.get("/products/{productId}",tags=["Products"],summary="get product by id",description="Fetch a product by id from the fakestore.api")
def get_products(productId:int):
    request = requests.get(f"https://fakestoreapi.com/products/{productId}")
    response = request.json()
    return {"message":response}