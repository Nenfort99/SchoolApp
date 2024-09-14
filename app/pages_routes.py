from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


page_router = APIRouter()

# Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


@page_router.get("/", response_class=HTMLResponse, name="home")
async def home_page(request:Request):
    return templates.TemplateResponse(name ="home.html", request = request)


@page_router.get("/about", response_class=HTMLResponse, name="about")
async def about_page(request:Request):
    return templates.TemplateResponse(name = "about.html", request = request)



@page_router.get("/courses", response_class=HTMLResponse, name="courses")
async def course_page(request:Request):
    return templates.TemplateResponse(name = "course.html", request = request)



@page_router.get("/contact", response_class=HTMLResponse, name="contact")
async def contact_page(request:Request):
    return templates.TemplateResponse(name = "contact.html", request = request)
