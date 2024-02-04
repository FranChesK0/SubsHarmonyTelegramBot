from sqlalchemy import Delete, delete

from database import models
from database.queries.queries import _execute_query


async def user(id_: str) -> None:
    query: Delete = delete(models.UserORM) \
        .filter(models.UserORM.id == id_)
    await _execute_query(query)


async def subscription(id_: int) -> None:
    query: Delete = delete(models.SubscriptionORM) \
        .filter(models.SubscriptionORM.id == id_)
    await _execute_query(query)


async def user_subscription(user_id: str, subscription_id: int) -> None:
    query: Delete = delete(models.UserSubscriptionORM) \
        .filter(models.UserSubscriptionORM.user_id == user_id and
                models.UserSubscriptionORM.subscription_id == subscription_id)
    await _execute_query(query)
