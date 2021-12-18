import sqlalchemy.exc

from Data.EmergencyNotificationRepository.EmergencyNotificationMapper import EmergencyNotificationMapper
from Data.EmergencyNotificationRepository.IEmergencyNotificationRepository import IEmergencyNotificationRepository
from Data.SensorMeasurementRepository.SensorMeasurementMapper import SensorMeasurementMapper
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity
from Utils.APIException import APIException
from db_helper import Session


class EmergencyNotificationRepositoryImpl(IEmergencyNotificationRepository):

    def __init__(self):
        self.emergency_notification_mapper = EmergencyNotificationMapper()
        self.sensor_measurement_mapper = SensorMeasurementMapper()

    def create(self, x_emergency_notification):
        session = Session()
        measurements = [
            self.sensor_measurement_mapper.convert_xsensormeasurement_to_sensor_measurement_entity(x_sensor_measurement)
            for x_sensor_measurement in x_emergency_notification.measurements
        ]
        if len(measurements) < 3:
            raise APIException(f"Emergency situation requires at least 3 measurements", 422)
        emergency_notification = self.emergency_notification_mapper.dto_to_entity(x_emergency_notification)
        emergency_notification.sensor_measurements = measurements
        session.add(emergency_notification)
        session.commit()
        emergency_notification_entity_id = emergency_notification.id
        session.close()
        return emergency_notification_entity_id

    def read(self, id):
        session = Session()
        try:
            emergency_notification = \
                session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Emergency notification with id={id} doesn't exist", 422)
        x_emergency_notification = self.emergency_notification_mapper.entity_to_dto(emergency_notification)
        session.close()
        return x_emergency_notification

    def read_all(self):
        session = Session()
        emergency_notifications = session.query(EmergencyNotificationEntity).all()
        x_emergency_notifications = [self.emergency_notification_mapper.entity_to_dto(x) for x in emergency_notifications]
        session.close()
        return x_emergency_notifications

    def update(self, id, data):
        session = Session()
        try:
            emergency_notification_entitity = \
                session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Emergency notification with id={id} doesn't exist", 422)
        emergency_notification_entitity.status = 0
        session.commit()
        session.close()
