import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.SensorMeasurementRepository.SensorMeasurementMapper import SensorMeasurementMapper
from Data.SensorMeasurementRepository.ISensorMeasurementRepository import ISensorMeasurementRepository
from Entities.SensorMeasurementEntity import SensorMeasurementEntity
from conf import DATABASE_URL


class SensorMeasurementRepository(ISensorMeasurementRepository):

    def __init__(self):
        self.sensor_measurement_mapper = SensorMeasurementMapper()
        self.engine = create_engine(DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        SensorMeasurementEntity.metadata.create_all(bind=self.engine)

    def create(self, xsensormeasurement):
        session = self.Session()
        sensor_measurement_entity = self.sensor_measurement_mapper. \
            convert_xsensormeasurement_to_sensor_measurement_entity(xsensormeasurement)
        session.add(sensor_measurement_entity)
        session.commit()
        sensor_measurement_entity_id = sensor_measurement_entity.id
        return sensor_measurement_entity_id

    def read_all(self):
        session = self.Session()
        sensor_measurements = session.query(SensorMeasurementEntity).all()
        session.close()
        return sensor_measurements

    def read_id(self, id):
        session = self.Session()
        try:
            sensor_measurements = session.query(SensorMeasurementEntity).filter(SensorMeasurementRepository == id)
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        return sensor_measurements
