from sqlalchemy.orm import Session
from app.models.menu import Menu
from app.schemas.menu import MenuCreate, MenuUpdate


def get_menu(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()


def get_menus(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Menu).offset(skip).limit(limit).all()


def create_menu(db: Session, menu_data: MenuCreate):
    db_menu = Menu(**menu_data.dict())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def update_menu(db: Session, menu_id: int, menu_data: MenuUpdate):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not db_menu:
        return None
    for key, value in menu_data.dict(exclude_unset=True).items():
        setattr(db_menu, key, value)
    db.commit()
    db.refresh(db_menu)
    return db_menu


def delete_menu(db: Session, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if not db_menu:
        return None
    db.delete(db_menu)
    db.commit()
    return db_menu
