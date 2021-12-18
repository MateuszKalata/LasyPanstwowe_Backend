from flask import Blueprint, request
from flask import jsonify

from DTO.XForestArea import XForestArea
from DTO.XForestry import XForestry
from Model.ForestryManager.ForestriesImpl import ForestriesImpl
from Utils.APIException import APIException

forestries_controller = Blueprint('ForestriesRESTController', __name__)
forestries = ForestriesImpl()


@forestries_controller.route("/forestareas/<id>", methods=['GET'])
def get_forest_areas(id):
    xforestrareas = forestries.get_forest_areas(int(id))
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
    xforestry = forestries.get_forestry(xforestarea.forestry_id)
    if sum([float(xfa.surface) for xfa in xforestry.xforestareas]) + float(xforestarea.surface) > float(
            xforestry.xforestry.surface):
        raise APIException(f"forest areas' total surface would exceed forestry area!", 422)
    if len(xforestarea.name) < 1:
        raise APIException(f"forestryarea name is empty!", 422)
    if not xforestarea.surface.isnumeric():
        raise APIException(f"forestryarea surface must be a number!", 422)
    if float(xforestarea.surface) > 10000:
        raise APIException(f"forestryarea can't be larger than 10000!", 422)
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
        raise APIException(f"forestry name is empty!", 422)
    if not xforestry.surface.isnumeric():
        raise APIException(f"forestry surface must be a number!", 422)
    if float(xforestry.surface) > 10000:
        raise APIException(f"forestry can't be larger than 10000!", 422)
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
    return jsonify(xforestry.as_dict()), 200
