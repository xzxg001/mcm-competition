import random

# 定义参数
component1_defective_rate = 0.05  # 零配件1的次品率
component1_cost = 4  # 零配件1的单价
detection_cost_1 = 2  # 零配件1的检测成本
component2_defective_rate = 0.05  # 零配件2的次品率
component2_cost = 18  # 零配件2的单价
detection_cost_2 = 3  # 零配件2的检测成本
final_product_defective_rate = 0.05  # 最终产品的次品率

assembly_cost = 6  # 装配一个成品的成本
detection_cost_final = 3  # 成品的检测成本
market_price = 56  # 成品的市场售价
replacement_loss = 10  # 替换不合格品的损失
disassembly_cost = 40  # 拆解一个不合格品的成本

# 适应度函数，计算个体的净利润
def fitness(individual):
    detected1, detected2, assembled, disassembled = individual
    cost = 0
    profit = 0

    if detected1:
        cost += detection_cost_1  # 增加零配件1的检测成本
    if detected2:
        cost += detection_cost_2  # 增加零配件2的检测成本

    if assembled:
        cost += assembly_cost  # 增加装配成本
        if individual[2]:  # 如果成品检测为真
            cost += detection_cost_final  # 增加成品的检测成本

    if disassembled:
        cost += disassembly_cost  # 增加拆解成本

    # 模拟生产一定数量的产品
    quantity = 100  # 假设生产100个成品
    for _ in range(quantity):
        c1_quality = random.random() > component1_defective_rate  # 随机确定零件是否合格
        c2_quality = random.random() > component2_defective_rate
        # 成品合格需要两个零件都合格，并且装配后也合格
        final_quality = c1_quality and c2_quality and (random.random() > final_product_defective_rate)
        if final_quality:
            profit += market_price - component1_cost - component2_cost - assembly_cost
        else:
            profit -= replacement_loss  # 不合格品导致损失

    return profit - cost  # 返回净利润作为适应度

# 初始化种群
def create_population(size):
    population = []
    for _ in range(size):
        individual = [
            random.choice([True, False]),  # 随机决定是否检测零配件1
            random.choice([True, False]),  # 随机决定是否检测零配件2
            random.choice([True, False]),  # 随机决定是否检测成品
            random.choice([True, False])   # 随机决定是否拆解不合格品
        ]
        population.append(individual)
    return population

# 选择操作，使用轮盘赌选择方法
def select(population, fitnesses, num_parents):
    selected = []
    for _ in range(num_parents):
        total_fitness = sum(fitnesses)
        pick = random.uniform(0, total_fitness)
        current = 0
        for individual, fit in zip(population, fitnesses):
            current += fit
            if current > pick:
                selected.append(individual)
                break
    return selected

# 交叉操作
def crossover(parents, num_offspring):
    offspring = []
    for _ in range(num_offspring):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = [
            random.choice([parent1[i], parent2[i]]) for i in range(len(parent1))
        ]
        offspring.append(child)
    return offspring

# 变异操作
def mutate(offspring):
    for individual in offspring:
        if random.random() < 0.1:  # 变异概率为10%
            index = random.randint(0, len(individual) - 1)
            individual[index] = not individual[index]
    return offspring

# 遗传算法主函数
def genetic_algorithm(population_size, num_generations, num_parents, num_offspring):
    population = create_population(population_size)
    for generation in range(num_generations):
        fitnesses = [fitness(individual) for individual in population]
        parents = select(population, fitnesses, num_parents)
        offspring = crossover(parents, num_offspring)
        offspring = mutate(offspring)
        population = parents + offspring
        best_individual = max(population, key=fitness)
        print(f"Generation {generation}: Best Fitness = {fitness(best_individual)}")
    return best_individual, fitness(best_individual)

# 运行遗传算法10000次
best_profit = -float('inf')
best_solution = None

for _ in range(1):
    solution, profit = genetic_algorithm(
        population_size=50,
        num_generations=10000,
        num_parents=10,
        num_offspring=40
    )
    if profit > best_profit:
        best_profit = profit
        best_solution = solution

print("Best Solution:", best_solution)
print("Best Profit:", best_profit)