from ..sql_db import Cursor

def is_initialized(cr: Cursor) -> bool: ...
def initialize(cr: Cursor) -> None: ...
def create_categories(cr: Cursor, categories: list[str]) -> int | None: ...
def has_unaccent(cr: Cursor) -> bool: ...
