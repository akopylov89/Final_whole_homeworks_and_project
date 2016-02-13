list = (range(7))
symm = 0
for i in list:
    if list[i] % 2 != 0:
        symm = symm + list[i]
        result = symm * list[-1]
print ("The result of multiplying the odd elements of the list and the last = {}".format(result))


