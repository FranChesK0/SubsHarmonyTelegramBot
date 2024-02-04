import decimal
import datetime

from database.schemas.base import BaseAddDTO


class UserAddDTO(BaseAddDTO):
    id: str
    notification_time: datetime.time


class SubscriptionAddDTO(BaseAddDTO):
    name: str
    date: datetime.date
    total_cost: decimal.Decimal


class UserSubscriptionAddDTO(BaseAddDTO):
    user_id: str
    subscription_id: int
    cost: decimal.Decimal
    send: bool
