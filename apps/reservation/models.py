from apps.core.database import Database
from apps.core.orm import ORMMixin


class ReservationManager(ORMMixin, Database):
    primary_keys = ["id"]
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS reservation (
            id SERIAL PRIMARY KEY,
            customer_id INTEGER REFERENCES "customer"(id) ON DELETE CASCADE,
            book_id INTEGER REFERENCES book(id) ON DELETE CASCADE,
            reservation_start TIMESTAMP,
            reservation_end TIMESTAMP,
            pyment DECIMAL(10, 1)
        );
    """


class Reservation:
    objects = ReservationManager()
