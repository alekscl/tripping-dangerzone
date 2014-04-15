#!/usr/bin/env python
import sqlite3


def main():

    with sqlite3.connect("cars.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            update inventory set Model = 'Mustang' where Model = 'Ka';
            """
        )
        c.execute(
            """
            update inventory set Quantity = 100 where Model = 'Civic';
            """
        )
        c.execute(
            """
            select Make, Model, Quantity from inventory order by quantity;
            """
        )

        rows = c.fetchall()
        for row in rows:
            print("%s %s %d" % (row[0], row[1], row[2]))


if __name__ == "__main__":
    main()
