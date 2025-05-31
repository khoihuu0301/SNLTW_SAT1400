class GiaoVien:
    def __init__(self, ID, ten):
        self.ID = ID
        self.ten = ten

    def to_dict(self):
        return {"ID": self.ID, "ten": self.ten}
