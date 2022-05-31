class Table:

    def __init__(self, color: str, height: float, area: float):
        """Constructor of a table object"""
        self.color = color
        self.height = height
        self.area = area
        self.isSet = False
        self.numberOfSettings = None

    def setTable(self, numOfSettings: int):
        """Sets the table with the specified settings"""
        self.isSet = True
        self.numberOfSettings = numOfSettings


tables = {}
brownTable = Table("brown", 2, 6)
tables[brownTable.color] = brownTable
whiteTable = Table("white", 2, 6)
tables[whiteTable.color] = whiteTable

print(tables)
for table in tables:
    print(table)
    print(type(table))

for table in tables.keys():
    print(table)
    print(type(table))

for table in tables.values():
    table.setTable(3)
    print(table)
    print(type(table))
