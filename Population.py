import Individual


class Population:
    
    def __init__(self, populationSize, fitness_params):
        self.individuals = []
        for i in range(populationSize):
            self.individuals.append(Individual.Individual())
        
        self.sortPopulation()
        

    def sortPopulation(self):
        self.individuals.sort(key = lambda ind: ind.fitness(), reverse=True)

    def fittest(self):
        return self.individuals[0]

    def secondFittest(self):
        return self.individuals[1]

    def addIndividual(self,child):
        #self.individuals.pop()
        self.individuals.pop(-1)
        self.individuals.append(child)
        self.sortPopulation()
