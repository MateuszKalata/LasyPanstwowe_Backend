class XForestry:
    def __init__(self, id, name, surface):
        self.id = id
        self.name = name
        self.surface = surface

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surface": self.surface
        }
