import itertools
import time
import random
import os

names = [
    # "a_example",
    # "b_little_bit_of_everything",
    # "c_many_ingredients",
    "d_many_pizzas",
    # "e_many_teams",
]

scoreTotal = 0
numberOfIterations = 1
step = int(numberOfIterations * 0.1)
if step == 0:
    step = 1

for name in names:
    if name not in os.listdir("drafts"):
        os.mkdir("drafts/"+name)

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
        
        pizzasSorted = sorted(enumerate(pizzas), key=lambda e: len(e[1]))
 
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
        b = 0
        teamsCopy = teams.copy()
        N = M
        pizzasIndices = list(range(N))
        score = 0
        deliveries = []
        choices = [2, 3, 4]
        cpt = 0
        while True:
            # r = random.choice(choices)  # the number of members of the team
            r = choices[-1]
            if teamsCopy[r] > 0:
                teamsCopy[r] -= 1
            else:
                choices.remove(r)
                if len(choices) == 0:
                    break
                continue
 
            cpt += 1
            delivery = [r]
            deliveryIngredients = set(pizzasSorted[b][1])
            for _ in range(r-1):
                oldScore = len(deliveryIngredients)
                deliveryIngredientsCopy1 = deliveryIngredients.copy()
                deliveryIngredientsCopy1.update(pizzasSorted[b][1]) # next in the list
                newScore1 = len(deliveryIngredientsCopy1)

                indice = random.choice(pizzasIndices) # random choice
                deliveryIngredientsCopy2 = deliveryIngredients.copy()
                deliveryIngredientsCopy2.update(pizzasSorted[indice][1])
                newScore2 = len(deliveryIngredientsCopy2)

                if newScore1 > newScore2:
                    deliveryIngredients = deliveryIngredientsCopy1
                    pizzasIndices.remove(b)
                    delivery.append(pizzasSorted[b][0])
                    deliveryIngredients.update(pizzasSorted[b][1])
                    b += 1
                else:
                    deliveryIngredients = deliveryIngredientsCopy2
                    pizzasIndices.remove(indice)
                    delivery.append(pizzasSorted[indice][0])
                    deliveryIngredients.update(pizzasSorted[indice][1])

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
                    delivery.append(pizzasSorted[b][0])
                    deliveryIngredients.update(pizzasSorted[b][1])
                    b += 1
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
    scoreTotal += bestScore


print("\n<<<<<<<<<<<<<<<<<< score total =", scoreTotal, ">>>>>>>>>>>>>>>>>>>>>>\n")