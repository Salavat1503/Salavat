class chair:
    def __init__(self, color, legs, material):
        self.color = color
        self.legs = legs
        self.material = material

    def __str__(self):
        return "Стул" + " " + "(" + self.color.__str__() + ", " + self.legs + ", " + self.material + ")"

    def __repr__(self):
        return "Стул" + " " + "(" + self.color.__str__() + ", " + self.legs + ", " + self.material + ")"

стул = chair("black", "glass", "5")
print([стул])