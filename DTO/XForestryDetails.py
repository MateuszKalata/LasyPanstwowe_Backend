class XForestryDetails:
    def __init__(self, xforestry, xforestareas):
        self.xforestry = xforestry
        self.xforestareas = xforestareas

    def as_dict(self):
        xforestry = self.xforestry.as_dict()
        xforestry["forest_areas"] = [xforestarea.as_dict() for xforestarea in self.xforestareas]
        return xforestry
