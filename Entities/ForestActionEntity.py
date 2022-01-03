from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from conf import Base


class ForestActionEntity(Base):
    __tablename__ = 'forest_actions'

    id = Column(Integer, primary_key=True)

    additional_info = Column(String(200))
    end_date = Column(String(200))
    forest_area_id = Column(String(200))
    forest_type_id = Column(String(200))
    number_of_trees_to_proceed = Column(Integer)
    special_condition = Column(String(200))
    start_date = Column(String(200))
    status = Column(String(200))
    team_leader = Column(String(200))
    team_size = Column(Integer)
    type = Column(String(200))
    tree_type = Column(String(200))

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