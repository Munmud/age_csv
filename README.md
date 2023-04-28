# age_csv
There are two functions that have been developed for the purpose of converting data that is stored in the Apache AGE Graph database system into a format that can be represented in CSV (comma-separated values) format. CSV is a popular data interchange format that is commonly used for data analysis, and Apache AGE Graph database is a graph database system that is optimized for working with highly connected data. The two functions in this repository would allow someone to take data that is stored in Apache AGE Graph database and export it into a format that can be easily analyzed or imported into other software tools that can handle CSV data.

### Installation 
- Download the github repository 
```
git clone https://github.com/Munmud/age_csv
```
- Go to project directory
```
cd age_csv
```
- Install Dependency
```
pip install -r requirements.txt
```

### Save to csv
- Change the `conn` and `GRAPH_NAME` according to your age configuration
```py
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
```

### LOAD from csv
- Change the `conn` according to your age configuration
- Give `GRAPH_NAME` where you want to load
- Give `directory` where you have stored the csv file
- You must follow the naming rules for generating nodes and edges
- Vertices file name format : `label_name.csv`
- Edges file name format : `edge_label_name.csv`
- Example:
    - Creating nodes with label People : `People.csv`
    - Creating edges with label Purchase : `edge_Purchase.csv`
```py
import psycopg2
from age_csv import *
import os

# set DB path and graph name
conn = psycopg2.connect(
    host="localhost",
    port="5430",
    dbname="postgresDB",
    user="postgresUser",
    password="postgresPW")

GRAPH_NAME = 'bitnine_global_inic'

data = load_csv(connection=conn,
                GRAPH_NAME=GRAPH_NAME,
                # directory=os.path.join(os.path.dirname(__file__), 'data')
                directory="./bitnine_global_inic_data"
                )

```

### Sample Files
- [Load from csv](https://github.com/Munmud/age_csv/blob/main/sample_load_csv.py)
- [Save to csv](https://github.com/Munmud/age_csv/blob/main/sample_save_csv.py)

### Note
- If you want go use latest age driver download the  age folder[ from here ](https://github.com/apache/age/tree/master/drivers/python)