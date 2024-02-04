from sqlalchemy import Update, update

from database import models, schemas
from database.queries.queries import _execute_query


async def user(value: schemas.UserDTO) -> None:
    query: Update = update(models.UserORM) \
        .filter(models.UserORM.id == value.id) \
        .values(**value.model_dump())
    await _execute_query(query)


async def subscription(value: schemas.SubscriptionDTO) -> None:
    query: Update = update(models.SubscriptionORM) \
        .filter(models.SubscriptionORM.id == value.id) \
        .values(**value.model_dump())
    await _execute_query(query)


async def user_subscription(value: schemas.UserSubscriptionDTO) -> None:
    query: Update = update(models.UserSubscriptionORM) \
        .filter(models.UserSubscriptionORM.user_id == value.user_id and
                models.UserSubscriptionORM.subscription_id == value.subscription_id) \
        .values(**value.model_dump())
    await _execute_query(query)
