from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    meal = Column(String, nullable=False)  # Ex: Almoço, Jantar
    date = Column(Date, nullable=False)
    option_1 = Column(String, nullable=True)
    option_2 = Column(String, nullable=True)
    vegan_option = Column(String, nullable=True)
    vegetarian_option = Column(String, nullable=True)
    salad_1 = Column(String, nullable=True)
    salad_2 = Column(String, nullable=True)
    garnish = Column(String, nullable=True)
    side_1 = Column(String, nullable=True)
    side_2 = Column(String, nullable=True)
    side_3 = Column(String, nullable=True)
    juice = Column(String, nullable=True)
    dessert = Column(String, nullable=True)
    coffee = Column(String, nullable=True)
    bread = Column(String, nullable=True)
