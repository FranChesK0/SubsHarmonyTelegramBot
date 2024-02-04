from sqlalchemy import Insert, insert

from database import models, schemas
from database.queries.queries import _execute_query


async def __insert(model: type[models.ORM], value: schemas.AddDTO) -> None:
    query: Insert = insert(model).values(**value.model_dump())
    await _execute_query(query)


async def user(value: schemas.UserAddDTO) -> None:
    await __insert(models.UserORM, value)


async def subscription(value: schemas.SubscriptionAddDTO) -> None:
    await __insert(models.SubscriptionORM, value)


async def user_subscription(value: schemas.UserSubscriptionAddDTO) -> None:
    await __insert(models.UserSubscriptionORM, value)
