from flask import Blueprint, request
from flask import jsonify

from DTO.XForestAction import XForestAction
from Model.ForestActionManager.ForestActionImpl import ForestActionImpl
from Data.ForestAreaRepository.ForestAreaRepositoryImpl import ForestAreaRepositoryImpl
from Utils.APIException import APIException

forest_action_controller = Blueprint('ForestActionRESTController', __name__)
forest_actions = ForestActionImpl()
forest_areas = ForestAreaRepositoryImpl()


@forest_action_controller.route("/forestaction", methods=['POST'])
def post_forest_action():
    xforestaction = XForestAction(
        request.json.get('type'),
        request.json.get('forest_area_id'),
        request.json.get('start_date'),
        request.json.get('end_date'),
        None,
        request.json.get('team_leader'),
        request.json.get('team_size'),
        request.json.get('additional_info'),
        None,
        request.json.get('number_of_trees_to_proceed'),
        request.json.get('special_condition'),
        'active',
        request.json.get('tree_type')
    )

    if request.json.get('type') == 'deforestation':
        xforestarea = forest_areas.read(request.json.get('forest_area_id'))
        for forestation_type in xforestarea.forestation_types:
            if str(forestation_type.get('name')) == xforestaction.tree_type:
                if int(forestation_type.get('surface')) < xforestaction.number_of_trees_to_proceed:
                    raise APIException(f"number_of_trees_to_proceed can't be greater than number of trees!", 422)
                else:
                    id = forest_actions.create_forest_action(xforestaction)
                    return {"id": str(id)}, 200
        raise APIException(f"Can't find matching type of tree", 422)
    else:
        id = forest_actions.create_forest_action(xforestaction)
        return {"id": str(id)}, 200


@forest_action_controller.route("/forestactions", methods=['GET'])
def send_forest_actions():
    xforestactions = forest_actions.get_forest_actions()
    xforestactions = [xforestaction.as_dict() for xforestaction in xforestactions]
    return jsonify(xforestactions), 200

@forest_action_controller.route("/forestaction/<id>", methods=['GET'])
def send_forest_action(id):
    xforestaction = forest_actions.get_forest_action(id)
    return jsonify(xforestaction.as_dict()), 200

@forest_action_controller.route("/forestaction/<id>/finish", methods=['PATCH'])
def update_forest_action(id):
    # xforestaction = forest_actions.get_forest_action(id)
    status = forest_actions.update_forest_action(id)
    return str(status), 200
