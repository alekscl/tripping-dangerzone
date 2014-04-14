#!/usr/bin/env python
import sqlite3


cities = [
    ('Boston', 'MA', 600000),
    ('Chicago', 'IL', 2700000),
    ('Houston', 'TX', 2100000),
    ('Phoenix', 'AZ', 1500000)
]


def main():

    with sqlite3.connect("new.db") as connection:
        cursor = connection.cursor()
        cursor.executemany(
            """
            insert into population (city, state, population)
            values(?, ?, ?)
            """
            , cities)


if __name__ == "__main__":
    main()
