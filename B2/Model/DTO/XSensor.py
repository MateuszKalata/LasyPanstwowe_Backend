class XSensor():
    def __init__(self,administrator,dateAdded, forestAreaId, id, name, status, type, unit):
        self.administrator = administrator
        self.dateAdded = dateAdded
        self.forestAreaId = forestAreaId
        self.id = id
        self.name = name
        self.status = status
        self.type = type
        self.unit = unit

    def as_dict(self):
        return{
            "administrator":self.administrator,
            "date_added":self.dateAdded,
            "forest_area_id":self.forestAreaId,
            "id":self.id,
            "name":self.name,
            "status":self.status,
            "type":self.type,
            "unit":self.unit
        }