import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from DTO.XEmergencyNotification import XEmergencyNotification
from Data.EmergencyNotificationRepository.IEmergencyNotificationRepository import IEmergencyNotificationRepository
from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity
from Data.EmergencyNotificationRepository.EmergenyNotificationMapper import EmergencyNotificationMapper
from conf import DATABASE_URL

class EmergencyNotificationImpl(IEmergencyNotificationRepository):

    def __init__(self):
        self.emergency_mapper = EmergencyNotificationMapper()
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind = self.engine)
        EmergencyNotificationEntity.metadata.create_all(bind=self.engine)

    def create(self, xemergency):
        session = self.Session()
        emergency_entity = self.emergency_mapper.convert_xemergency_notification_to_emergency_notification_entity(xemergency)
        session.add(emergency_entity)
        session.commit()
        emergency_id = emergency_entity.id
        session.close()
        return emergency_id

    def read(self,id):
        session = self.Session()
        try:
            emergency_entity = session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xemergency = self.emergency_mapper.convert_emergency_notification_entity_to_xemergency_notification(emergency_entity)
        return xemergency

    def read_all(self):
        session = self.Session()
        emergency_entities = session.query(EmergencyNotificationEntity).all()
        session.close()
        emergencies = map(self.emergency_mapper.convert_emergency_notification_entity_to_xemergency_notification, emergency_entities)
        return emergencies

    def update(self, xemergency):
        session = self.Session()
        session.query(EmergencyNotificationEntity).filter(EmergencyNotificationEntity.id == xemergency.id).update({
            "emergency_status" : self.emergency_status,
            "sensor_id" : self.sensor_id,
            "emergency_type" : self.emergency_type
        })
        session.commit()
        session.close()
        return 0