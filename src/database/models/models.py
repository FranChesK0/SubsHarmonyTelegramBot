import decimal
import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, ForeignKey, text

from database.database import Base


class UserORM(Base):
    __tablename__ = "user"
    _repr_columns_number = 2

    id: Mapped[str] = mapped_column(primary_key=True)
    notification_time: Mapped[datetime.time]

    subscriptions: Mapped[list["UserSubscriptionORM"]] = relationship(back_populates="user")


class SubscriptionORM(Base):
    __tablename__ = "subscription"
    __table_args__ = (
        CheckConstraint("total_cost > 0", name="subscription_total_cost_check"),
    )
    _repr_columns_number = 4

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    date: Mapped[datetime.date]
    total_cost: Mapped[decimal.Decimal]

    users: Mapped[list["UserSubscriptionORM"]] = relationship(back_populates="subscription")


class UserSubscriptionORM(Base):
    __tablename__ = "user_subscription"
    __table_args__ = (
        CheckConstraint("cost > 0", name="user_subscription_cost_check"),
        CheckConstraint("debt >= 0", name="user_subscription_debt_check"),
    )
    _repr_columns_number = 5

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), primary_key=True)
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscription.id", ondelete="CASCADE"),
                                                 primary_key=True)
    cost: Mapped[decimal.Decimal]
    send: Mapped[bool]
    debt: Mapped[decimal.Decimal] = mapped_column(server_default=text("0"))

    user: Mapped["UserORM"] = relationship(back_populates="subscriptions")
    subscription: Mapped["SubscriptionORM"] = relationship(back_populates="users")
