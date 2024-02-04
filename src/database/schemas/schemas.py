import decimal

from database import schemas


class UserDTO(schemas.UserAddDTO, schemas.base.BaseDTO):
    pass


class SubscriptionDTO(schemas.SubscriptionAddDTO, schemas.base.BaseDTO):
    id: int


class UserSubscriptionDTO(schemas.UserSubscriptionAddDTO, schemas.base.BaseDTO):
    debt: decimal.Decimal
