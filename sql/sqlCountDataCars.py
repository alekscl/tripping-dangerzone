#!/usr/bin/env python
import sqlite3


def main():

    with sqlite3.connect("cars.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            select make,model,count(order_date)
            from orders group by make, model;
            """
        )
        rows = c.fetchall()

        for row in rows:
            print("%s %s: %s" % (row[0], row[1], row[2]))


if __name__ == "__main__":
    main()
