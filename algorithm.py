import random

MAX_ITERATIONS = 50000

class TrialAndError:
    def __init__(self, domain):
        self._domain = domain

    def randomSolution(self):
        """ Get a random solution to evaluate """
        cities = [i for i in range(self._domain.shape[0])]
        random.shuffle(cities)
        return cities

    def getDistance(self, city1, city2):
        """ Get the distance between two cities """
        return self._domain[city1][city2]

    def commit(self):
        """ Trial and error algorithm """
        global MAX_ITERATIONS

        global_result = 1000
        global_solution = []
        iteration_normalizer = 0

        while iteration_normalizer < MAX_ITERATIONS:
            solution = self.randomSolution()

            result_per_solution = 0

            for index in range(len(solution)):
                try:
                    result_per_solution += self.getDistance(solution[index], solution[index+1])
                except IndexError:
                    result_per_solution += self.getDistance(solution[index], solution[0])

            if result_per_solution < global_result:
                global_result = result_per_solution
                global_solution = solution
            else:
                iteration_normalizer += 1

        return (global_result, global_solution)


