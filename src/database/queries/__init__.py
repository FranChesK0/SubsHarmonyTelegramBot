from .queries import create_tables
from . import insert
from . import update
from . import delete

__all__ = [
    "create_tables",
    "delete",
    "insert",
    "update"
]
