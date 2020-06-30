from flask import Flask, request
from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Manager1@192.168.67.245:5432/relok_dev"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class LokacijaModel(db.Model):    
    __tablename__ = 'rl_lokacija'
    __table_args__ = {"schema": "relok"}
    
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String())
    adresa = db.Column(db.String())

    def __init__(self, first_name, last_name):
        self.naziv = naziv
        self.adresa = adresa        

    def __repr__(self):
        return f"<Lokacija {self.naziv}>"


@app.route('/')
def init():
	return {""}

@app.route('/lokacije', methods=['POST', 'GET'])
def handle_lokacija_post_get():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_lokacija = LokacijaModel(naziv=data['naziv'], adresa=data['adresa'])

            db.session.add(new_lokacija)
            db.session.commit()

            return {"message": f"lokacija {new_lokacija.naziv} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        lokacije = LokacijaModel.query.all()
        results = [
            {
                "naziv": lokacija.naziv,
                "adresa": lokacija.adresa
            } for lokacija in lokacije]

        return {"count": len(results), "lokacije": results, "message": "success"}

@app.route('/lokacije/<lokacija_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_lokacije_getByID_put_delete(lokacija_id):
    lokacija = LokacijaModel.query.get_or_404(lokacija_id)

    if request.method == 'GET':
        response = {
            "naziv": lokacija.naziv,
            "adresa": lokacija.adresa,
        }
        return {"message": "success", "lokacija": response}        

    elif request.method == 'PUT':
        data = request.get_json()
        lokacija.naziv = data['naziv']
        lokacija.adresa = data['adresa']

        db.session.add(lokacija)
        db.session.commit()
        
        return {"message": f"lokacija {lokacija.naziv} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(lokacija)
        db.session.commit()
        
        return {"message": f"Lokacija {lokacija.naziv} successfully deleted."}    

if __name__ == '__main__':
    app.run(debug=True)
