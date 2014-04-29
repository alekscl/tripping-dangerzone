#!/usr/bin/env python
import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    # create the table
    c.execute(
        """
        create table if not exists ftasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        due_date TEXT NOT NULL,
        priority INTEGER NOT NULL,
        status INTEGER NOT NULL
        );
        """
    )

    # insert dummy data into the table
    data = [
        ("Finish this tutorial", "02/03/2014", 10, 1),
        ("Finish Real Python Course 2", "02/03/2014", 10, 1)
    ]

    c.executemany(
        """
        insert into ftasks (name, due_date, priority, status)
        values (?, ?, ?, ?);
        """,
        data
    )
