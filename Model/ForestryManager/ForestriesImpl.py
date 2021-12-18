from DTO.XForestryDetails import XForestryDetails
from Data.ForestAreaRepository.ForestAreaRepositoryImpl import ForestAreaRepositoryImpl
from Data.ForestryRepository.ForestryRepositoryImpl import ForestryRepositoryImpl
from Model.ForestryManager.IForestAreas import IForestAreas
from Model.ForestryManager.IForestires import IForestries


class ForestriesImpl(IForestries, IForestAreas):

    def __init__(self):
        self.forestry_repository = ForestryRepositoryImpl()
        self.forest_area_repository = ForestAreaRepositoryImpl()

    def create_forest_area(self, forest_area):
        return self.forest_area_repository.create(forest_area)

    def create_forestry(self, forestry):
        return self.forestry_repository.create(forestry)

    def get_forest_areas(self, forestry_id):
        return list(filter(lambda x: x.forestry_id == forestry_id, self.forest_area_repository.read_all()))

    def get_forestry(self, id):
        xforestry = self.forestry_repository.read(id)
        xforestareas = self.get_forest_areas(xforestry.id)
        return XForestryDetails(xforestry, xforestareas)

    def get_forestries(self):
        return self.forestry_repository.read_all()
