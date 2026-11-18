
import sqlite3
from pathlib import Path
from datetime import datetime
from contextlib import closing


# Database location
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "prompt_history.db"


def get_connection():
    """Create a database connection."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create or update the history table."""

    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS prompt_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    task TEXT NOT NULL,
                    user_input TEXT NOT NULL,
                    result TEXT NOT NULL,
                    category TEXT DEFAULT 'General',
                    tone TEXT DEFAULT 'Professional',
                    created_at TEXT NOT NULL
                )
            """)

            # Support databases created with the earlier version
            columns = [
                row["name"]
                for row in connection.execute(
                    "PRAGMA table_info(prompt_history)"
                ).fetchall()
            ]

            if "session_id" not in columns:
                connection.execute(
                    "ALTER TABLE prompt_history ADD COLUMN session_id TEXT"
                )


def add_history(
    task,
    user_input,
    result,
    session_id,
    category="General",
    tone="Professional"
):
    """Save an activity for the current browser session."""

    initialize_database()

    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                INSERT INTO prompt_history (
                    session_id,
                    task,
                    user_input,
                    result,
                    category,
                    tone,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                session_id,
                task,
                user_input,
                str(result),
                category,
                tone,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ))


def get_history(session_id, limit=100):
    """Retrieve only the current session's activities."""

    initialize_database()

    with closing(get_connection()) as connection:
        rows = connection.execute("""
            SELECT *
            FROM prompt_history
            WHERE session_id = ?
            ORDER BY id DESC
            LIMIT ?
        """, (session_id, limit)).fetchall()

        return [dict(row) for row in rows]


def delete_history(record_id, session_id):
    """Delete a record belonging to the current session only."""

    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                DELETE FROM prompt_history
                WHERE id = ? AND session_id = ?
            """, (record_id, session_id))


def clear_history(session_id):
    """Clear only the current session's history."""

    with closing(get_connection()) as connection:
        with connection:
            connection.execute("""
                DELETE FROM prompt_history
                WHERE session_id = ?
            """, (session_id,))
