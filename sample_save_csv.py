"""
Author : Moontasir Mahmood
Github : munmud
"""

import psycopg2
from age_csv import *

# set DB path and graph name
conn = psycopg2.connect(
    host="localhost",
    port="5430",
    dbname="postgresDB",
    user="postgresUser",
    password="postgresPW")

GRAPH_NAME = 'bitnine_global_inic'

save_csv(connection=conn,
         GRAPH_NAME=GRAPH_NAME)
