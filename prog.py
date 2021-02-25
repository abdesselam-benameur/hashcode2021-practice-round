import itertools
import time
import random
import os
import matplotlib.pyplot as plt 

numberOfIngredients_dict = {
    "a_example": 7,
    "b_little_bit_of_everything": 10,
    "c_many_ingredients": 10000,
    "d_many_pizzas": 100,
    "e_many_teams": 100,
}

names = [
    # "a_example",
    "b_little_bit_of_everything",
    # "c_many_ingredients",
    # "d_many_pizzas",
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

# if "stats.txt" not in os.listdir():
    # with open("stats.txt", "w") as f:
    #     # create the file stats.txt
    #     pass

for nameOfFile in names:
    start_time = time.time()
    x, y = [], []
    allIngredients = {}
    ingredients_dict = {}
    with open("drafts/ingredients_stats/{} ingredients.txt".format(nameOfFile)) as file:
        file.readline()
        for line in file:
            line = line.split()[1:]
            ingredient = line[0]
            l = list(map(int, line[1:]))
            ingredients_dict[ingredient] = l
            y += l
            x += [ingredient]*len(l)
    
    # plotting the points
    plt.plot(x, y, linestyle='', marker=',')

    # naming the x axis x²
    plt.xlabel('pizzas') 
    # naming the y axis 
    plt.ylabel('ingredients') 
    plt.title(nameOfFile)
    plt.show()
    # pizzasSorted = sorted(enumerate(pizzas), key=lambda e: (len(e[1]), e[1]), reverse=True)
    # allIngredients = sorted(ingredients_dict)

    # with open("drafts/matrices/{} matrix.csv".format(nameOfFile), "w") as file:
    #     print("Number of Pizzas ({}) x Number of ingredients ({})".format(M, len(allIngredients)),  file=file)
    #     print(" ", *allIngredients, sep=', ', file=file)
    #     for i in range(M):
    #         print(i, end=", ", file=file)
    #         print(*pizzas_dict[i], sep=', ', file=file)
    # print("---- %s seconds ----" % (time.time() - start_time))
    #     # for ingredient in allIngredients:
    #     #     ingredients_dict[ingredient].sort()
    #     #     print(len(ingredients_dict[ingredient]), ingredient , *ingredients_dict[ingredient], sep=" ", file=file)
    

    # with open("drafts/ingredients/{0} ingredients.txt".format(nameOfFile), "w") as file:
    #     print(len(ingredients_dict),  file=file)
    #     for ingredient in allIngredients:
    #         ingredients_dict[ingredient].sort()
    #         print(len(ingredients_dict[ingredient]), ingredient , *ingredients_dict[ingredient], sep=" ", file=file)

    # with open("drafts/sorted/{0} sorted.txt".format(nameOfFile), "w") as file:
    #     print(M, *list(teams.values()),  file=file)
    #     for pizza in pizzasSorted:
    #         print(len(pizza[1]), *pizza[1], '\n', sep=" ", file=file)


#     try:
#         bestScore = int(
#             os.listdir("drafts/{}".format(nameOfFile))[0].split(" ")[1][:-4])
#     except IndexError:
#         bestScore = 0

#     values = list(range(0, numberOfIterations, step))
#     values.append(numberOfIterations)

#     for i in range(numberOfIterations):
#         if i == values[0]:
#             values.pop(0)
#             print("iteration {}".format(i))
#         b = 0
#         teamsCopy = teams.copy()
#         N = M
#         # pizzasIndices = list(range(N))
#         score = 0
#         deliveries = []
#         choices = [2, 3, 4]
#         cpt = 0
#         while True:
#             # r = random.choice(choices)  # the number of members of the team
#             r = choices[-1]
#             if teamsCopy[r] > 0:
#                 teamsCopy[r] -= 1
#             else:
#                 choices.remove(r)
#                 if len(choices) == 0:
#                     break
#                 continue
 
#             cpt += 1
#             delivery = [r]
#             deliveryIngredients = set()
#             for _ in range(r):
#                 delivery.append(pizzasSorted[b][0])
#                 deliveryIngredients.update(pizzasSorted[b][1])
#                 b += 1
#             deliveries.append(delivery)
#             score += len(deliveryIngredients)**2
 
#             N -= r
 
#             if N <= 1:
#                 break
 
#             if N <= 4:
#                 cpt += 1
#                 delivery = [N]
#                 deliveryIngredients = set()
#                 for _ in range(N):
#                     delivery.append(pizzasSorted[b][0])
#                     deliveryIngredients.update(pizzasSorted[b][1])
#                     b += 1
#                 deliveries.append(delivery)
#                 score += len(deliveryIngredients)**2
#                 break
 
#         if score > bestScore:
#             bestScore = score
#             try:
#                 os.remove("drafts/{}/{}".format(
#                     nameOfFile,
#                     os.listdir("drafts/{}".format(nameOfFile))[0]))
#             except IndexError:
#                 pass
#             with open("drafts/{0}/{0} {1}.txt".format(nameOfFile, score), "w") as file:
#                 print(cpt, file=file)
#                 for delivery in deliveries:
#                     print(*delivery, sep=" ", file=file)
#                 # delete the last newline
#                 file.truncate(file.tell() - len(os.linesep))
 
#     print("best score after {} iterations ({}) =".format(numberOfIterations, nameOfFile), bestScore)
#     print("---- %s seconds ----" % (time.time() - start_time))
#     scoreTotal += bestScore


# print("\n<<<<<<<<<<<<<<<<<< score total =", scoreTotal, ">>>>>>>>>>>>>>>>>>>>>>\n")