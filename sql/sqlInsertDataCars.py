#!/usr/bin/env python
import sqlite3


def main():

    cars = [
        ('Ford', 'Ka', 20),
        ('Ford', 'Fiesta', 34),
        ('Ford', 'Focus', 40),
        ('Honda', 'Accord', 15),
        ('Honda', 'Civic', 36)
    ]

    with sqlite3.connect("cars.db") as connection:
        c = connection.cursor()
        c.executemany(
            """
            insert into inventory (Make, Model, Quantity) values (?, ?, ?);
            """,
            cars
        )
        c.execute("select Make, Model, Quantity from inventory;")
        rows = c.fetchall()

        for row in rows:
            print("%s, %s, %d" % (row[0], row[1], row[2]))


if __name__ == "__main__":
    main()
