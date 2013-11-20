#!/usr/bin/env python

import psycopg2
import subprocess
from mc_db import *

# Script that returns the number of connected clients
# Replace with actual path to script
script = "/home/longb4/wwumc_clients.sh"

c = subprocess.call([script])
conn = psycopg2.connect(host = db_host, user = db_user,
                        password = db_pass, database = db_name)

stmt = conn.cursor()
stmt.execute("INSERT INTO clients (number) VALUES (%s)", (c,))
stmt.close()
conn.commit()
conn.close()
