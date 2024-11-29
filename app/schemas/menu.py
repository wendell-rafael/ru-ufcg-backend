from pydantic import BaseModel
from datetime import date
from typing import Optional


class MenuBase(BaseModel):
    meal: str
    date: date
    option_1: Optional[str] = None
    option_2: Optional[str] = None
    vegan_option: Optional[str] = None
    vegetarian_option: Optional[str] = None
    salad_1: Optional[str] = None
    salad_2: Optional[str] = None
    garnish: Optional[str] = None
    side_1: Optional[str] = None
    side_2: Optional[str] = None
    side_3: Optional[str] = None
    juice: Optional[str] = None
    dessert: Optional[str] = None
    coffee: Optional[str] = None
    bread: Optional[str] = None


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuBase):
    pass


class MenuOut(MenuBase):
    id: int

    class Config:
        orm_mode = True
