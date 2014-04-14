#!/usr/bin/env python
import sqlite3


def main():
    conn = sqlite3.connect("cars.db")
    cursor = conn.cursor()
    cursor.execute("""create table if not exists inventory (
        Make TEXT,
        Model TEXT,
        Quantity INTEGER
    )""")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
