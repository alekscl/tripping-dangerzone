#!/usr/bin/env python
import sqlite3


def main():
    data = [
        ("Good", "I'm good."),
        ("Well", "I'm well."),
        ("Excellent", "I'm excelent."),
        ("Okay", "I'm okay.")
    ]

    with sqlite3.connect("blog.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            create table if not exists posts
            (title TEXT, post TEXT);
            """
        )
        c.executemany(
            """
            insert into posts values(?, ?);
            """,
            data
        )


if __name__ == "__main__":
    main()
