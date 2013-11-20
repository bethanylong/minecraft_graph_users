#!/usr/bin/env python

import bottle
import psycopg2
import sys
from mc_db import *

# Change port as desired (standalone server)
listen_port = 59000

# Change path as desired
@bottle.route('/json/')
def json():

    try:
        conn = psycopg2.connect(host = db_host, user = db_user,
                                password = db_pass, database = db_name)

        stmt = conn.cursor()
        stmt.execute("SELECT date, number FROM clients WHERE date > now() - INTERVAL '7 days'")
        data = stmt.fetchall()
        stmt.close()
        conn.commit()
        conn.close()

        data = map(list, data)

        for item in data:
            # Return time in milliseconds, shifted from UTC to PST
            item[0] = int(item[0].strftime("%s")) * 1000 - 28800000

        json = {"label": "Clients Connected", "data": data}
        return json
    except psycopg2.Error, e:
        print("Error {}".format(e.args))
        sys.exit(5)

# WSGI
application = bottle.default_app()

# Standalone
if __name__ == "__main__":
    bottle.run(host="0.0.0.0", port=listen_port)
