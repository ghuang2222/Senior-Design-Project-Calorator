from sqlalchemy import Column, Integer, String
from database import Base

class FoodInfo(Base):
    __tablename__ = "food_info"


    label = Column(String(255), primary_key=True, index=True)
    calories = Column(Integer)
    protein = Column(Integer)
    carbohydrates = Column(Integer)
    fats = Column(Integer)
    fiber = Column(Integer)
    sugars = Column(Integer)
    sodium = Column(Integer)
