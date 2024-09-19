
from app.models import Blogpost, BlogIn_Pydantic, Blog_Pydantic
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


blog_router = APIRouter()


class Message(BaseModel):
    message: str
# Defining a simple Pydantic model for response messages (used in the delete operation), with a single field `message`.

@blog_router.get('/api/posts', response_model=List[Blog_Pydantic])
async def get_all_posts():
    return await Blog_Pydantic.from_queryset(Blogpost.all())

@blog_router.post('/api/post', response_model=Blog_Pydantic)
async def create_a_post(blogpost: BlogIn_Pydantic):
    postobj = await Blogpost.create(**blogpost.dict(exclude_unset=True))
    return await Blog_Pydantic.from_tortoise_orm(postobj)

@blog_router.get('/api/post/{id}', response_model=Blog_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def get_a_post(id: int):
    return await Blog_Pydantic.from_queryset_single(Blogpost.get(id=id))

@blog_router.put("/api/post/{id}", response_model=Blog_Pydantic, responses={404: {"model": HTTPNotFoundError}})
async def update_a_post(id: int, blogpost: BlogIn_Pydantic):
    await Blogpost.filter(id=id).update(**blogpost.dict(exclude_unset=True))
    return await Blog_Pydantic.from_queryset_single(Blogpost.get(id=id))


@blog_router.delete("/api/post/{id}", response_model=Message, responses={404: {"model": HTTPNotFoundError}})
async def delete_a_post(id: int):
    delete_obj = await Blogpost.filter(id=id).delete()

    if not delete_obj:
        raise HTTPException(status_code=404, detail="This Blogpost is not found.")
    return Message(message="Successfully Deleted")





