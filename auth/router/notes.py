from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from dbConnection import get_session
from dbTables import Notes
from pydanticModels import ShowNotes, InputNotes


router = APIRouter(prefix="/notes", tags=["notes"])


# Endpoint to get all notes
@router.get("/all")
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
@router.post("/create", response_model=ShowNotes)
def create_new_note(notes_data: InputNotes, session_db: Session = Depends(get_session)):
    try:
        new_notes = Notes(
            title=notes_data.title, content=notes_data.content, owner=notes_data.owner
        )
        session_db.add(new_notes)
        session_db.commit()
        session_db.refresh(new_notes)
        return new_notes
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating a new note in db 😳: {str(err)}",
        )
