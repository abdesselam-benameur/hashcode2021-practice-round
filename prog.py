import itertools
import time
import random
import os

names = [
    # "a_example",
    # "b_little_bit_of_everything",
    # "c_many_ingredients",
    # "d_many_pizzas",
    "e_many_teams",
]
choices = [3, 2, 4]

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
        
        pizzasSorted = sorted(enumerate(pizzas), key=lambda e: len(e[1]), reverse=True) # descending order
 
    try:
        bestScore = int(
            os.listdir("drafts/{}".format(nameOfFile))[0].split(" ")[1][:-4])
    except IndexError:
        bestScore = 0

    # values = list(range(0, numberOfIterations, step))
    # values.append(numberOfIterations)

    # for i in range(numberOfIterations):
    #     if i == values[0]:
    #         values.pop(0)
    #         print("iteration {}".format(i))
    # teams = teams.copy()

    # b = 0
    N = M
    value = 1000
    score = 0
    cpt = 0
    deliveries = []
    # choices = [4, 3, 2]

    for choice in choices:
        while True:
            if teams[choice] > 0:
                teams[choice] -= 1
            else:
                break

            delivery = [choice, pizzasSorted[0][0]]
            deliveryIngredients = set(pizzasSorted[0][1])
            pizzasSorted.pop(0)

            for _ in range(1, choice):
                try:
                    delivery.append(pizzasSorted[-1][0])
                    deliveryIngredients.update(pizzasSorted[-1][1])
                    pizzasSorted.pop()
                except IndexError: #FIXME: Fix this exception
                    print(pizzasSorted)
                    

            score += len(deliveryIngredients)**2
            # TODO: use myLen() instead of len() where myLen = len for faster results
            deliveries.append(delivery)
            cpt += 1

            if cpt == value:
                print("I have done {} deliveries so far (score = {})".format(value, score))
                value += 1000

            N -= choice

            if N <= 1:
                break

            if N <= 4: # N in [2,3,4]
                if teams[N] > 0:
                    delivery = [N, pizzasSorted[0][0]]
                    deliveryIngredients = set(pizzasSorted[0][1])
                    for _ in range(1, N):
                        delivery.append(pizzasSorted[-1][0])
                        deliveryIngredients.update(pizzasSorted[-1][1])
                        pizzasSorted.pop()

                    score += len(deliveryIngredients)**2
                    deliveries.append(delivery)
                    break
                else:
                    break
                   
    if score > bestScore:
        print("new best score 💪")
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
    print("this times's score =", score)
    print("best score after {} iterations ({}) =".format(numberOfIterations, nameOfFile), bestScore)
    print("---- %s seconds ----" % (time.time() - start_time))
    scoreTotal += bestScore


print("\n<<<<<<<<<<<<<<<<<< score total =", scoreTotal, ">>>>>>>>>>>>>>>>>>>>>>\n")