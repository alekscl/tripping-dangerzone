#!/usr/bin/env python
import sqlite3


def main():

    conn = sqlite3.connect("new.db")

    cursor = conn.cursor()

    cursor.execute(
        """create table population (city TEXT, state TEXT, population INT);""")

    conn.close()


if __name__ == "__main__":
    main()
