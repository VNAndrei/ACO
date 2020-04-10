import bisect
import itertools
import random


class Ant:
    def __init__(self, antParameters):
        self.__parameters = antParameters
        self.__path = []
        self.__citiesToVisit = [i for i in range(0, self.__parameters["numberOfCities"])]
        self.__currentCity = random.randint(0, self.__parameters["numberOfCities"] - 1)
        self.__path.append(self.__currentCity)
        self.__citiesToVisit.remove(self.__currentCity)
        self.__cost = 0.0

    @property
    def cost(self):
        return self.__cost

    @property
    def path(self):
        return self.__path

    def chooseNode(self, choices, scores):
        total = sum(scores)
        cumdist = list(itertools.accumulate(scores)) + [total]
        index = bisect.bisect(cumdist, random.random() * total)
        return choices[min(index, len(choices) - 1)]

    def selectNextCity(self):
        scores = []
        for i in self.__citiesToVisit:
            scores.append(self.__parameters["pheromones"][self.__currentCity][i] ** self.__parameters["alpha"] * \
                          self.__parameters["eta"][self.__currentCity][i] ** self.__parameters["beta"])

        selected = self.chooseNode(self.__citiesToVisit, scores)
        self.__citiesToVisit.remove(selected)
        self.__path.append(selected)
        self.__cost += self.__parameters["graph"][self.__currentCity][selected]
        self.__currentCity = selected

    def updatePheromone(self):

        c1 = self.path[-2]
        c2 = self.path[-1]
        t1 = self.__parameters["pheromones"][c1][c2]
        self.__parameters["pheromones"][c1][c2] = (1 - self.__parameters["degradation"]) * t1 + \
                                                  self.__parameters["pheromoneQuantity"] / \
                                                  self.__parameters["graph"][c1][c2]

