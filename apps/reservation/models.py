from apps.core.database import Database
from apps.core.orm import ORMMixin


class ReservationManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS reservation (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "user"(id) ON DELETE CASCADE,
            book_id INTEGER REFERENCES book(id) ON DELETE CASCADE,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            pyment DECIMAL(10, 1)
        );
    """


class Reservation:
    objects = ReservationManager()
