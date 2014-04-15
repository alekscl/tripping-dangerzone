#!/usr/bin/env python
import sqlite3


def printRows(rows):
    for row in rows:
        print("%s\t%s\t%d" % (row[0], row[1], row[2]))


def main():

    with sqlite3.connect("new.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            update population set population = 9000000 where city = 'New York';
            """
        )
        c.execute("select city, state, population from population;")
        rows = c.fetchall()
        print("Print results after executing an update statement")
        printRows(rows)

        c.execute(
            """
            delete from population where city = "Boston";
            """
        )
        c.execute("select city, state, population from population;")
        rows = c.fetchall()
        print("Print result after executing a deleting statement")
        printRows(rows)

        c.execute(
            """
            insert into population (city, state, population)
            values ('Boston', 'MA', 600000);
            """
        )
        c.execute(
            """
            update population set population = 8200000 where city = 'New York';
            """
        )
        c.execute("select city, state, population from population;")
        rows = c.fetchall()
        print("Print result after doing a manual rollback")
        printRows(rows)


if __name__ == "__main__":
    main()
