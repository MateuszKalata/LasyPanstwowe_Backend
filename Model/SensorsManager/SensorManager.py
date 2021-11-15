from Model.SensorsManager.ISensors import ISensors
from Model.SensorsManager.ISensorsRegistration import ISensorsRegistration
from Data.SensorRepository.SensorRepositoryImpl import SensorRepositoryImpl


class SensorManager(ISensors,ISensorsRegistration):

    def __init__(self):
        self.sensorRepository = SensorRepositoryImpl()

    def AssignSensor(self, sensorId, forestAreaId):
        return self.sensorRepository.AssignSensor(sensorId,forestAreaId)

    def GetSensor(self, id):
        return self.sensorRepository.read(id)

    def GetSensorsByForestry(self, forestryId):
        return self.sensorRepository.readByForestry(forestryId)

    def GetSensorsNotAssigned(self):
        return self.sensorRepository.readNotAssigned()

    def RegisterSensor(self, sensor):
        return self.sensorRepository.create(sensor)