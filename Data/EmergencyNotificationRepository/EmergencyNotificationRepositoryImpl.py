import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
        emergency_notification_entity = self.emergency_notification_mapper.dto_to_entity(x_emergency_notification)
        session.add(emergency_notification_entity)
        session.commit()
        emergency_notification_entity_id = emergency_notification_entity.emergency_id
        session.close()
        return emergency_notification_entity_id

    def read(self, id):
        session = self.Session()
        try:
            emergency_notification_entitity = \
                session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.emergency_id == id).one()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Emergency notification with id={id} doesn't exist", 422)
        session.close()
        x_emergency_notification = self.emergency_notification_mapper.entity_to_dto(emergency_notification_entitity)
        return x_emergency_notification

    def read_all(self):
        session = self.Session()
        emergency_notification_entities = session.query(EmergencyNotificationEntity).all()
        session.close()
        x_emergency_notifications = \
            map(self.emergency_notification_mapper.entity_to_dto, emergency_notification_entities)
        return x_emergency_notifications

    def update(self, id, data):
        session = self.Session()
        try:
            emergency_notification_entitity = \
                session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.emergency_id == id).one()
        except sqlalchemy.exc.NoResultFound:
            raise APIException(f"Emergency notification with id={id} doesn't exist", 422)
        emergency_notification_entitity.emergency_status = 0
        session.commit()
        session.close()
