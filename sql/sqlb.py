#!/usr/bin/env python
import sqlite3


def main():
    conn = sqlite3.connect("new.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        insert into population (city, state, population)
        values ('New York', 'NY', 8200000);
        """
    )
    cursor.execute(
        """
        insert into population (city, state, population)
        values ('San Francisco', 'CA', 800000);
        """
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
