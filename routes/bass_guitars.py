from fastapi import APIRouter
from typing import Union

router = APIRouter(
    prefix="/bass-guitars",
    tags=["Bass Guitars"],
    responses={404: {"description" : "Not found"}}
)

@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"id": item_id, "q": q}