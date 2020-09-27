# Simple Genetic Algorithm Demo
Genetic Algorithm is a problem solving technique inspired by process of natural selection. It can be used to find optimal or near-optimal solutions to constrained as well as unconstrained optimization problems.
This project is a simple demonstration of using Genetic algorithm for solving linear equations of the form ax1 + bx2 + cx3 +...= d where (x1, x2, x3,..) are the unknown variables and (a,b,c...d) are the coefficients.

The coefficients are entered as a list assigned to the variable `coeffs`

The `Population` class represents a population of individuals where each individual is an instance of the `Individual` class. Each individual has a fitness score. The individuals with the highest fitness scores take part in crossover i.e. they reproduce to generate a new individual, a child. The child then undergoes a mutation process which can be controlled by a `mutation_rate` parameter. The mutation operation adds genetic diversity to the population. This individual is then added to the existing population and the individual with the lowest fitness score is removed from the population.

Eacch of the above mentioned processes are implemented using the functions `selection`, `crossover` and `mutation`.
