import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from Data.EmergencyNotificationRepository.EmergencyNotificationMapper import EmergencyNotificationMapper
from Data.EmergencyNotificationRepository.IEmergencyNotificationRepository import IEmergencyNotificationRepository
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity
from Utils.APIException import APIException
from conf import DATABASE_URL


class EmergencyNotificationRepositoryImpl(IEmergencyNotificationRepository):

    def __init__(self):
        self.emergency_notification_mapper = EmergencyNotificationMapper()
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        EmergencyNotificationEntity.metadata.create_all(bind=self.engine)

    def create(self, x_emergency_notification):
        session = self.Session()
        try:
            new_id = session.query(func.max(EmergencyNotificationEntity.emergency_id)).one()[0] + 1
        except Exception:
            new_id = 1
        x_emergency_notification.emergency_id = new_id
        emergency_notification_entities = self.emergency_notification_mapper.dto_to_entity(x_emergency_notification)
        for x in emergency_notification_entities:
            session.add(x)
        session.commit()
        emergency_notification_entity_id = emergency_notification_entities[0].emergency_id
        session.close()
        return emergency_notification_entity_id

    def read(self, id):
        session = self.Session()
        try:
            emergency_notification_entities = \
                session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.emergency_id == id).all()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Emergency notification with id={id} doesn't exist", 422)
        session.close()
        x_emergency_notification = self.emergency_notification_mapper.entity_to_dto(emergency_notification_entities)
        return x_emergency_notification

    def read_all(self):
        session = self.Session()
        x_emergency_notifications = []
        for value in session.query(EmergencyNotificationEntity.emergency_id).distinct():
            x_emergency_notifications.append(self.read(value[0]))
        session.close()
        return x_emergency_notifications

    def update(self, id, data):
        session = self.Session()
        try:
            emergency_notification_entitity = \
                session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.emergency_id == id).all()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Emergency notification with id={id} doesn't exist", 422)
        for x in emergency_notification_entitity:
            x.emergency_status = 0
        session.commit()
        session.close()
