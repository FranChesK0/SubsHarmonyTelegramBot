from database import schemas


class UserRelDTO(schemas.UserDTO, schemas.base.RelDTO):
    subscriptions: list[schemas.SubscriptionDTO]


class SubscriptionRelDTO(schemas.SubscriptionDTO, schemas.base.RelDTO):
    users: list[schemas.UserDTO]


class UserSubscriptionRelDTO(schemas.UserSubscriptionDTO, schemas.base.RelDTO):
    user: schemas.UserDTO
    subscription: schemas.SubscriptionDTO
