import re
class shortestPath():
    # x = input("Enter a string")
    # print(int("".join(re.findall("\d", x))))

    dataSet = """
        Mysore to Mandya = 66
        Mysore to Chennapatna = 28
        Mysore to Nanjangud = 60
        Mysore to Bandipur = 34
        Mysore to Nagarhole = 34
        Mysore to Somnathpur = 3
        Mysore to Bylakuppe = 108
        Mandya to Chennapatna = 22
        Mandya to Nanjangud = 12
        Mandya to Bandipur = 91
        Mandya to Nagarhole = 121
        Mandya to Somnathpur = 111
        Mandya to Bylakuppe = 71
        Chennapatna to Nanjangud = 39
        Chennapatna to Bandipur = 113
        Chennapatna to Nagarhole = 130
        Chennapatna to Somnathpur = 35
        Chennapatna to Bylakuppe = 40
        Nanjangud to Bandipur = 63
        Nanjangud to Nagarhole = 21
        Nanjangud to Somnathpur = 57
        Nanjangud to Bylakuppe = 83
        Bandipur to Nagarhole = 9
        Bandipur to Somnathpur = 50
        Bandipur to Bylakuppe = 60
        Nagarhole to Somnathpur = 27
        Nagarhole to Bylakuppe = 81
        Somnathpur to Bylakuppe = 90
    """

    filteredDataSet = []

    def filterNewLine(self, workingDataSet):
        filtered = workingDataSet.split("\n")
        return filtered

    def filterWhiteSpace(self, workingDataSet):
        tempDataSet = []
        for i in workingDataSet:
            tempDataSet.append([t for t in i.split(" ") if t not in ["", "to", "="]])
        return tempDataSet

    def trimFilteredDataSet(self, workingDataSet):
        return [i for i in workingDataSet if i]

run = shortestPath()
filteredLines = run.filterNewLine(run.dataSet)
filteredSpaces = run.filterWhiteSpace(filteredLines)
run.filteredDataSet = run.trimFilteredDataSet(filteredSpaces)
print(run.filteredDataSet)