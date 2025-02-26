from typing import List
from sqlalchemy import Session
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.todo import TodoRequest, TodoResponse
import crud
from database import sessionlocal

router = APIRouter(prefix="/todos")

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", code=status.HTTP_201_CREATED)
def create_db(todo:TodoRequest, db:Session = Depends(get_db)):
    todo = crud.create_todo(db, todo)
    return todo

@router.get("", response_model=List[TodoResponse])
def get_todos(complete:bool =None, db:Session=Depends(get_db)):
    todos = crud.read_todos(db, complete)
    return todos

@router.get("/{id}")
def get_todo_by_id(id: int, db: Session=Depends(get_db)):
    todo = crud.read_todo(db, id)
    if todo is None:
        raise HTTPException(status_code=404, detail="To do not gound")
    return todo

@router.put("/{id}")
def update_todo(id: int, todo:TodoRequest, db: Session=Depends(get_db)):
    todo = crud.update_todo(db=db, id=id, todo=todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="To do not found")
    
    return todo

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_todo(id: int, db: Session=Depends(get_db)):
    res = crud.delete_todo(db=db, id=id)
    if res is None:
        raise HTTPException(status_code=404, detail="To do not found")
    
    return res

