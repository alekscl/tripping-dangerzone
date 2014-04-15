#!/usr/bin/env python
import sqlite3


def main():

    with sqlite3.connect("new.db") as connection:
        c = connection.cursor()
        c.execute(
            """
            select distinct population.city, population.population,
            regions.region
            from population, regions
            where population.city = regions.city
            order by population.city ASC
            """
        )
        rows = c.fetchall()
        for row in rows:
            print("City: %s\nPopulation: %s\nRegion: %s\n" %
                  (row[0], row[1], row[2]))


if __name__ == "__main__":
    main()
