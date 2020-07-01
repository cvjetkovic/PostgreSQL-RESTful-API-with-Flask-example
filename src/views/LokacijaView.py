from flask import request, g, Blueprint, json, Response
from ..models.LokacijaModel import LokacijaModel, LokacijeSchema
import json

lokacije_api = Blueprint('lokacije_api', __name__)
lokacije_schema = LokacijeSchema()

@lokacije_api.route('/', methods=['GET'])
def get_all():

  limit = request.args.get('limit')
  offset = request.args.get('offset')
  lokacije = LokacijaModel.get_all_lokacije_paginate(limit, offset)  
  data = lokacije_schema.dump(lokacije, many=True)
  return custom_response(data, 200)
  

@lokacije_api.route('/<int:lokacija_id>', methods=['GET'])
def get_one(lokacija_id):

  lokacija = LokacijaModel.get_one_lokacija(lokacija_id)
  if not lokacija:
    return custom_response({'error': 'post not found'}, 404)
  data = lokacije_schema.dump(lokacija) 
  return custom_response(data, 200)


@lokacije_api.route('/', methods=['POST'])
def create():
  
  req_data = request.get_json()
  # req_data['owner_id'] = g.user.get('id')
  data, error = lokacije_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  lokacija = LokacijaModel(data)
  lokacija.save()
  data = lokacije_schema.dump(post)
  return custom_response(data, 201)


@lokacije_api.route('/<int:lokacija_id>', methods=['PUT'])
# @Auth.auth_required
def update(lokacija_id):

  req_data = request.get_json()
  lokacija = LokacijaModel.get_one_lokacija(lokacija_id)
  if not lokacija:
    return custom_response({'error': 'post not found'}, 404)
  data = lokacije_schema.dump(lokacija)
  # if data.get('owner_id') != g.user.get('id'):
  #   return custom_response({'error': 'permission denied'}, 400)
  
  data, error = lokacije_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  lokacija.update(data)
  
  data = lokacije_schema.dump(lokacija)
  return custom_response(data, 200)


@lokacije_api.route('/<int:lokacija_id>', methods=['DELETE'])
def delete(lokacija_id):
      
  lokacija = LokacijaModel.get_one_lokacija(lokacija_id)
  if not lokacija:
    return custom_response({'error': 'post not found'}, 404)
  data = lokacije_schema.dump(lokacija)
  # if data.get('owner_id') != g.user.get('id'):
  #   return custom_response({'error': 'permission denied'}, 400)

  lokacija.delete()
  return custom_response({'message': 'deleted'}, 204)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

