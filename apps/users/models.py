from apps.core.database import Database
from apps.core.orm import ORMMixin


class UserManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            password TEXT NOT NULL,
            is_superuser BOOLEAN NOT NULL DEFAULT FALSE,
            is_active BOOLEAN NOT NULL DEFAULT FALSE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            is_active BOOLEAN NOT NULL,
            date_joined TIMESTAMP NOT NULL,
            username TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL UNIQUE,
            otp TEXT
        );
    """


class AuthorManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY REFERENCES "user" (id) ON DELETE CASCADE,
            name VARCHAR(100) NOT NULL,
            biography TEXT NOT NULL,
            book_id INTEGER,
            city_id INTEGER,
            goodreads TEXT NOT NULL UNIQUE CHECK (goodreads ~ '^https?://'),
            bank_account VARCHAR(50) NOT NULL UNIQUE,
            FOREIGN KEY (book_id) REFERENCES book (id) ON DELETE CASCADE,
            FOREIGN KEY (city_id) REFERENCES city (id) ON DELETE CASCADE
        );
    """


class CustomUserManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY REFERENCES "user" (id) ON DELETE CASCADE,
            subscription_model VARCHAR(10) NOT NULL DEFAULT 'Free' CHECK (subscription_model IN ('Free', 'Plus', 'Premium')),
            subscription_start TIMESTAMP,
            subscription_end TIMESTAMP,
            wallet_amount DECIMAL(10,2) NOT NULL DEFAULT 0.00
        );
    """


class User:
    objects = UserManager()


class Author:
    objects = AuthorManager()


class Customer:
    objects = CustomUserManager()
