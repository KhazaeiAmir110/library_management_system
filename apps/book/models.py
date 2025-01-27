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


class AuthorManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS author (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            biography TEXT NOT NULL
        );
    """


class BookManager(ORMMixin, Database):
    _create_table_query = """
        CREATE TABLE IF NOT EXISTS book (
            id SERIAL PRIMARY KEY,
            name VARCHAR(250) NOT NULL,
            type CHAR(1) NOT NULL DEFAULT 'B',
            status CHAR(1) NOT NULL DEFAULT 'A',
            price FLOAT NOT NULL,
            description TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            city_id INTEGER NOT NULL,
            genre_id INTEGER NOT NULL,
            FOREIGN KEY (author_id) REFERENCES author (id) ON DELETE CASCADE,
            FOREIGN KEY (city_id) REFERENCES city (id) ON DELETE CASCADE,
            FOREIGN KEY (genre_id) REFERENCES genre (id) ON DELETE CASCADE
        );
    """


class City:
    objects = CityManager()


class Genre:
    objects = GenreManager()


class Author:
    objects = AuthorManager()


class Book:
    objects = BookManager()
