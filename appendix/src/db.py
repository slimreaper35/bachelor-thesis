from dataclasses import dataclass, field
from typing import TypeAlias

import psycopg2

Connection: TypeAlias = psycopg2.extensions.connection
Cursor: TypeAlias = psycopg2.extensions.cursor


@dataclass
class DatabaseConfig:
    """Configuration for database connection."""

    dbname: str
    user: str
    host: str
    port: int


@dataclass
class NewDatabaseCursor:
    """Context manager for database cursor."""

    config: DatabaseConfig

    conn: Connection = field(init=False)
    cur: Cursor = field(init=False)

    def __enter__(self) -> Cursor:
        """Connect to database and create cursor."""
        self.conn = psycopg2.connect(
            dbname=self.config.dbname,
            user=self.config.user,
            host=self.config.host,
            port=self.config.port,
        )
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:  # noqa: ANN001
        """Close connection and cursor."""
        self.cur.close()
        self.conn.close()
