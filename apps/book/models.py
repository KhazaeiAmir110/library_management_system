from apps.core.database import Database
from apps.core.orm import ORMMixin


class CityManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS city (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            country VARCHAR(100) NOT NULL
        );
    """


class GenreManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS genre (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
    """


class BookManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS book (
            id SERIAL PRIMARY KEY,
            title VARCHAR(250) NOT NULL,
            units INTEGER NOT NULL DEFAULT 0,
            status CHAR(1) NOT NULL DEFAULT 'Available' CHECK (status IN ('Available', 'Reserved'))
            isbn TEXT UNIQUE,
            price FLOAT NOT NULL,
            description TEXT NOT NULL,
            genre_id INTEGER NOT NULL,
            FOREIGN KEY (genre_id) REFERENCES genre (id) ON DELETE CASCADE
        );
    """


class City:
    objects = CityManager()


class Genre:
    objects = GenreManager()


class Book:
    objects = BookManager()
