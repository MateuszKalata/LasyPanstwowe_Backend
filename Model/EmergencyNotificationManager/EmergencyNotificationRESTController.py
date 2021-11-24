from flask import Blueprint, request

from Model.EmergencyNotificationManager.EmergencyNotificationJSONMapper import EmergencyNotificationJSONMapper
from Model.EmergencyNotificationManager.EmergencyNotificationsImpl import EmergencyNotificationImpl
from flask import jsonify

from Utils.APIException import exception_catcher


emergency_notification_controller = Blueprint('EmergencyNotificationRESTController', __name__)
emergency_notifications = EmergencyNotificationImpl()
emergency_notification_json_mapper = EmergencyNotificationJSONMapper()


@emergency_notification_controller.route("/emergencynotifications/<id>", methods=['GET'])
@exception_catcher
def get_emergency_notification(id):
    emergency_notification = emergency_notifications.get_emergency_notification(int(id))
    json_data = emergency_notification_json_mapper.dto_to_json(emergency_notification)
    return jsonify(json_data), 200


@emergency_notification_controller.route("/emergencynotifications", methods=['GET'])
@exception_catcher
def get_emergency_notifications():
    emergency_notification = emergency_notifications.get_emergency_notifications()
    json_data = [emergency_notification_json_mapper.dto_to_json(x) for x in emergency_notification]
    return jsonify(json_data), 200


@emergency_notification_controller.route("/emergencynotifications/<id>/resolve", methods=['POST'])
@exception_catcher
def mark_emergency_as_resolved(id):
    emergency_notifications.mark_emergency_as_resolved(id)
    return jsonify({"message": "success"}), 200


@emergency_notification_controller.route("/emergencynotifications", methods=['POST'])
@exception_catcher
def report_emergency():
    x_emergency_notification = emergency_notification_json_mapper.json_to_dto(request.json)
    emergency_notifications.report_emergency(x_emergency_notification)
    return jsonify({"message": "success"}), 200

