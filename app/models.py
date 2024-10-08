from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator import pydantic_items_creator, pydantic_queryset_creator
from datetime import datetime

class Course(Model):
    id = fields.IntField(pk=True)  # Primary key
    title = fields.CharField(max_length=255)  # Post title
    description = fields.TextField()  # Post content
    author = fields.CharField(max_length=100)  # Author name
    price = fields.FloatField(null=True )
    created_at = fields.DatetimeField(auto_now_add=True)  # Automatically set to current time on creation
    updated_at = fields.DatetimeField(auto_now=True)  # Automatically updates when the record is modified
    is_published = fields.BooleanField(default=True)  # Optional field to mark post as published or not


    def __str__(self):
        return self.title

    class PydanticMeta:
        table = "courses"  # Set the table name in the database





Course_Pydantic = pydantic_model_creator(Course, name="Course")
CourseIn_Pydantic = pydantic_model_creator(Course, name="CourseIn", exclude_readonly=True)


class Blogpost(Model):
    id = fields.IntField(pk=True)  # Primary key
    title = fields.CharField(max_length=255)  # Post title
    body = fields.TextField()  # Post content
    author = fields.CharField(max_length=100)  # Author name
    created_at = fields.DatetimeField(auto_now_add=True)  # Automatically set to current time on creation
    updated_at = fields.DatetimeField(auto_now=True)  # Automatically updates when the record is modified
    is_published = fields.BooleanField(default=True)  # Optional field to mark post as published or not



    def __str__(self):
        return self.title

    class PydanticMeta:
        table = "blogpost"  # Set the table name in the database




Blog_Pydantic = pydantic_model_creator(Blogpost, name="Blog")
BlogIn_Pydantic = pydantic_model_creator(Blogpost, name="BlogIn", exclude_readonly=True)


class Items(Model):
    id = fields.IntField(pk=True)  # Primary key
    title = fields.CharField(max_length=255)  # Post title
    body = fields.TextField()  # Post content
    author = fields.CharField(max_length=100)  # Author name
    created_at = fields.DatetimeField(auto_now_add=True)  # Automatically set to current time on creation
    updated_at = fields.DatetimeField(auto_now=True)  # Automatically updates when the record is modified
    is_published = fields.BooleanField(default=True)  # Optional field to mark post as published or not



    def __str__(self):
        return self.title

    class PydanticMeta:
        table = "item"  # Set the table name in the database




Items_Pydantic = pydantic_model_creator(Items, name="Items")
ItemsIn_Pydantic = pydantic_model_creator(Items, name="ItemsIn", exclude_readonly=True)


TORTOISE_ORM = {
    "connections": {
        # "default": "asyncpg://jamezslim90:zmgHh7aNwQk9@ep-cold-leaf-25567838.us-west-2.aws.neon.tech/fastapi-school-app"
        "default": "asyncpg://jamezslim90:zmgHh7aNwQk9@ep-cold-leaf-25567838.us-west-2.aws.neon.tech/fast-schoolapp"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # Include Aerich models
            "default_connection": "default",
        },
    },
}
