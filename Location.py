class Location:
    def __init__(self, name=None, specialAttr=None, positions=None):
        if name is None:
            name = dict()
        if specialAttr is None:
            specialAttr = dict()
        if positions is None:
            positions = dict()
        self.names = name
        self.specialAttrs = specialAttr
        self.positions = positions
        self.maxKey = max(name, key=name.get)
        if len(specialAttr) != 0 and max(self.specialAttr, key=self.specialAttr.get) > self.maxKey:
            self.maxKey = max(self.specialAttr, key=self.specialAttr.get)
        if len(positions) != 0 and max(self.positions, key=self.positions.get) > self.maxKey:
            self.maxKey = max(self.positions, key=self.positions.get)

    def getMaxKey(self):
        return self.maxKey

    def getAllFromNumber(self, num):
        return self.names.get(num), self.specialAttrs.get(num), self.positions.get(num)

    def getNameFromNumber(self, num):
        return self.names.get(num)

    def getSpecialAttrFromNumber(self, num):
        return self.specialAttrs.get(num)

    def getPositionsFromNumber(self, num):
        return self.positions.get(num)



