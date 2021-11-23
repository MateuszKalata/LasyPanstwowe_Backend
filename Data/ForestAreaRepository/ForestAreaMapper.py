from DTO.XForestArea import XForestArea
from Entities.ForestAreaEntity import ForestAreaEntity


class ForestAreaMapper:

    def convert_forest_area_entity_to_xforestarea(self, forest_area_entity):
        return XForestArea(
            forest_area_entity.id,
            forest_area_entity.forestry_id,
            forest_area_entity.name,
            forest_area_entity.surface,
            []
        )

    def convert_xforestarea_to_forest_area_entity(self, xforestarea):
        return ForestAreaEntity(
            xforestarea.id,
            xforestarea.forestry_id,
            xforestarea.name,
            xforestarea.surface
        )
