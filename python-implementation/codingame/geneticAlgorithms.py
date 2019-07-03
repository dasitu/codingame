import random
import string
import sys


def get_letter():
    alphabet = string.ascii_letters + " !'."
    return random.choice(alphabet)


def create_chromosome(size):
    chromosome = ""
    for i in range(size):
        chromosome += get_letter()
    return chromosome


def get_answer():
    answer = 'This is a robot!'
    return answer


def is_answer(answer):
    #print(answer)
    if answer == get_answer():
        return True
    return False


def get_score(chrom):
    key = get_answer()
    score = 0
    for i in range(len(key)):
        if i < len(chrom) and chrom[i] == key[i]:
                score += 1
    return score/len(key)


def score(chrom):
    return get_score(chrom)


def get_mean_score(population):
    total_score = 0
    for chrom in population:
        total_score += score(chrom)
    return total_score/len(population)


def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    selected_chromesomes = []
    chromo_score = {}
    for chromosome in chromosomes_list:
        chromo_score[chromosome] = score(chromosome)
    sorted_chromesome_list = [k for k in sorted(chromo_score, key=chromo_score.get, reverse=True)]

    best_fitting_count = int(GRADED_RETAIN_PERCENT * len(chromosomes_list))
    random_count = int(NONGRADED_RETAIN_PERCENT * len(chromosomes_list))

    selected_chromesomes += sorted_chromesome_list[:best_fitting_count]
    selected_chromesomes += random.choices(population=sorted_chromesome_list[best_fitting_count+1:], k=random_count)
    return selected_chromesomes


def crossover(parent1, parent2):
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    child = parent1[:int(len(parent1)/2)] + parent2[int(len(parent2)/2):]
    return child


def mutation(chrom):
    #  * Random gene mutation : a character is replaced
    index = random.randint(0,len(chrom))
    new_chrom = ""
    for i in range(len(chrom)):
        if i == index:
            new_chrom += get_letter()
        else:
            new_chrom += chrom[i]
    return new_chrom


def create_population(pop_size, chrom_size):
    # use the previously defined create_chromosome(size) function
    population = []
    for i in range(pop_size):
        chrom = create_chromosome(chrom_size)
        population.append(chrom)
    return population


def generation(population):
    # selection
    # use the selection(population) function created on exercise 2
    #print("population:{}".format(population), file=sys.stderr)
    select = selection(population)
    #print("selected:{}".format(select), file=sys.stderr)

    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    while len(children) < len(select):
        ## crossover
        rand_nums = random.choices(population=range(0,len(select)),k=2)
        #print("rand_nums:{}".format(rand_nums), file=sys.stderr)
        parent1 = select[rand_nums[0]] # randomly selected
        parent2 = select[rand_nums[1]] # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        #print("patent1:{},parent2:{}".format(parent1,parent2), file=sys.stderr)

        child = crossover(parent1, parent2)
        #print("child:{}".format(child), file=sys.stderr)

        ## mutation
        # use the mutation(child) function created on exercise 2
        child = mutation(child)
        #print("mutated child:{}".format(child), file=sys.stderr)
        children.append(child)

    # return the new generation
    #print("children:{}".format(children), file=sys.stderr)
    return select + children


def algorithm():
    chrom_size = len(get_answer())
    population_size = 10

    # create the base population
    population = create_population(population_size, chrom_size)
    #print("base population:{}".format(population), file=sys.stderr)

    answers = []

    # while a solution has not been found :
    while not answers:
        ## create the next generation
        population = generation(population)

        ## display the average score of the population (watch it improve)
        print(get_mean_score(population), file=sys.stderr)

        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
    print(answers)


algorithm()