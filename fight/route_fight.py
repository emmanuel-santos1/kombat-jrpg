from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from sql_app.crud import list_fights
from sql_app.crud import search_fight
from sql_app.session import get_db
from users.api_route import get_current_user_from_token


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    fights = list_fights(db=db)
    authorization: str = request.cookies.get("access_token", None)
    scheme, token = get_authorization_scheme_param(authorization)
    if not authorization or scheme.lower() != "bearer":
        user = None
        fights = []
    else:
        try:
            user = get_current_user_from_token(token, db)
        except HTTPException:
            user = None
            fights = []
    return templates.TemplateResponse(
        "general_pages/homepage.html",
        {"request": request, "fights": fights, "user": user, "msg": msg},
    )


@router.get("/search/")
def search(
    request: Request, db: Session = Depends(get_db), query: Optional[str] = None
):
    fights = search_fight(query, db=db)
    authorization: str = request.cookies.get("access_token", None)
    scheme, token = get_authorization_scheme_param(authorization)
    if not authorization or scheme.lower() != "bearer":
        user = None
        fights = []
    else:
        try:
            user = get_current_user_from_token(token, db)
        except HTTPException:
            user = None
            fights = []
    return templates.TemplateResponse(
        "general_pages/homepage.html",
        {"request": request, "user": user, "fights": fights},
    )
