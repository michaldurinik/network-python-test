class cube:

    def __init__(self, cube=[[0]]*100):
        self.cube = cube
        for i in self.cube:
            for j in range(100):
                i.append(j)

    def __str__(self):
        string = ""
        for line in self.cube:
            for item in line:
                string += str(item)
                string += " "
            string += "\n"
        return string

    def get_cube(self):
        return self.cube


