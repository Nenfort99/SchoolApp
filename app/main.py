from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.pages_routes import  page_router
from app.course_routes import course_router
from fastapi.staticfiles import StaticFiles

# Initialise our fastapi app
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Include routers
app.include_router(page_router)
app.include_router(course_router)



# Register Tortoise ORM
register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)