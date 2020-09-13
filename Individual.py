import random


class Individual:
    fitness_params = [1,1]
    def __init__(self, gns=None):
        self.geneLen = 30
        self.genes = []
        
        if gns is None:
            for i in range(0,self.geneLen):
                self.genes.append(int(random.randint(0,100)<50))
        else:
            self.genes = gns

            
    def __str__(self):
        return str(self.get_vec())


    def get_vec(self):
        no_of_vars = len(Individual.fitness_params) - 1
        partitionLen = self.geneLen//no_of_vars
        params = []
        for i in range(no_of_vars):
            params.append(self.genes[i*partitionLen:(i+1)*partitionLen])

        x = []
        for sub in params:
            s = "".join(map(str, sub))
            x.append(int(s, 2))

        return x


    def fitness(self):
        x = self.get_vec()
        
        expr_res = sum([a*xi for a,xi in zip(Individual.fitness_params[:-1],x)])
        return -abs(Individual.fitness_params[-1] - expr_res)
