import itertools
import time
import random


# def score(pizzas):
#     return len(set(pizzas))


with open("b_little_bit_of_everything.in") as file:
    firstLine = list(map(int, file.readline().strip().split(" ")))
    N = firstLine[0]  # number of pizzas
    teams = {
        2: firstLine[1],
        3: firstLine[2],
        4: firstLine[3]
    }

    pizzas = []
    for i in range(N):
        line = file.readline().strip().split(" ")
        numberOfIngredients = int(line[0])
        ingredients = line[1:]
        pizzas.append(ingredients)


pizzasIndices = list(range(N))
# N = M
score = 0
deliveries = []
choices = [2,3,4]
cpt = 0
while True:
    r = random.choice(choices) # the number of members of the team
    # r = choices[-1]
    if teams[r] > 0:
        teams[r] -= 1
    else:
        choices.remove(r)
        # choices.pop()
        if len(choices) == 0:
            break
        continue

    cpt += 1
    delivery = [r]
    deliveryIngredients = set()
    for _ in range(r):
        b = random.choice(pizzasIndices) 
        pizzasIndices.remove(b)
        delivery.append(b)
        deliveryIngredients.update(pizzas[b])
    deliveries.append(delivery)
    score += len(deliveryIngredients)**2

    N -= r

    if N <= 1:
        break

    if N <= 4:
        cpt += 1
        delivery = [N]
        deliveryIngredients = set()
        for _ in range(N):
            b = random.choice(pizzasIndices) 
            pizzasIndices.remove(b)
            delivery.append(b)
            deliveryIngredients.update(pizzas[b])
        deliveries.append(delivery)
        score += len(deliveryIngredients)**2
        break

with open("b_little_bit_of_everything.txt", 'w') as file:
    print(cpt, file=file)
    for delivery in deliveries:
        print(*delivery, sep=' ', file=file)

print("score =", score)
