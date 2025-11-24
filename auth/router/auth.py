from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from dbConnection import get_session
from dbConnection import get_session
from dbTables import User
from pwdlib import PasswordHash

hash_password = PasswordHash.recommended()


# Function to hash user passwords ------------------------------------------------------->
def hash_user_password(password: str) -> str:
    return hash_password.hash(password)


# Router for authentication-related endpoints ------------------------------------------->
router = APIRouter(prefix="/auth", tags=["auth user"])


# Endpoint to register a new user
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: User, session_db: Session = Depends(get_session)):
    hash_pass = hash_user_password(user.password)
    new_user = User(username=user.username, email=user.email, password=hash_pass)
    try:
        session_db.add(new_user)
        session_db.commit()
        session_db.refresh(new_user)
        return {"message": "User registered successfully 😊"}
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while registering the user 😳: {str(err)}",
        )
