import itertools
import time
import random
import os

names = [
    "a_example",
    "b_little_bit_of_everything",
    "c_many_ingredients",
    "d_many_pizzas",
    "e_many_teams",
]

numberOfIterations = 10
step = int(numberOfIterations * 0.1)

for name in names:
    if name not in os.listdir("drafts"):
        os.mkdir("drafts/"+name)
 
# nameOfFile = names[1]
for nameOfFile in names:
    start_time = time.time()
    with open("{}.in".format(nameOfFile)) as file:
        firstLine = list(map(int, file.readline().strip().split(" ")))
        M = firstLine[0]  # number of pizzas
        teams = {2: firstLine[1], 3: firstLine[2], 4: firstLine[3]}
 
        pizzas = []
        for i in range(M):
            line = file.readline().strip().split(" ")
            numberOfIngredients = int(line[0])
            ingredients = line[1:]
            pizzas.append(ingredients)
 
    try:
        bestScore = int(
            os.listdir("drafts/{}".format(nameOfFile))[0].split(" ")[1][:-4])
    except IndexError:
        bestScore = 0

    values = list(range(0, numberOfIterations, step))
    values.append(numberOfIterations)

    for i in range(numberOfIterations):
        if i == values[0]:
            values.pop(0)
            print("iteration {}".format(i))
        teamsCopy = teams.copy()
        N = M
        pizzasIndices = list(range(N))
        score = 0
        deliveries = []
        choices = [2, 3, 4]
        cpt = 0
        while True:
            r = random.choice(choices)  # the number of members of the team
            # r = choices[-1]
            if teamsCopy[r] > 0:
                teamsCopy[r] -= 1
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
 
        if score > bestScore:
            bestScore = score
            try:
                os.remove("drafts/{}/{}".format(
                    nameOfFile,
                    os.listdir("drafts/{}".format(nameOfFile))[0]))
            except IndexError:
                pass
            with open("drafts/{0}/{0} {1}.txt".format(nameOfFile, score), "w") as file:
                print(cpt, file=file)
                for delivery in deliveries:
                    print(*delivery, sep=" ", file=file)
                # delete the last newline
                file.truncate(file.tell() - len(os.linesep))
 
    print("best score after {} iterations ({}) =".format(numberOfIterations, nameOfFile), bestScore)
    print("---- %s seconds ----" % (time.time() - start_time))