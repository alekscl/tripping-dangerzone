#!/usr/bin/env python
import sqlite3


def main():

    orders = [
        ('Ford', 'Mustang', '2013-02-01'),
        ('Ford', 'Mustang', '2013-03-02'),
        ('Ford', 'Mustang', '2013-04-03'),
        ('Ford', 'Fiesta', '2013-05-04'),
        ('Ford', 'Fiesta', '2013-06-05'),
        ('Ford', 'Fiesta', '2013-07-06'),
        ('Ford', 'Focus', '2013-08-07'),
        ('Ford', 'Focus', '2013-09-08'),
        ('Ford', 'Focus', '2013-10-09'),
        ('Honda', 'Accord', '2013-11-10'),
        ('Honda', 'Accord', '2013-12-11'),
        ('Honda', 'Accord', '2014-01-12'),
        ('Honda', 'Civic', '2014-02-13'),
        ('Honda', 'Civic', '2014-03-14'),
        ('Honda', 'Civic', '2014-04-15')
    ]

    with sqlite3.connect("cars.db") as connection:
        c = connection.cursor()

        try:
            c.execute(
                """
                create table  orders
                (make TEXT, model TEXT, order_date TEXT);
                """
            )

            c.executemany(
                """
                insert into
                orders (make, model, order_date)
                values (?, ?, ?);
                """,
                orders
            )

        except sqlite3.OperationalError, e:
            print e


if __name__ == "__main__":
    main()
