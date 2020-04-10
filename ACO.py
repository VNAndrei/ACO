from Ant import Ant
import random


class ACO:
    def __init__(self, parameters):
        self.__parameters = parameters
        self.__ants = []

    def __initialize(self):
        self.__parameters["eta"] = [[0 if i == j else 1 / self.__parameters["graph"][i][j]
                                     for j in range(self.__parameters["numberOfCities"])]
                                    for i in range(self.__parameters["numberOfCities"])]

        self.__parameters["pheromones"] = [[0
                                            for j in range(self.__parameters["numberOfCities"])]
                                           for i in range(self.__parameters["numberOfCities"])]

    def __initializeAnts(self):
        self.__ants = []
        for _ in range(self.__parameters['numberOfAnts']):
            self.__ants.append(Ant(self.__parameters))

    def __updatePheromoneGlobal(self, ant):
        for i in range(len(ant.path)):
            a = ant.path[i]
            if i == len(ant.path) - 1:
                b = ant.path[0]
            else:
                b = ant.path[i + 1]

            t1 = self.__parameters["pheromones"][a][b]
            self.__parameters["pheromones"][a][b] = self.__parameters["degradation"] * t1 + \
                                                    (1 - self.__parameters["degradation"]) / ant.cost

    def __updatePheromoneGlobal(self, ant):
        for i in range(len(ant.path)):
            a = ant.path[i]
            if i == len(ant.path) - 1:
                b = ant.path[0]
            else:
                b = ant.path[i + 1]

            t1 = self.__parameters["pheromones"][a][b]
            self.__parameters["pheromones"][a][b] =(1- self.__parameters["degradation"]) * t1 + \
                                                    self.__parameters["pheromoneQuantity"] / ant.cost

    def __dinamic(self):
        x = random.randint(0, self.__parameters["numberOfCities"] - 1)
        y = random.randint(0, self.__parameters["numberOfCities"] - 1)
        self.__parameters["graph"][x][y] *= 2
        self.__parameters["graph"][x][y] *= (1 / 2)

    def __bestAnt(self):
        bestAnt = self.__ants[0]
        for ant in self.__ants:
            if ant.cost < bestAnt.cost:
                bestAnt = ant
        return bestAnt


    def run(self):
        self.__initialize();
        for i in range(self.__parameters["numberOfGenerations"]):
            self.__initializeAnts()
            for j in range(self.__parameters["numberOfCities"] - 1):
                for ant in self.__ants:
                    ant.selectNextCity()

                for ant in self.__ants:
                    ant.updatePheromone()


            bestAnt = self.__bestAnt()
            self.__updatePheromoneGlobal(bestAnt)
            print("GENERATIA: " + str(i + 1) + " CEA MAI BUNA FURNICA: " + str(bestAnt.cost) + " #### " + str(
                bestAnt.path))
            print()
