from flask import request, g, Blueprint, json, Response
from ..models.LokacijaModel import LokacijaModel, LokacijeSchema

lokacije_api = Blueprint('lokacije_api', __name__)
lokacije_schema = LokacijeSchema()

@lokacije_api.route('/', methods=['GET'])
def get_all():

  lokacije = LokacijaModel.get_all_lokacije()
  data = lokacije_schema.dump(lokacije, many=True)
  return custom_response(data, 200)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

