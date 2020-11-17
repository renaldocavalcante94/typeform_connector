from fastapi import FastAPI
from typing import Optional
from connector.typeform import TypeformAPI


typeform_connector = FastAPI()
typeform = TypeformAPI()

@typeform_connector.get("/me")
async def get_me():
    result = typeform.me()

    return result.json()

@typeform_connector.get("/forms")
async def list_forms():

    return typeform.list_all_forms()

@typeform_connector.get("/forms/{form_id}")
async def get_form(form_id: str):

    return typeform.get_form(form_id)

@typeform_connector.get("/forms/{form_id}/responses")
async def get_responses(form_id: str, completed: bool = True):
    
    return typeform.get_responses(form_id,completed=completed)

@typeform_connector.get("/forms/{form_id}/all_responses")
async def get_all_responses(
    form_id: str,
    completed: bool = True,
    after: Optional[str] = None
    ):

    return typeform.get_all_responses(form_id,completed=completed,after=after)