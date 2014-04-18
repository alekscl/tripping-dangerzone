#!/usr/bin/env python
import sqlite3


def main():

    with sqlite3.connect("cars.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            select inventory.Make, inventory.Model,
            inventory.Quantity, orders.order_date
            from inventory, orders
            where inventory.Make = orders.make
            and inventory.Model = orders.model
            order by orders.order_date ASC;
            """
        )
        rows = c.fetchall()

        for row in rows:
            print("%s, %s, %s, %s" % (row[0], row[1], row[2], row[3]))


if __name__ == "__main__":
    main()
