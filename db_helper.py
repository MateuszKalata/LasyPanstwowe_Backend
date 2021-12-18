from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Entities.EmergencyNotificationEntity import EmergencyNotificationEntity
from Entities.ForestAreaEntity import ForestAreaEntity
from Entities.ForestationTypeEntity import ForestationTypeEntity
from Entities.ForestryEntity import ForestryEntity
from Entities.SensorEntity import SensorEntity
from Entities.SensorMeasurementEntity import SensorMeasurementEntity
from conf import DATABASE_URL


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
SensorMeasurementEntity.metadata.create_all(bind=engine)
SensorEntity.metadata.create_all(bind=engine)
ForestAreaEntity.metadata.create_all(bind=engine)
ForestationTypeEntity.metadata.create_all(bind=engine)
ForestryEntity.metadata.create_all(bind=engine)
EmergencyNotificationEntity.metadata.create_all(bind=engine)
