from flask import Blueprint, request
from Model.ForestryManager.ForestriesImpl import ForestriesImpl
from DTO.XForestry import XForestry
from DTO.XForestArea import XForestArea
from flask import jsonify

forestries_controller = Blueprint('ForestriesRESTController', __name__)
forestries = ForestriesImpl()


@forestries_controller.route("/forestareas/<id>", methods=['GET'])
def get_forest_areas(id):
    xforestrareas = forestries.get_forest_areas(int(id))
    if xforestrareas == 1:
        return "not found", 404
    return jsonify([xforestarea.as_dict() for xforestarea in xforestrareas]), 200


@forestries_controller.route("/forestareas", methods=['POST'])
def post_forest_area():
    xforestarea = XForestArea(
        None,
        request.json.get('forestry_id'),
        request.json.get('name'),
        request.json.get('surface'),
        request.json.get('forestation_types')
    )
    xforestry = forestries.get_forestry(xforestarea.id)
    if xforestry == 1:
        return {"message", "forestry doesn't exist!"}, 422
    if sum([float(xfa.surface) for xfa in xforestry.xforestareas]) + float(xforestarea.surface) > float(xforestry.xforestry.surface):
        return {"message", "forest areas' total surface would exceed forestry area!"}, 422
    if len(xforestarea.name) < 1:
        return {"message", "forestryarea name is empty!"}, 422
    if not xforestarea.surface.isnumeric():
        return {"message", "forestryarea surface must be a number!"}, 422
    if float(xforestarea.surface) > 10000:
        return {"message", "forestryarea can't be larger than 10000!"}, 422
    id = forestries.create_forest_area(xforestarea)
    return {"id": str(id)}, 200


@forestries_controller.route("/forestries", methods=['POST'])
def post_forestry():
    xforestry = XForestry(
        None,
        request.json.get('name'),
        request.json.get('surface')
    )
    if len(xforestry.name) < 1:
        return {"message", "forestry name is empty!"}, 422
    if not xforestry.surface.isnumeric():
        return {"message", "forestry surface must be a number!"}, 422
    if float(xforestry.surface) > 10000:
        return {"message", "forestry can't be larger than 10000!"}, 422
    id = forestries.create_forestry(xforestry)
    return {"id": str(id)}, 200


@forestries_controller.route("/forestries", methods=['GET'])
def send_forestries():
    xforestries = forestries.get_forestries()
    xforestries = [xforestry.as_dict() for xforestry in xforestries]
    return jsonify(xforestries), 200


@forestries_controller.route("/forestry/<id>", methods=['GET'])
def send_forestry(id):
    xforestry = forestries.get_forestry(id)
    if xforestry == 1:
        return {"message", "forestry doesn't exist!"}, 422
    return jsonify(xforestry.as_dict()), 200


