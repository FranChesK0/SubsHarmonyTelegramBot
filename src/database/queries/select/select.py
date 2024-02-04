from sqlalchemy import Select, select

from database import models, schemas
from database.queries.queries import _to_dto, _select


async def all_users() -> list[schemas.UserDTO]:
    query: Select = select(models.UserORM)
    return _to_dto(await _select(query), schemas.UserDTO)


async def all_subscriptions() -> list[schemas.SubscriptionDTO]:
    query: Select = select(models.SubscriptionORM)
    return _to_dto(await _select(query), schemas.SubscriptionDTO)


async def all_user_subscriptions() -> list[schemas.UserSubscriptionDTO]:
    query: Select = select(models.UserSubscriptionORM)
    return _to_dto(await _select(query), schemas.UserSubscriptionDTO)
