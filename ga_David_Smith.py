# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 00:34:06 2018

@author: iancs
"""

import random
import string
import math

geneset = string.ascii_letters + " !"
target = "Hello World!"
targetLength = len(target)
poolSize = 350
generations = 1000
crossoverRate = 0.80
mutationRate = 0.05

# Creating initial population by generating strings of random characters taken from geneset and of target length. 


def randomPopulation():
  pop = []
  for i in range(poolSize):
    dna = ""
    for c in range(targetLength):
      dna += random.choice(geneset)
    pop.append(dna)
    
  return pop

# Fitness is rated from matching letters in the generated parents and the target. 


def getFitness(pop = []):
    popFitness = {}    
    for i in range(poolSize):       
        fitness = 0.0        
        for c in range(targetLength):        
            if target[c] == pop[i][c]:            
                fitness += 1
        
        fitness = fitness / targetLength
        popFitness[i] = fitness

    
#  Elitist sorting of population with high to low fitness ranking.
        
    sortedFitness = [(k, popFitness[k]) for k in sorted(popFitness, key = popFitness.get, reverse = True)]
    
    return sortedFitness
        
# Crossover


def crossover(pop = [], fitness = []):
    
    # Designating selection from population for mating and applying crossover probability.
    
    newPopulation = []
    selection = (int)(poolSize) / 2
    
    for i in range(poolSize):
        
        if random.random() < crossoverRate:
            
            # Favouring the best performing candidates in the population but still allowing for mating of poorer ones.        
            
            if(random.random() < 0.75):                
                parentOne = pop[fitness[random.randrange(0, selection)][0]]
                parentTwo = pop[fitness[random.randrange(0, selection)][0]]
            
                crossoverPoint = random.randint(0, targetLength)
                child = parentOne[:crossoverPoint] + parentTwo[crossoverPoint:]
                newPopulation.append(child)
              
   
            else:
                parentOne = pop[fitness[random.randrange(0, poolSize - 1)][0]]
                parentTwo = pop[fitness[random.randrange(0, poolSize - 1)][0]]
                
                crossoverPoint = random.randint(0, targetLength)
                child = parentOne[:crossoverPoint] + parentTwo[crossoverPoint:]
                newPopulation.append(child)

    # Duplicating parents if crossover threshold not reached to ensure pool size consistent. 
                
        else:
            newPopulation.append(pop[fitness[random.randrange(0, poolSize - 1)][0]])
            
    return newPopulation

# Mutating according to mutation rate.


def mutate(pop = []):
    for i in range(poolSize):
        if random.random() < mutationRate:
            mutateSite = random.randint(0, targetLength - 1)
            tempString = list(pop[i])
            tempString[mutateSite] = random.choice(geneset)
            pop[i] = "".join(tempString)
            
# Main function.


def geneticAlgorithm():
    population = randomPopulation()
    populationFitness = getFitness(population)
    finalResult = ""
    generation = 0
    limit = 10000

    # While loop containing termination condition.
    
    while finalResult != target:
        population = crossover(population, populationFitness)
        mutate(population)
        populationFitness = getFitness(population)
        finalResult = population[populationFitness[0][0]]
        print("Current best result = %s : Generation %d" % (finalResult, generation))
        generation = generation + 1
        if generation == limit:
            break
    print("Solved target in %d generations" % generation)
    return generation


geneticAlgorithm() 

# Finding average generations over iteration amount. 
    
gens = []
iterations = 100


def getAverage(iterations):
    for i in range(iterations):
        gens.append(geneticAlgorithm())
    averageGen = float(sum(gens))/(iterations)
    print("Average generations in %s iterations = %d" % (iterations, averageGen))
    return averageGen


getAverage(iterations)
    
# Comparative random iteration of initial population.


def randomAlgorithm():
    population = randomPopulation()
    populationFitness = getFitness(population)
    finalResult = ""
    generation = 0
    limit = 10000

    # While loop containing termination condition.
    
    while finalResult != target:
        population = randomPopulation()
        populationFitness = getFitness(population)
        finalResult = population[populationFitness[0][0]]
        print("Current best result = %s : Generation %d" % (finalResult, generation))
        generation = generation + 1
        if generation == limit:
            break
    
    print("Solved target in %d generations" % generation) 


#randomAlgorithm()


# How many random solutions are there?

x = 2  # Doubling alphabet length to account for lower and upper case.
y = 26 # Length of alphabet.
z = 2 # "!" and " " symbols.
n = 12 # Length of 12 possible characters.
b = x + y + z
c = (math.factorial(b)) / (math.factorial(b - n))
print(c)