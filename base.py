from fastapi import APIRouter

from fight import api_route as api_route_fight
from fight import route_fight
from sql_app import models
from sql_app.session import engine
from users import api_route as api_route_user
from users import route_users

# models.Base.metadata.create_all(bind=engine)

api_router = APIRouter()
api_router.include_router(route_fight.router, prefix="", tags=["fight"])
api_router.include_router(route_users.router, prefix="", tags=["users"])
api_router.include_router(api_route_fight.router, prefix="", tags=["api-fights"])
api_router.include_router(api_route_user.router, prefix="", tags=["api-users"])
