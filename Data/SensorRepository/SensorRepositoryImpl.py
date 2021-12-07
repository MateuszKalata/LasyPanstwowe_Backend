import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DTO.XSensor import XSensor
from Data.SensorRepository.ISensorRepository import ISensorRepository
from Entities.SensorEntity import SensorEntity
from Data.SensorRepository.SensorMapper import SensorMapper
from conf import DATABASE_URL


class SensorRepositoryImpl(ISensorRepository):

    allowedTypes = ["fire","humidity","rain","wind","temperature","camera","camera_trap"]
    allowedUnits = ["","%","K","°C","°F","C","F","bool","m/s","km/h","mm"]
    def __init__(self):
        self.sensorMapper = SensorMapper()
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        SensorEntity.metadata.create_all(bind=self.engine)

    def create(self, xSensor):
        #test do sprawdzenia czy taki rodzaj czujnika jest akceptowalny
        if (xSensor.type not in self.allowedTypes):
            return -1
        if (xSensor.unit not in self.allowedUnits):
            return -2

        session = self.Session()       
        sensorEntity = self.sensorMapper.convertXSensorToSensorEntity(xSensor)
        session.add(sensorEntity)
        session.commit()
        sensor_entity_id = sensorEntity.id
        session.close()
        return sensor_entity_id

    def read(self, id):
        session = self.Session()
        try:
            sensorEntity = session.query(SensorEntity).filter(SensorEntity.id == id).one()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensor = self.sensorMapper.convertSensorEntityToXSensor(sensorEntity)
        return xSensor

    def readByForestry(self, id):
        session = self.Session()
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
        session = self.Session()
        try:
            sensorsEntities = session.query(SensorEntity).filter(SensorEntity.forestAreaId == "").all()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensors = []
        for sensorEntity in sensorsEntities:
            xSensors.append(self.sensorMapper.convertSensorEntityToXSensor(sensorEntity))
        return xSensors

    def readAll(self):
        session = self.Session()
        sensorsEntities = session.query(SensorEntity).all()
        session.close()
        xSensors = map(self.sensorMapper.convertSensorEntityToXSensor, sensorsEntities)
        return xSensors

    #przetestować czy działa bo sam to zrobiłem
    #nie działa, ale narazie jest niepotrzebne
    def update(self,sensorEntity):
        session = self.Session()
        session.query(SensorEntity).filter(SensorEntity.id == sensorEntity.id).update({
            "administrator":self.administrator,
            "dateAdded":self.dateAdded,
            "forestAreaId":self.forestAreaId,
            "name":self.name,
            "status":self.status,
            "type":self.type,
            "unit":self.unit
        })
        # jeśli działa zbyt wolno to można spóbować przekazać do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0

    def AssignSensor(self,id,forestAreaId):
        session = self.Session()
        session.query(SensorEntity).filter(SensorEntity.id == id).update({"forestAreaId":forestAreaId})
        # jeśli działa zbyt wolno to można spóbować przekazać do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0

    def ActivateSensor(self,id):
        session = self.Session()
        session.query(SensorEntity).filter(SensorEntity.id == id).update({"status":'active'})
        # jeśli działa zbyt wolno to można spóbować przekazać do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0


    def notExist(self, name):
        session = self.Session()
        exist = session.query(SensorEntity).filter(SensorEntity.name == name).count() == 0
        session.close()
        return exist

    
