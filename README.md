# flask-db-init
Simple flask app for initializing sqlalchemy db models.

## Instructions:
1. ```git clone [this repo]```
2. ```pip install -e .```
3. ```pip install -r requirements.txt```

```python
import flask_init_db as help

# currently doesn't run SQL create database [database];
db = help.create_db(server, database)

class NewRecordType(db.Model): # class named after value to store
    __tablename__ = 'new_record_type_table' # SQL table name
    id = db.Column(db.String(255), primary_key=True) # required
    column_one = db.Column(db.String(50))
    column_two = db.Column(db.String(50))

db.drop_all() # if you'd like to drop every model-defined table
db.create_all() # to create all model-defined tables
```
