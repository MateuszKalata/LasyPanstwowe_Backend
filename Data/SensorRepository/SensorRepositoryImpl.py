import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.SensorRepository.ISensorRepository import ISensorRepository
from Entities.SensorEntity import SensorEntity
from Data.SensorRepository.SensorMapper import SensorMapper
from conf import DB_URI



class SensorRepositoryImpl(ISensorRepository):

    def __init__(self):
        self.sensorMapper = SensorMapper()
        self.engine = create_engine(DB_URI)
        self.Session = sessionmaker(bind=self.engine)
        SensorEntity.metadata.create_all(bind=self.engine)

    def create(self, xSensor):
        session = self.Session()
        sensorEntity = self.sensorMapper.convertXSensorToSensorEntity(xSensor)
        session.add(sensorEntity)
        session.commit()
        session.close()
        return 0

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
            sensorsEntity = session.query(SensorEntity).filter(SensorEntity.forest_area_id == id).all()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensors = self.sensorMapper.convertSensorEntityToXSensor(sensorsEntity)
        return xSensors
    
    #przyjąłem, że nie przypisane maja forestry id = 0
    def readNotAssigned(self):
        session = self.Session()
        try:
            sensorsEntity = session.query(SensorEntity).filter(SensorEntity.forest_area_id == 0).all()
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xSensors = self.sensorMapper.convertSensorEntityToXSensor(sensorsEntity)
        return xSensors

    def readAll(self):
        session = self.Session()
        sensorsEntities = session.query(SensorEntity).all()
        session.close()
        xSensors = map(self.sensorMapper.convertSensorEntityToXSensor, sensorsEntities)
        return xSensors

    #przetestować czy działa bo sam to zrobiłem
    def update(self,sensorEntity):
        session = self.Session()
        session.query(SensorEntity).filter(SensorEntity.id == sensorEntity.id).update({
            "administrator":self.administrator,
            "date_added":self.dateAdded,
            "forest_area_id":self.forestAreaId,
            "name":self.name,
            "status":self.status,
            "type":self.type,
            "unit":self.unit
        })
        # jeśli działa zbyt wolno to można spóbować przekazać do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0

   #przetestować czy działa bo sam to zrobiłem
    def AssignSensor(self,sensorId,forestAreaId):
        session = self.Session()
        session.query(SensorEntity).filter(SensorEntity.id == sensorId).update({"forest_area_id":forestAreaId})
        # jeśli działa zbyt wolno to można spóbować przekazać do update() synchronize_session=False    
        session.commit()
        session.close()
        return 0


    def notExist(self, name):
        session = self.Session()
        exist = session.query(SensorEntity).filter(SensorEntity.name == name).count() == 0
        session.close()
        return exist

    
