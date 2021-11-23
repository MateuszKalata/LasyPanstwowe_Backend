class XForestArea:
    def __init__(self, id, forestry_id, name, surface, forestation_types):
        self.id = id
        self.forestry_id = forestry_id
        self.name = name
        self.surface = surface
        self.forestation_types = forestation_types

    def as_dict(self):
        return {
            "id": self.id,
            "forestry_id": self.forestry_id,
            "name": self.name,
            "surface": self.surface,
            "forestation_types": self.forestation_types
        }
