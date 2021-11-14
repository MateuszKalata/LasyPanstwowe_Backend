from flask import Blueprint, request
from Model.ForestryManager.ForestriesImpl import ForestriesImpl
from DTO.XForestry import XForestry
from DTO.XForestryDetails import XForestryDetails
from DTO.XForestArea import XForestArea
import json

forestries_controller = Blueprint('ForestriesRESTController', __name__)
forestries = ForestriesImpl()


@forestries_controller.route("/forestareas/<id>", methods=['GET'])
def get_forest_areas(id):
    xforestrareas = forestries.get_forest_areas(int(id))
    if xforestrareas == 1:
        return "not found", 404
    return json.dumps([xforestarea.as_dict() for xforestarea in xforestrareas]), 200


@forestries_controller.route("/forestareas", methods=['POST'])
def post_forest_area():
    xforestarea = XForestArea(
        None,
        request.json.get('forestry_id'),
        request.json.get('name'),
        request.json.get('surface'),
        request.json.get('forestation_types')
    )
    status = forestries.create_forest_area(xforestarea)
    return str(status), 200


@forestries_controller.route("/forestries", methods=['POST'])
def post_forestry():
    xforestry = XForestry(
        None,
        request.json.get('name'),
        request.json.get('surface')
    )
    status = forestries.create_forestry(xforestry)
    return str(status), 200


@forestries_controller.route("/forestries", methods=['GET'])
def send_forestries():
    xforestries = forestries.get_forestries()
    xforestries = [xforestry.as_dict() for xforestry in xforestries]
    return json.dumps(xforestries), 200


@forestries_controller.route("/forestry/<id>", methods=['GET'])
def send_forestry(id):
    xforestry = forestries.get_forestry(id)
    if xforestry == 1:
        return "not found", 404
    return json.dumps(xforestry.as_dict()), 200
