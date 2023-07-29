from pydantic import BaseModel, UUID4
from typing import List, Optional

class DishBase(BaseModel):
    title: str
    description: str
    price: Optional[float] = None

class DishCreate(DishBase):
    pass

class Dish(DishBase):
    id: UUID4
    menu_id: UUID4
    submenu_id: Optional[UUID4] = None

    class Config:
        orm_mode = True

class SubMenuBase(BaseModel):
    title: str
    description: str

class SubMenuCreate(SubMenuBase):
    pass

class SubMenu(SubMenuBase):
    id: UUID4
    menu_id: UUID4
    dishes: List[Dish] = []

    class Config:
        orm_mode = True

class MenuBase(BaseModel):
    title: str
    description: str

class MenuCreate(MenuBase):
    pass

class Menu(MenuBase):
    id: UUID4
    submenus: List[SubMenu] = []

    class Config:
        orm_mode = True