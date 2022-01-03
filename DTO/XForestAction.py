class XForestAction:
    def __init__(
            self, type, forest_area_id, start_date,
            end_date, forest_type_id, team_leader, 
            team_size, additional_info, id,
            number_of_trees_to_proceed, special_condition, status, tree_type
        ):
        self.additional_info = additional_info
        self.end_date = end_date
        self.forest_area_id = forest_area_id
        self.forest_type_id = forest_type_id
        self.id = id
        self.number_of_trees_to_proceed = number_of_trees_to_proceed
        self.special_condition = special_condition
        self.start_date = start_date
        self.status = status
        self.team_leader = team_leader
        self.team_size = team_size
        self.type = type
        self.tree_type = tree_type

    def as_dict(self):
        return {
           "additional_info" : self.additional_info,
           "end_date" : self.end_date,
           "forest_area_id" : self.forest_area_id,
           "id" : self.id,
           "number_of_trees_to_proceed" : self.number_of_trees_to_proceed,
           "special_condition" : self.special_condition,
           "start_date" : self.start_date,
           "status" : self.status,
           "team_leader" : self.team_leader,
           "team_size" : self.team_size,
           "type" : self.type,
           "tree_type" : self.tree_type
        }
