from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.menu import MenuCreate, MenuUpdate, MenuOut
from app.service.menu import list_menus, create_new_menu, update_existing_menu, delete_existing_menu

router = APIRouter()


@router.get("/", response_model=list[MenuOut])
def get_all_menus(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_menus(db, skip, limit)


@router.post("/", response_model=MenuOut)
def create_menu(menu_data: MenuCreate, db: Session = Depends(get_db)):
    return create_new_menu(db, menu_data)


@router.put("/{menu_id}", response_model=MenuOut)
def update_menu(menu_id: int, menu_data: MenuUpdate, db: Session = Depends(get_db)):
    menu = update_existing_menu(db, menu_id, menu_data)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu


@router.delete("/{menu_id}", response_model=MenuOut)
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = delete_existing_menu(db, menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu
