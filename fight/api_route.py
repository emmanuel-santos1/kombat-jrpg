from fastapi import APIRouter
from fastapi import Depends
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from fight.controller import ControllerFight
from sql_app.models import User
from sql_app.schemas import PlayerGame
from sql_app.session import get_db
from users.api_route import get_current_user_from_token

router = APIRouter()


@router.post("/fight")
async def fight(
    player1: PlayerGame,
    player2: PlayerGame,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
    limit_second=Depends(RateLimiter(times=1, seconds=1)),
    limit_min=Depends(RateLimiter(times=10, seconds=60)),
):
    controller = ControllerFight(player1, player2, db)
    controller.fight()
    return controller.story
