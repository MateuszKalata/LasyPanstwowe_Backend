import sqlalchemy.exc

from Data.SensorRepository.ISensorRepository import ISensorRepository
from Data.SensorRepository.SensorMapper import SensorMapper
from Entities.SensorEntity import SensorEntity
from Utils.DBhelper import Session


class SensorRepositoryImpl(ISensorRepository):

    def __init__(self):
        self.sensorMapper = SensorMapper()

    def create(self, xSensor):
        # test do sprawdzenia czy taki rodzaj czujnika jest akceptowalny
        session = Session()
        sensorEntity = self.sensorMapper.convertXSensorToSensorEntity(xSensor)
        session.add(sensorEntity)
        session.commit()
        sensor_entity_id = sensorEntity.id
        session.close()
        return sensor_entity_id

    def read(self, id):
        session = Session()
        try:
            sensorEntity = session.query(SensorEntity).filter(SensorEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensor = self.sensorMapper.convertSensorEntityToXSensor(sensorEntity)
        return xSensor

    def readByForestry(self, id):
        session = Session()
        try:
            sensorsEntity = session.query(SensorEntity).filter(SensorEntity.forestAreaId == id).all()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensors = []
        for entity in sensorsEntity:
            xSensors.append(self.sensorMapper.convertSensorEntityToXSensor(entity))
        return xSensors

    def readNotAssigned(self):
        session = Session()
        try:
            sensorsEntities = session.query(SensorEntity).filter(SensorEntity.forestAreaId == None).all()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensors = []
        for sensorEntity in sensorsEntities:
            xSensors.append(self.sensorMapper.convertSensorEntityToXSensor(sensorEntity))
        return xSensors

    def readAll(self):
        session = Session()
        sensorsEntities = session.query(SensorEntity).all()
        session.close()
        xSensors = map(self.sensorMapper.convertSensorEntityToXSensor, sensorsEntities)
        return xSensors

    # przetestowa?? czy dzia??a bo sam to zrobi??em
    # nie dzia??a, ale narazie jest niepotrzebne
    def update(self, sensorEntity):
        session = Session()
        session.query(SensorEntity).filter(SensorEntity.id == sensorEntity.id).update({
            "administrator": self.administrator,
            "dateAdded": self.dateAdded,
            "forestAreaId": self.forestAreaId,
            "name": self.name,
            "status": self.status,
            "type": self.type,
            "unit": self.unit
        })
        # je??li dzia??a zbyt wolno to mo??na sp??bowa?? przekaza?? do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0

    def AssignSensor(self, id, forestAreaId):
        session = Session()
        session.query(SensorEntity).filter(SensorEntity.id == id).update({"forestAreaId": forestAreaId})
        # je??li dzia??a zbyt wolno to mo??na sp??bowa?? przekaza?? do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0

    def ActivateSensor(self, id):
        session = Session()
        session.query(SensorEntity).filter(SensorEntity.id == id).update({"status": 'active'})
        # je??li dzia??a zbyt wolno to mo??na sp??bowa?? przekaza?? do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0

    def notExist(self, name):
        session = Session()
        exist = session.query(SensorEntity).filter(SensorEntity.name == name).count() == 0
        session.close()
        return exist
