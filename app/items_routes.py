
from app.models import Course, CourseIn_Pydantic, Course_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


requirements_router = APIRouter()


class Message(BaseModel):
    message: str
# Defining a simple Pydantic model for response messages (used in the delete operation), with a single field `message`.

@items_router.get('/api/items', response_model=List[Items_Pydantic])
async def get_all_items():
    return await Requirements_Pydantic.from_queryset(Items.all())

@items_router.post('/api/items', response_model=Items_Pydantic)
async def create_an_item(item: ItemsIn_Pydantic):
    itemobj = await Items.create(**items.dict(exclude_unset=True))
    return await Items_Pydantic.from_tortoise_orm(itemobj)

@items_router.get('/api/items/{id}', response_model=Items_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_an_item(id: int):
    return await Items_Pydantic.from_queryset_single(Item.get(id=id))

@items_router.put("/api/items/{id}", response_model=Course_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_an_item(id: int, items: ItemsIn_Pydantic):
    await Items.filter(id=id).update(**item.dict(exclude_unset=True))
    return await Items_Pydantic.from_queryset_single(Items.get(id=id))


@course_router.delete("/api/course/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete_a_course(id: int):
    delete_obj = await Course.filter(id=id).delete()

    if not delete_obj:
        raise HTTPException(status_code=404, detail="This Course is not found.")
    return Message(message="Successfully Deleted")
