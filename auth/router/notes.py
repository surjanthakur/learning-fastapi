from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from dbConnection import get_session
from dbTables import Notes
from typing import List
from pydanticModels import ShowNotes


router = APIRouter(prefix="/notes", tags=["notes"])


# Endpoint to get all notes
@router.get("/all", response_model=List[ShowNotes])
def get_all_notes(session_db: Session = Depends(get_session)):
    try:
        all_notes = session_db.exec(select(Notes)).all()
        if not all_notes:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="No notes found 😳"
            )
        return all_notes
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while fetching all notes from db 😳: {str(err)}",
        )


# Endpoint to create a new note
@router.post("/create/{user_id}", response_model=ShowNotes)
def create_new_note(
    user_id: str, notes: ShowNotes, session_db: Session = Depends(get_session)
):
    try:
        new_notes = Notes(title=notes.title, content=notes.content)
        if new_notes.owner_id == user_id:
            session_db.add(new_notes)
            session_db.commit()
            session_db.refresh(new_notes)
            return notes
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not authorized to create notes for this user 😳",
        )
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating a new note in db 😳: {str(err)}",
        )
