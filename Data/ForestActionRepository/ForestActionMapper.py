from DTO.XForestAction import XForestAction
from Entities.ForestActionEntity import ForestActionEntity

class ForestActionMapper:

    def convert_ForestActionEntity_to_XForestAction(self, forest_action_entity):
        return XForestAction(
            forest_action_entity.type,
            forest_action_entity.forest_area_id,
            forest_action_entity.start_date,
            forest_action_entity.end_date,
            forest_action_entity.forest_type_id,
            forest_action_entity.team_leader,
            forest_action_entity.team_size,
            forest_action_entity.additional_info,
            forest_action_entity.id,
            forest_action_entity.number_of_trees_to_proceed,
            forest_action_entity.special_condition,
            forest_action_entity.status,
            forest_action_entity.tree_type
        )

    def convert_XForestAction_to_ForestActionEntity(self, xforestaction):
        return ForestActionEntity(
            xforestaction.type,
            xforestaction.forest_area_id,
            xforestaction.start_date,
            xforestaction.end_date,
            xforestaction.forest_type_id,
            xforestaction.team_leader,
            xforestaction.team_size,
            xforestaction.additional_info,
            xforestaction.id,
            xforestaction.number_of_trees_to_proceed,
            xforestaction.special_condition,
            xforestaction.status,
            xforestaction.tree_type
        )
