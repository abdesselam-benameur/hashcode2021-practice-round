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
        
        pizzasSorted = sorted(enumerate(pizzas), key=lambda e: len(e[1]), reverse=True)
 
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
    value = 5
    score = 0
    cpt = 0
    deliveries = []
    choices = [2, 3, 4]
    while True:
        r = choices[-1]
        if teams[r] > 0:
            teams[r] -= 1
        else:
            choices.remove(r)
            if len(choices) == 0:
                break
            continue

        # cpt += 1
        delivery = [r]
        s = 0

        delivery.append(pizzasSorted[0][0])
        deliveryIngredients = set(pizzasSorted[0][1])

        for _ in range(r-1):
            for j in range(1, len(pizzasSorted)):
                
                deliveryIngredientsCopy = deliveryIngredients.copy()
                deliveryIngredientsCopy.update(pizzasSorted[j][1])

                t = len(deliveryIngredients)

                if t > s:
                    s = t
                    meillurePizza = pizzasSorted[j][0]
                    k = j

            delivery.append(meillurePizza)
            deliveryIngredients.update(pizzasSorted[k][1])
            pizzasSorted.pop(k)
            
        pizzasSorted.pop(0)
        deliveries.append(delivery)
        cpt += 1
        score += s**2
        if cpt == value:
            print("I have done {} deliveries so far (score = {})".format(value, score))
            value += 5

        N -= r

        if N <= 1:
            break

        if N <= 4: # N in [2,3,4]
            if teams[N] > 0:
                delivery = [N]
                deliveryIngredients = set()
                for _ in range(N):
                    delivery.append(pizzasSorted[0][0])
                    deliveryIngredients.update(pizzasSorted[0][1])
                    pizzasSorted.pop(0)
                deliveries.append(delivery)
                cpt += 1
                score += len(deliveryIngredients)**2
                break
            else:
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
            print(len(deliveries), file=file)
            for delivery in deliveries:
                print(*delivery, sep=" ", file=file)
            # delete the last newline
            file.truncate(file.tell() - len(os.linesep))
 
    print("best score after {} iterations ({}) =".format(numberOfIterations, nameOfFile), bestScore)
    print("---- %s seconds ----" % (time.time() - start_time))
    scoreTotal += bestScore


print("\n<<<<<<<<<<<<<<<<<< score total =", scoreTotal, ">>>>>>>>>>>>>>>>>>>>>>\n")