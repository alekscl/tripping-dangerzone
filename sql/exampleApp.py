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


def main():

    createtable()

    while True:
        print(
            """
            1 => Print averege
            2 => Print maximum
            3 => Print minimum
            4 => Print summation
            5 => Exit
            """
        )
        x = raw_input("Select option: ")
        if x in ['1', '2', '3', '4', '5']:
            if x == '1':
                print("average")
            if x == '2':
                print('maximum')
            if x == '3':
                print('minimun')
            if x == '4':
                print('summation')
            if x == '5':
                break
        else:
            print("Wrong selection")

    destroytable()
    print("Done...")


if __name__ == "__main__":
    main()
