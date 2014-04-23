#!/usr/bin/env pyhton
import sqlite3


def main():
    with sqlite3.connect("new.db") as connection:
        c = connection.cursor()

        sql = {
            'average': "select avg(population) from population;",
            'maximum': "select max(population) from population;",
            'minimum': "select min(population) from population;",
            'sum': "select sum(population) from population;",
            'count': "select count(city) from population;"
        }

        for keys, values in sql.iteritems():
            c.execute(values)
            result = c.fetchone()
            print("%s: %s" % (keys, result))


if __name__ == "__main__":
    main()
