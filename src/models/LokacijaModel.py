from . import db
from marshmallow import fields, Schema

class LokacijaModel(db.Model): 

    # table & schema name  
    __tablename__ = 'rl_lokacija'
    __table_args__ = {"schema": "relok"}
    
    id = db.Column(db.Integer, primary_key=True)
    naziv = db.Column(db.String())
    adresa = db.Column(db.String())

    # class constructor
    def __init__(self, data):
        self.naziv = data.get('naziv')
        self.adresa = data.get('adresa')        

    def __repr__(self):
        return f"<Lokacija {self.naziv}>"


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_lokacije():
        return LokacijaModel.query.all()

    def __repr__(self):
        return '<id {}>' .format(self.id)

class LokacijeSchema(Schema):

    id = fields.Int(dump_only=True)
    naziv = fields.Str(required=True)
    adresa = fields.Str(required=True)


# # @app.route('/')
# def init():
# 	return {""}

# # @app.route('/lokacije', methods=['POST', 'GET'])
# def handle_lokacija_post_get():
#     if request.method == 'POST':
#         if request.is_json:
#             data = request.get_json()
#             new_lokacija = LokacijaModel(naziv=data['naziv'], adresa=data['adresa'])

#             db.session.add(new_lokacija)
#             db.session.commit()

#             return {"message": f"lokacija {new_lokacija.naziv} has been created successfully."}
#         else:
#             return {"error": "The request payload is not in JSON format"}

#     elif request.method == 'GET':
#         lokacije = LokacijaModel.query.all()
#         results = [
#             {
#                 "naziv": lokacija.naziv,
#                 "adresa": lokacija.adresa
#             } for lokacija in lokacije]

#         return {"count": len(results), "lokacije": results, "message": "success"}

# # @app.route('/lokacije/<lokacija_id>', methods=['GET', 'PUT', 'DELETE'])
# def handle_lokacije_getByID_put_delete(lokacija_id):
#     lokacija = LokacijaModel.query.get_or_404(lokacija_id)

#     if request.method == 'GET':
#         response = {
#             "naziv": lokacija.naziv,
#             "adresa": lokacija.adresa,
#         }
#         return {"message": "success", "lokacija": response}        

#     elif request.method == 'PUT':
#         data = request.get_json()
#         lokacija.naziv = data['naziv']
#         lokacija.adresa = data['adresa']

#         db.session.add(lokacija)
#         db.session.commit()
        
#         return {"message": f"lokacija {lokacija.naziv} successfully updated"}

#     elif request.method == 'DELETE':
#         db.session.delete(lokacija)
#         db.session.commit()
        
#         return {"message": f"Lokacija {lokacija.naziv} successfully deleted."}  