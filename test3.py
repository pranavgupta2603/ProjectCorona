import random as rand
import numpy as np
from numpy import arange, polyfit
import matplotlib.pyplot as plt
import sys
#import openpyxl
#import re

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

def random_p(p_i, a, n):
    for r in range(0, len(p_i)):
        num = rand.uniform(0, 1)
        #print(a/n)
        if num <= a/n:
            p_i[r] = 1
    return (p_i)

def change_p(p_i, c):
    if p_i[c[0]-1] > 0 and p_i[c[1]-1] == 0:
        p_i[c[1] - 1] = p_i[c[0] - 1] + 1
    if p_i[c[0]-1] == 0 and p_i[c[1] -1 ] > 0:
        p_i[c[0] - 1] = p_i[c[1] - 1] + 1
    return(p_i)

def comparing_two_people(a_i, p_i, people, sample):
    C = 0
    I = 0
    for count in range(0, sample):
        p = rand.randint(1, people)
        q = rand.randint(1, people)
        while p == q:
            q = rand.randint(1, people)
        if p_i[p - 1] > 1 or p_i[q - 1] > 1:
            C += 1
            if a_i[p - 1] > a_i[q - 1] and p_i[p - 1] > 1:
                I += 1
            if a_i[p - 1] < a_i[q - 1] and p_i[q - 1] > 1:
                I += 1
    print(I/C)
    return (I/C)
def main(n, x, p_i, k, sample_count):
    p_max = int(x * n)#max number of pairs at any time step
    #p_max = (p_max / n) * 1000
    print(p_max)
    a_i = []
    #Create Scores 
    for i in range(0, n):
        a_i.append(0)
    for i in range(1, k+1):
        pair = rand.randint(1, p_max)
        b = []
        for j in range(0, pair):
            c = create_pair()
            check_dupl(b, c)
            change_p(p_i, c)
            b.append(c)
        for val in range(0, len(b)):
            max_value = max(a_i[b[val][0] - 1], a_i[b[val][1] - 1])
            a_i[b[val][0] - 1] = max_value + 1
            a_i[b[val][1] - 1] = max_value + 1
    print("a_i length: " + str(len(a_i)))
    ratio = comparing_two_people(a_i, p_i, n, sample_count)
    countofInfected(p_i)
    return(ratio)

def create_range(arr):
    for i in arange(0.05, 0.205, 0.005):
        print("sup: ", str(i))
        arr.append(round(i, 3))
    return arr
def create_graph(the_people, frac, steps, m, sample_count, ratio_list):
    SUB = str.maketrans("max", "ₘₐₓ")
    factor = "Jmax/N".translate(SUB)
    plt.plot(frac, ratio_list)

    plt.title("R: " + str(sample_count[0]) + ", M: " + str(m[0])+ ", T: " + str(steps[0]) + ", N: " + str(the_people[0]))
    plt.xlabel(str(factor))
    plt.ylabel("Accuracy")
    """x = np.array(steps)
    y = np.array(ratio_list)
    g, b = np.polyfit(x, y, 1)
    plt.plot(x, g*x + b)"""
    plt.show()
def countofInfected(p_i):
    count = 0
    for i in p_i:
        if i > 1:
            count +=1
    print(count)

    
rand.seed(11)
#the_people = [int(str(i)+ "00") for i in range(5, 83)] #number of people
the_people = [10000]
frac = []
frac = create_range(frac)
steps = [20]
#steps = [i for i in range(5, 100)]
p_i = []
#m = [int(str(i) + "0") for i in range(20, 100)] # originals
m = [300]
sample_count = [10000]
#sample_count = [int(str(i)+ "00") for i in range(1, 81)]
ratio_list = []
for n in the_people:
    for x in frac:
        for k in steps:
            for a in m:
                for sample in sample_count:
                    #Create Originaly affected 
                    for i in range(0, n):
                        p_i.append(0)
                    new_p_i = random_p(p_i, a, n)
                    ratio = main(n, x, new_p_i, k, sample)
                    ratio_list.append(ratio)
                    p_i = []
create_graph(the_people, frac, steps, m, sample_count, ratio_list)
