parol_number = list()
def random_number(rand_num):
    global parol_number
    for i in range(1, 21):
        j = i + 1
        while i + j <= rand_num:
            if rand_num % (i + j) == 0:
                real_number = (i, j)
                parol_number.append(real_number)
            j += 1
    print(parol_number)
    return parol_number
random_number(5)
random_number(18)
