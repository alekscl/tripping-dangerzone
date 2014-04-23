#!/usr/bin/env python
import sqlite3
import random


def createtable():
    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            create table if not exists random
            (rnd INTEGER)
            """
        )
        rndvct = []
        random.seed()
        for i in xrange(0, 101):
            rndvct.append(tuple([random.randrange(1, 1000)]))

        c.executemany(
            """
            insert into random (rnd) values (?);
            """
            , rndvct
        )


def destroytable():
    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            drop table if exists random
            """
        )


def executeSelect(key, value):
    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()
        c.execute(value)
        result = c.fetchone()
        print("%s: %s\n\n\n" % (key, result[0]))


def main():

    createtable()

    aggfunct = {
        "avg": "select avg(rnd) from random;",
        "max": "select max(rnd) from random;",
        "min": "select min(rnd) from random;",
        "sum": "select sum(rnd) from random;"
    }

    while True:

        print(
            """
            1 => Print average
            2 => Print maximum
            3 => Print minimum
            4 => Print summation
            5 => Exit
            """
        )

        x = raw_input("Select option: ")
        if x in ['1', '2', '3', '4', '5']:
            if x == '1':
                executeSelect("Average", aggfunct.get("avg"))
            if x == '2':
                executeSelect("Maximum", aggfunct.get("max"))
            if x == '3':
                executeSelect("Minimum", aggfunct.get("min"))
            if x == '4':
                executeSelect("Summation", aggfunct.get("sum"))
            if x == '5':
                break
        else:
            print("Wrong selection")

    destroytable()
    print("Done...")


if __name__ == "__main__":
    main()
