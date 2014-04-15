#!/usr/bin/env python
import sqlite3


def main():
    with sqlite3.connect("new.db") as connection:
        cursor = connection.cursor()

        for row in cursor.execute("select * from population;"):
            print row


if __name__ == "__main__":
    main()
