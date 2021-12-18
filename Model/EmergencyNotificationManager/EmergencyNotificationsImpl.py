from Data.EmergencyNotificationRepository.EmergencyNotificationRepositoryImpl import EmergencyNotificationRepositoryImpl
from Data.SensorRepository.SensorRepositoryImpl import SensorRepositoryImpl
from Model.EmergencyNotificationManager.IEmergencyNotification import IEmergencyNotification
from Model.EmergencyNotificationManager.IEmergencyReporting import IEmergencyReporting
from Utils.APIException import APIException


class EmergencyNotificationImpl(IEmergencyNotification, IEmergencyReporting):

    def __init__(self):
        self.emergency_notification_repository = EmergencyNotificationRepositoryImpl()
        self.sensor_repository = SensorRepositoryImpl()

    def get_emergency_notification(self, id):
        return self.emergency_notification_repository.read(id)

    def get_emergency_notifications(self):
        return self.emergency_notification_repository.read_all()

    def mark_emergency_as_resolved(self, id):
        self.emergency_notification_repository.update(id, {"status": 0})

    def report_emergency(self, x_emergency_notification_details):
        if self.sensor_repository.read(x_emergency_notification_details.sensor_id) == 1:
            raise APIException(f"Sensor with id={x_emergency_notification_details.sensor_id} doesn't exist!", 422)
        return self.emergency_notification_repository.create(x_emergency_notification_details)
