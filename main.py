from fastapi import FastAPI, HTTPEException
from pydantic import BaseModel

app = FastAPI(title= "Tasks CRUD API")


class TaskCREAT(BaseModel):
    title: str
    description: str = ""
    done: bool = False    