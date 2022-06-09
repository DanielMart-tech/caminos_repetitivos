# Program to generate a third list with the repeated elements in the first two lists

list_1 = ["h", "e", "l", "l", "o", " ", "t", "e", "a", "m"]
list_2 = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
list_3 = []

for i in list_1.copy():
    for j in list_2.copy():
        if i == j:
            if list_3.count(i) == 0:
                list_3.append(i)
                break

print(list_3)