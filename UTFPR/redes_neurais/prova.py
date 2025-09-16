from easyga import EasyGA, crossover, mutation
import random

# Modelagem do GA com o framework
ga = EasyGA.GA()                                      # Resposta 1 Questão 2

# Parâmetros: Tamanho cromossomo
ga.chromosome_length = 10                             # Resposta 2 Questão 2

# Tipo de valor de cada gene
ga.gene_impl = lambda: random.randint(0, 1)           # Resposta 3 Questão 2

# Tipo de problema de otimização 
ga.target_fitness_type = 'max'                        # Resposta 4 Questão 2

# Faz a escolha do tipo de cruzamento e mutação
ga.crossover_function = crossover.Crossover.Individual.single_point     # Resposta 5 Questão 2
ga.mutation_function = mutation.Mutation.Individual.individual_genes    # Resposta 6 Questão 2
