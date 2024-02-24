
CSV_FILE='inventory.csv'
DB_FILE='inventory.db'

# SQL Queries

SELECT_ALL="SELECT * FROM inventory"
INSERT_TO_DB="INSERT INTO inventory (item_name, cost, subtype, replacement_duration) VALUES (?, ?, ?, ?)"
CREATE_TABLE="CREATE TABLE IF NOT EXISTS inventory (item_name TEXT,cost REAL,subtype TEXT,replacement_duration INTEGER)"
REGEX_NAME="/^[a-z ,.'-]+$/i"
REGEX_NUMBER="/ \d+ / "

regex_map ={"itemName":REGEX_NAME,
      "subtype":REGEX_NAME,
      "cost":REGEX_NUMBER,
      "replacementDuration":REGEX_NUMBER}

