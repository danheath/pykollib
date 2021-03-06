# Stubs for tortoise.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Awaitable, Callable, Iterator, Optional

class QueryAsyncIterator:
    query: Any = ...
    sequence: Any = ...
    def __init__(self, query: Awaitable[Iterator], callback: Optional[Callable]=...) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...

def get_schema_sql(client: Any, safe: bool) -> str: ...
async def generate_schema_for_client(client: Any, safe: bool) -> None: ...
