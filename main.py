from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from calculation import equal_yearly_payment

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Settlement(BaseModel):
    amount: float
    years: int
    interest: float


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/calculation", response_class=HTMLResponse)
def calculate_amount(settlement: Settlement, request: Request):
    yearly_payment = equal_yearly_payment(settlement.interest, settlement.years, settlement.amount)
    return templates.TemplateResponse("index.html", {"request": request, "yearly_payment": yearly_payment})
