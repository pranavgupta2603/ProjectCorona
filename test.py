import random as rand
import numpy as np
rand.seed(23)
n = 100 #number of people
x = 0.1 # fraction of n representing the maximum no. of pairs
k = 10 #number of steps

p_max = x * n #max number of pairs at any time step
a_i = []
p_i = []

#print(np.zeros((6,), dtype=int)
for i in range(0, n):
    a_i.append(0)
    p_i.append(0)


def create_pair():
    c = []
    random_int1 = rand.randint(1, n)
    random_int2 = rand.randint(1, n)
    while random_int1 == random_int2:
        random_int1 = rand.randint(1, n)
    c.append(random_int1)
    c.append(random_int2)
    return c

def check_dupl(b, c):
    for i in b:
        while c == i or c == i[::-1]:
            c = create_pair()
    return c

def random_p(p_i):
    for r in range(0, len(p_i)):
        num = rand.uniform(0, 1)
        if num <= 0.1:
            p_i[r] = 1
    return (p_i)

def change_p(p_i, c):
    if p_i[c[0]-1] > 0 and p_i[c[1]-1] == 0:
        p_i[c[1] - 1] = p_i[c[0] - 1] + 1
    if p_i[c[0]-1] == 0 and p_i[c[1] -1 ] > 0:
        p_i[c[0] - 1] = p_i[c[1] - 1] + 1
    return(p_i)

def descending(arr):
    desc_arr = sorted(arr, reverse = True)
    desc_arr = list(dict.fromkeys(desc_arr))
    person_desc = []
    for i in range(0 , len(desc_arr)):
        for j in range(0, len(arr)):
            if desc_arr[i] == arr[j]:
                person_desc.append(j+1)
    return(person_desc)

def normalise(desc_a_i, a_i):
    norm_a_i = []
    for i in range(0, n):
        norm_a_i.append(round(desc_a_i[i]/desc_a_i[0], 3))
    return norm_a_i


random_p(p_i)
for i in range(1, k+1):
    pair = rand.randint(1, p_max)
    #print("In time stamp " + str(i) + " there are: " + str(pair) + " pairs")
    b = []
    for j in range(0, pair):
        c = create_pair()
        check_dupl(b, c)
        change_p(p_i, c)
        b.append(c)
    #print (b)
    for val in range(0, len(b)):
        max_value = max(a_i[b[val][0] - 1], a_i[b[val][1] - 1])
        a_i[b[val][0] - 1] = max_value + 1
        a_i[b[val][1] - 1] = max_value + 1

        


desc_a_i = sorted(a_i, reverse = True)
desc_p_i = sorted(p_i, reverse = True)
val_desc_a_i = descending(a_i)
val_desc_p_i = descending(p_i)
"""
print("Scores(a_i): ")
print (desc_a_i)
print("Descending a_i:")
print(val_desc_a_i)
print("Probs(p_i): ")
print(desc_p_i)
"""
print("Descending p_i:")
print(val_desc_p_i)

m = 100
c = 0
for i in range(0, m):
    if p_i[val_desc_a_i[i] - 1] > 0:
        c +=1
print("Count of people affected in range(" + str(m) + " out of " + str(n) + "): " + str(c))
norm_a_i = normalise(desc_a_i, a_i)


print(norm_a_i)
def accuracy(norm_a_i, p_i):
    cutoff = 0.6
    a_c = []
    loss_a_c = []
    c = 0
    loss = 0
    for i in range(0, n):
        if norm_a_i[i] >= cutoff:
            a_c.append(val_desc_a_i[i])
    print(a_c)
    for i in range(0, len(a_c)):
        if p_i[a_c[i] - 1] > 0:
            c += 1
    print(c/len(a_c))

    for i in range(0, n):
        if norm_a_i[i] < cutoff:
           loss_a_c.append(val_desc_a_i[i])
    print(loss_a_c)
    for i in range(0, len(loss_a_c)):
        if p_i[loss_a_c[i] - 1] > 0:
            loss += 1
    print(loss/len(loss_a_c))
accuracy(norm_a_i, p_i)










