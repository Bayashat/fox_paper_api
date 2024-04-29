from datetime import datetime, timezone
from typing import Annotated

from sqlalchemy import text
from sqlalchemy.orm import mapped_column

str_256 = Annotated[str, 256]

intpk = Annotated[int, mapped_column(primary_key=True)]

created_at = Annotated[
    datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))
]
updated_at = Annotated[
    datetime,
    mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.now(timezone.utc),
    ),
]
