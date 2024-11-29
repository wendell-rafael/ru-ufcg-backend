from sqlalchemy.orm import Session
from app.crud.menu import get_menus, create_menu, update_menu, delete_menu
from app.schemas.menu import MenuCreate, MenuUpdate


def list_menus(db: Session, skip: int = 0, limit: int = 10):
    return get_menus(db, skip=skip, limit=limit)


def create_new_menu(db: Session, menu_data: MenuCreate):
    return create_menu(db, menu_data)


def update_existing_menu(db: Session, menu_id: int, menu_data: MenuUpdate):
    return update_menu(db, menu_id, menu_data)


def delete_existing_menu(db: Session, menu_id: int):
    return delete_menu(db, menu_id)
