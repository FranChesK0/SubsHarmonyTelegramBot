from database import schemas


class UserRelDTO(schemas.UserDTO, schemas.base.BaseRelDTO):
    subscriptions: list[schemas.SubscriptionDTO]


class SubscriptionRelDTO(schemas.SubscriptionDTO, schemas.base.BaseRelDTO):
    users: list[schemas.UserDTO]


class UserSubscriptionRelDTO(schemas.UserSubscriptionDTO, schemas.base.BaseRelDTO):
    user: schemas.UserDTO
    subscription: schemas.SubscriptionDTO
