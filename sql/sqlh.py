#!/usr/bin/env python
import sqlite3


def main():

    cities = [
        ('New York City', 'Northeast'),
        ('San Francisco', 'West'),
        ('Chicago', 'Midwest'),
        ('Houston', 'South'),
        ('Phoenix', 'West'),
        ('Boston', 'Northeast'),
        ('Los Angeles', 'West'),
        ('Houston', 'South'),
        ('Philadelphia', 'Northeast'),
        ('San Antonio', 'South'),
        ('San Diego', 'West'),
        ('Dallas', 'South'),
        ('San Jose', 'West'),
        ('Jacksonville', 'South'),
        ('Indianapolis', 'Midwest'),
        ('Austin', 'South'),
        ('Detroit', 'Midwest')
    ]

    with sqlite3.connect("new.db") as connection:
        c = connection.cursor()

        c.execute(
            """
            create table if not exists
            regions
            (city TEXT, region TEXT);
            """
        )
        c.executemany(
            """
            insert into regions (city, region) values (?, ?);
            """,
            cities
        )
        c.execute(
            """
            select city, region from regions order by region ASC;
            """
        )
        rows = c.fetchall()

        for row in rows:
            print("%s %s" % (row[0], row[1]))


if __name__ == "__main__":
    main()
