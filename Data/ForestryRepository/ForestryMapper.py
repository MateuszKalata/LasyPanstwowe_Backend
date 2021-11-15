from DTO.XForestry import XForestry
from Entities.ForestryEntity import ForestryEntity


class ForestryMapper:

    def convert_forestry_entity_to_xforestry(self, forestry_entity):
        return XForestry(
            forestry_entity.id,
            forestry_entity.name,
            forestry_entity.surface
        )

    def convert_xforestry_to_forestry_entity(self, xforestry):
        return ForestryEntity(
            xforestry.id,
            xforestry.name,
            xforestry.surface
        )
