import itertools
import time
import random
import os

names = [
    # "a_example",
    "b_little_bit_of_everything",
    "c_many_ingredients",
    "d_many_pizzas",
    "e_many_teams",
]

scoreTotal = 0
numberOfIterations = 10
step = int(numberOfIterations * 0.1)
if step == 0:
    step = 1

for name in names:
    if name not in os.listdir("drafts"):
        os.mkdir("drafts/"+name)

for nameOfFile in names:
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
        
        pizzasSorted = sorted(enumerate(pizzas), key=lambda e: len(e[1]), reverse=True)
 
    try:
        bestScore = int(
            sorted(os.listdir("drafts/{}".format(nameOfFile)))[-1].split(" ")[1][:-4])
    except IndexError:
        bestScore = 0

    values = list(range(0, numberOfIterations, step))
    values.append(numberOfIterations)

    for i in range(numberOfIterations):
        # try:
        #     bestScore = int(
        #         sorted(os.listdir("drafts/{}".format(nameOfFile)))[-1].split(" ")[1][:-4])
        # except IndexError:
        #     bestScore = 0
        start_time = time.time()
        pizzasSortedCopy = pizzasSorted.copy()
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

            delivery = [r, pizzasSortedCopy[b][0]]
            deliveryIngredients = set(pizzasSortedCopy[b][1])
            # TODO: transform the next line to this: pizzasIndices.pop(0)
            # pizzasIndices.pop(0)
            pizzasSortedCopy.pop(0)

            for _ in range(1, r):
                # oldScore = len(deliveryIngredients)
                deliveryIngredientsCopy1 = deliveryIngredients.copy()
                deliveryIngredientsCopy1.update(pizzasSortedCopy[0][1])  # the next pizza in the list
                newScore1 = len(deliveryIngredientsCopy1)

                pizza = random.choice(pizzasSortedCopy[1:])  # a random pizza in pizzaSorted[1:]
                deliveryIngredientsCopy2 = deliveryIngredients.copy()
                deliveryIngredientsCopy2.update(pizza[1])
                newScore2 = len(deliveryIngredientsCopy2)

                if newScore1 >= newScore2:
                    deliveryIngredients = deliveryIngredientsCopy1
                    # TODO: transform the next line to this: pizzasIndices.pop(0)
                    delivery.append(pizzasSortedCopy[0][0])
                    deliveryIngredients.update(pizzasSortedCopy[0][1])
                    # pizzasIndices.pop(0)
                    pizzasSortedCopy.pop(0)
                    # b += 1
                else:
                    deliveryIngredients = deliveryIngredientsCopy2
                    delivery.append(pizza[0])
                    deliveryIngredients.update(pizza[1])
                    # pizzasIndices.remove(pizza[0])
                    pizzasSortedCopy.remove(pizza)

            deliveries.append(delivery)
            cpt += 1
            # if cpt == value:
            #     print("I have done {} deliveries so far".format(cpt))
            score += len(deliveryIngredients)**2

            N -= r

            if N <= 1:
                break

            if N <= 4:
                while N >= 2:
                    if teamsCopy[N] > 0:
                        delivery = [N]
                        deliveryIngredients = set()
                        for _ in range(N):
                            delivery.append(pizzasSortedCopy[b][0])
                            deliveryIngredients.update(pizzasSortedCopy[b][1])
                            b += 1
                        deliveries.append(delivery)
                        cpt += 1
                        score += len(deliveryIngredients)**2
                        break
                    else:
                        N -= 1
                break

        # print("I have done {} deliveries so far with score = {}".format(cpt, score))
        if score > bestScore:
            print("{} new best score = {} previous best score = {}".format(nameOfFile, score, bestScore), "---- %s seconds ----" % (time.time() - start_time))
            print("############################## new best score ##############################")
            bestScore = score
            try:
                os.remove("drafts/{}/{}".format(
                    nameOfFile,
                    os.listdir("drafts/{}".format(nameOfFile))[0]))
            except IndexError:
                pass
            with open("drafts/{0}/{0} {1}.txt".format(nameOfFile, score), "w") as file:
                print(len(deliveries), file=file)
                for delivery in deliveries:
                    print(*delivery, sep=" ", file=file)
                # delete the last newline
                file.truncate(file.tell() - len(os.linesep))
 
    print("---- %s seconds ----" % (time.time() - start_time))
    # scoreTotal += score


# print("\n<<<<<<<<<<<<<<<<<< score total =", scoreTotal, ">>>>>>>>>>>>>>>>>>>>>>\n")
