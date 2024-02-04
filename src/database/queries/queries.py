from sqlalchemy import Delete, Insert, Select, Sequence, Update

from database.schemas import DTO
from core import get_logger, Logger
from database.database import Base, engine, session_factory

logger: Logger = get_logger()


async def create_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        logger.warning("Tables were dropped")
        await connection.run_sync(Base.metadata.create_all)
        logger.warning("Tables were created")


async def _execute_query(query: Insert | Update | Delete) -> None:
    logger.debug(__compile_query(query))
    async with session_factory() as session:
        await session.execute(query)
        await session.commit()


async def _select(query: Select) -> list[any] | Sequence[any]:
    logger.debug(__compile_query(query))
    async with session_factory() as session:
        return (await session.execute(query)).unique().scalars().all()


def _to_dto(values: list[any] | Sequence[any], dto: type[DTO]) -> list[DTO]:
    return [dto.model_validate(row, from_attributes=True) for row in values]


def __compile_query(query: Insert | Update | Delete | Select) -> str:
    return str(query.compile(compile_kwargs={"literal_binds": True}))
