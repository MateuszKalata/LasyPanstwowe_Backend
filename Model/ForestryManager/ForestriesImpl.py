from Model.ForestryManager.IForestires import IForestries
from Model.ForestryManager.IForestAreas import IForestAreas
from Data.ForestryRepository.ForestryRepositoryImpl import ForestryRepositoryImpl
from Data.ForestAreaRepository.ForestAreaRepositoryImpl import ForestAreaRepositoryImpl
from DTO.XForestryDetails import XForestryDetails


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
        if xforestry == 1:
            return 1
        xforestareas = self.get_forest_areas(xforestry.id)
        return XForestryDetails(xforestry, xforestareas)

    def get_forestries(self):
        return self.forestry_repository.read_all()
