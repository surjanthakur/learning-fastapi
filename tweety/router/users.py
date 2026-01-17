from fastapi import APIRouter, HTTPException, status, Depends, Path
from database.database import get_session
from sqlmodel import Session, select
from database.sql_model import User
from validation.pydantic_schema import pydantic_user
from fastapi.responses import JSONResponse
from datetime import datetime


router = APIRouter(tags=["user routers"])


# get user by their id
@router.get("/users/{user_id}")
def get_user_by_id(
    user_id: str = Path(
        ...,
        title="enter user_id",
        description="enter the user id to access information !!",
    ),
    db: Session = Depends(get_session),
):
    statement = select(User).where(User.id == user_id)
    user = db.exec(statement).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid user_id enter the valid user id !!",
        )
    return user


# create new user
@router.post("/users/create")
def create_users(user_data: pydantic_user, db: Session = Depends(get_session)):
    new_user = User(name=user_data.name, email=user_data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=f"user: {new_user.email} created successfullt !!",
    )


# update user by id
@router.put("/users/{user_id}/update")
def update_user_by_id(
    update_data: pydantic_user,
    user_id: str = Path(
        ...,
        title="enter user_id",
        description="enter the user id to update information !!",
    ),
    db: Session = Depends(get_session),
):
    statement = select(User).where(User.id == user_id)
    user = db.exec(statement).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid user_id enter the valid user id !!",
        )
    updated_dict = update_data.model_dump(exclude_unset=True)
    for key, value in updated_dict.items():
        setattr(user, key, value)
    user.updated_at = datetime.now()
    db.add(user)
    db.commit()
    db.refresh(user)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=f"user: {user_id} updated successfully !!",
    )


# delete user by id
@router.delete("/users/{user_id}/delete")
def delete_user_by_id(
    user_id: str = Path(..., description="enter the user id to update information !!"),
    db: Session = Depends(get_session),
):
    statement = select(User).where(User.id == user_id)
    user = db.exec(statement=statement).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="invalid user_id enter the valid user id !!",
        )
    db.delete(user)
    db.commit()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=f"user: {user_id} deleted successfully !!",
    )
