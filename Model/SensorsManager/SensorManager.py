from Model.SensorsManager.ISensors import ISensors
from Model.SensorsManager.ISensorsRegistration import ISensorsRegistration
from Data.SensorRepository.SensorRepositoryImpl import SensorRepositoryImpl


class SensorManager(ISensors,ISensorsRegistration):

    allowedTypes = ["fire","humidity","rain","wind","temperature","camera","camera_trap"]
    allowedUnits = ["","%","K","°C","°F","C","F","bool","m/s","km/h","mm"]

    def __init__(self):
        self.sensorRepository = SensorRepositoryImpl()

    def AssignSensor(self, id, forestAreaId):
        return self.sensorRepository.AssignSensor(id,forestAreaId)

    def GetSensor(self, id):
        return self.sensorRepository.read(id)

    def GetSensorsByForestry(self, forestryId):
        return self.sensorRepository.readByForestry(forestryId)

    def GetSensorsNotAssigned(self):
        return self.sensorRepository.readNotAssigned()

    def RegisterSensor(self, sensor):
        if (sensor.type not in self.allowedTypes):
            return -1
        if (sensor.unit not in self.allowedUnits):
            return -2
        return self.sensorRepository.create(sensor)

    def ActivateSensor(self, id):
        return self.sensorRepository.ActivateSensor(id)
