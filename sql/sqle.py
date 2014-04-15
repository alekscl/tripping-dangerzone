#!/usr/bin/env python
import sqlite3


def main():

    with sqlite3.connect("new.db") as connection:

        cursor = connection.cursor()
        cursor.execute("select city, state from population")
        rows = cursor.fetchall()

        for row in rows:
            print("%s %s" % (row[0], row[1]))


if __name__ == "__main__":
    main()
