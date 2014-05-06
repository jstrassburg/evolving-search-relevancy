#   Copyright 2014 James Strassburg
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import random
from deap import creator, base, tools, algorithms
from CandidateSolution import CandidateSolution


class Program:
    def __init__(self):
        pass

    @staticmethod
    def main():
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        toolbox = base.Toolbox()
        toolbox.register("attr_bool", random.randint, 0, 1)
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, CandidateSolution.size)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", CandidateSolution.evaluate)
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        population = toolbox.population(n=200)

        hof = tools.HallOfFame(maxsize=1)
        final_population = algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.1, ngen=10, halloffame=hof)

        print final_population
        print "Best solution: {0}, fitness: {1}".format(hof[0], hof[0].fitness)

        best_solution = CandidateSolution(hof[0])
        print "Best solution: name_boost = {0}, description_boost = {1}".format(
            best_solution.name_boost.value, best_solution.description_boost.value)

if __name__ == "__main__":
    Program.main()