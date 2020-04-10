from ACO import ACO


def readFile(fileName):
    matrix = []
    with open(fileName, 'r') as file:
        n = int(file.readline())
        for i in range(n):
            line = file.readline()
            row = list(map(lambda x: float(x), line.split(',')))
            matrix.append(row)
    return matrix


def main():
    graph = readFile("data/hardE.txt")
    parameters = {}
    parameters["numberOfCities"] = len(graph)
    parameters["numberOfGenerations"] = 200
    parameters["numberOfAnts"] = int(len(graph) * 0.8)
    parameters["graph"] = graph
    parameters["degradation"] = 0.03
    parameters["pheromoneQuantity"] = 1
    parameters["beta"] = 2.5
    parameters["alpha"] = 2

    aco = ACO(parameters)
    aco.run()


main()
