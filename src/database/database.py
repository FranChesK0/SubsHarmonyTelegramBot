from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker

from core import settings

engine: AsyncEngine = create_async_engine(url=settings.db.url, echo=settings.debug)
session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(engine)


class Base(DeclarativeBase):
    _repr_columns_number: int = 1
    _repr_columns: tuple = tuple()

    def __repr__(self) -> str:
        columns: list[str] = []
        for ind, column in enumerate(self.__table__.columns.keys()):
            if column in self._repr_columns or ind < self._repr_columns_number:
                columns.append(f"{column}={getattr(self, column)}")
        return f"<{self.__class__.__name__} {', '.join(columns)}>"
    
    def __str__(self) -> str:
        return self.__repr__()
