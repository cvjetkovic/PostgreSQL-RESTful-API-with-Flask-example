from flask import Flask, request
from flask_sqlalchemy import *
from .src.models import db
from .src.views.LokacijaView import lokacije_api as lokacija_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Manager1@192.168.67.245:5432/relok_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

app.register_blueprint(lokacija_blueprint, url_prefix='/api/lokacije')

if __name__ == '__main__':
    app.run(debug=True)
