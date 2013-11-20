minecraft_graph_users
=====================

Plot the number of connected Minecraft users using Flot, JSON, Bottle, and Postgres.

Most of the scripts here will need to be manually modified for your setup.

Python
------

Python dependencies are `bottle` and `psycopg2`.

Database
--------

The table is called "clients".
The "number" column is where the numbers of clients are stored.
There should be a "date" column that defaults to now().

You will need to edit `mc_db.py` in `json` and `gather_stats` according to your setup.

A basic example of database setup is in `examples/postgres.markdown`. It is assumed that you have a working Postgres installation, but if you don't, [excellent documentation is available](http://www.postgresql.org/docs/manuals/).

JSON
----

`json/plot_mc_clients.py` formats graph points from the database into JSON. It can then use Bottle to run as a standalone HTTP server or as a WSGI script with another web server like `uwsgi` or Apache `mod_wsgi`.

In general, the standalone server is adequate for light usage, especially if it's behind a caching reverse proxy. An example of this setup is in `examples/nginx.markdown`.

Static frontend
---------------

The static frontend content in `frontend` revolves around the [Flot plotting library](http://www.flotcharts.org/).
