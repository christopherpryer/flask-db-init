from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import flask_init_db as help
import os

# TODO:
server = os.environ.get('SQL_SERVER')
database = os.environ.get('SQL_DATABASE')

def get_db():
    return help.create_db(server=server, database=database)

def reset_db():
    db = get_db()
    db.drop_all()

def test_create():
    db = get_db()

    assert isinstance(db, (SQLAlchemy,))

def test_simple_init():
    reset_db()

    db = get_db()
    db.create_all()

    con_str = help.get_con_str(server=server, database=database)
    engine = create_engine(con_str)
    clean_shipments = None

    try:
        sql_str = 'select * from clean_shipments'
        clean_shipments = pd.read_sql(sql_str, con=con_str)
    except:
        pass

    assert clean_shipments is not None

def test_advanced_init():
    reset_db()

    db = get_db()

    class RawShipment(db.Model):
        __tablename__ = 'raw_shipments'
        id = db.Column(db.String(255), primary_key=True)
        origin_city = db.Column(db.String(50))
        origin_state = db.Column(db.String(50))
        origin_zip = db.Column(db.String(10))
        dest_city = db.Column(db.String(50))
        dest_state = db.Column(db.String(50))
        dest_zip = db.Column(db.String(10))
        demand = db.Column(db.Float)
        demand_uom = db.Column(db.String(50))

    db.create_all()

    con_str = help.get_con_str(server=server, database=database)
    engine = create_engine(con_str)
    raw_shipments = None

    try:
        sql_str = 'select * from raw_shipments'
        raw_shipments = pd.read_sql(sql_str, con=con_str)
    except:
        pass

    assert raw_shipments is not None


# pytest is giving me issues
if __name__ == '__main__':
    test_create()
    test_simple_init()
    test_advanced_init()
