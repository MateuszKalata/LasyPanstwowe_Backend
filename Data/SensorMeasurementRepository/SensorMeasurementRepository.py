import sqlalchemy.exc

from Data.SensorMeasurementRepository.ISensorMeasurementRepository import ISensorMeasurementRepository
from Data.SensorMeasurementRepository.SensorMeasurementMapper import SensorMeasurementMapper
from Entities.SensorMeasurementEntity import SensorMeasurementEntity
from Utils.DBhelper import Session


class SensorMeasurementRepository(ISensorMeasurementRepository):

    def __init__(self):
        self.sensor_measurement_mapper = SensorMeasurementMapper()

    def create(self, xsensormeasurement):
        session = Session()
        sensor_measurement_entity = self.sensor_measurement_mapper. \
            convert_xsensormeasurement_to_sensor_measurement_entity(xsensormeasurement)
        session.add(sensor_measurement_entity)
        session.commit()
        sensor_measurement_entity_id = sensor_measurement_entity.id
        session.close()
        return sensor_measurement_entity_id

    def read_all(self):
        session = Session()
        sensor_measurements = session.query(SensorMeasurementEntity).all()
        session.close()
        xsensormeasurements = map(
            self.sensor_measurement_mapper.convert_sensor_measurement_entity_to_xsensormeasurement, sensor_measurements)
        return xsensormeasurements

    def read_id(self, id):
        session = Session()
        try:
            sensor_measurements = session.query(SensorMeasurementEntity).filter(SensorMeasurementEntity.sensor_id == id)
        except sqlalchemy.exc.NoResultFound:
            return 1
        session.close()
        xsensormeasurements = map(
            self.sensor_measurement_mapper.convert_sensor_measurement_entity_to_xsensormeasurement, sensor_measurements)
        return xsensormeasurements
