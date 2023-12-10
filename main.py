from random import *

def evaluate(seed_val, target):
    seed(seed_val)
    generated = ''.join([chr(randint(0, 1000)) for _ in range(len(target))])
    return sum(g == t for g, t in zip(generated, target))

def generate_population(pop_size):
    return [randint(0, 2**32) for _ in range(pop_size)]

def select_parents(population, num_parents, target):
    return sample(sorted(population, key=lambda x: -evaluate(x, target))[:num_parents], 2)

def crossover(parent1, parent2):
    pivot = randint(0, 32)
    mask1 = (1 << pivot) - 1
    mask2 = (1 << 32 - pivot) - 1
    child1 = (parent1 & mask1) + (parent2 & mask2)
    child2 = (parent2 & mask1) + (parent1 & mask2)
    return child1, child2

def mutate(child):
    mutation_rate = 0.1
    bit_to_mutate = randint(0, 31)
    return child ^ (1 << bit_to_mutate) if random() < mutation_rate else child

def main(target, generations=1000):
    pop_size = 50000
    population = generate_population(pop_size)

    for gen in range(generations):
        parents = select_parents(population, 2, target)
        child1, child2 = crossover(*parents)
        child1 = mutate(child1)
        child2 = mutate(child2)

        if evaluate(child1, target) == len(target):
            print("Found seed:", child1)
            return

        if evaluate(child2, target) == len(target):
            print("Found seed:", child2)
            return

        population.extend([child1, child2])

    print("Algorithm did not find a solution within the specified generations.")

# Exemple d'utilisation
main("Hi!")