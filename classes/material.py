class Matherial:
    def __init__(self, type: str = "Sklo", name: str = "BUD"):
        self.type = type
        self.name = name

    def __del__(self):
        pass

    def __str__(self):
        return f'Material Type: {self.type} and name: {self.name}\n'

    @property
    def type_and_name(self):
        return "{} {}".format(self.type, self.name)

    @type_and_name.setter
    def type_and_name(self, type_and_name):
        type, name = type_and_name.split(' ')
        self.type = type
        self.name = name
