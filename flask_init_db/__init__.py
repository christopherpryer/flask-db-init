from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib

def get_con_str(server, database):
    driver = '{SQL Server}'
    server = '{%s}' % server
    database = '{%s}' % database
    base_str = 'DRIVER={};SERVER={};DATABASE={};Trusted_Connection=yes'
    _str = urllib.parse.quote_plus(base_str.format(driver, server, database))
    return 'mssql+pyodbc:///?odbc_connect=%s' % _str

def create_db(server, database):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_con_str(server, database)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class CleanShipment(db.Model):
        __tablename__ = 'clean_shipments'
        id = db.Column(db.String(255), primary_key=True)
        route_id = db.Column(db.String(255))
        stop_id = db.Column(db.String(255))
        order_id = db.Column(db.String(255))
        load_id = db.Column(db.String(255))
        sku_id = db.Column(db.String(255))
        origin_id = db.Column(db.String(255))
        origin_city = db.Column(db.String(50))
        origin_state = db.Column(db.String(50))
        origin_zip = db.Column(db.String(10))
        origin_country = db.Column(db.String(50))
        dest_id = db.Column(db.String(255))
        dest_city = db.Column(db.String(50))
        dest_state = db.Column(db.String(50))
        dest_zip = db.Column(db.String(10))
        dest_country = db.Column(db.String(50))
        demand = db.Column(db.Float)
        demand_uom = db.Column(db.String(50))

    return db
