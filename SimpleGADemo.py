from Population import Population
from Individual import Individual
import random


populationSize = 50
coeffs = [1,2,3,10]
Individual.fitness_params = coeffs
p = Population(populationSize, coeffs)


# Elitism used for selecting parents
def selection(population):
	return (population.fittest(), population.secondFittest())


# The child will have genes from both parents.
# A crossover point is generated randomly.
def crossover(couple):
	xpoint = random.randint(0, couple[0].geneLen)
	child =  Individual(couple[0].genes[:xpoint] + couple[1].genes[xpoint:])
	mutation(child)
	p.addIndividual(child)



def mutation(ind):
	mut_pt = random.randint(0, ind.geneLen-1)
	ind.genes[mut_pt] = 1 - ind.genes[mut_pt]	


ctr=0
while(not(p.fittest().fitness()==0)):
	crossover(selection(p))
	ctr+=1
	# if(ctr%100000==0):
	# 	print(p.fittest().genes, p.fittest().fitness(), ctr)
	# 	print(int("".join(map(str, p.fittest().genes)),2))
	if(ctr%10000==0):
		break


print("Fittest: ",p.fittest())
print("Iterations: ", ctr)
print("Fitness score: ", p.fittest().fitness())
