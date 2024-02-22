import random as rand
import numpy as np
from numpy import arange
import matplotlib.pyplot as plt
import sys
import openpyxl
import re



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

def random_p(p_i, a):
    for r in range(0, len(p_i)):
        num = rand.uniform(0, 1)
        if num <= a:
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

def accuracy(norm_a_i, p_i, total_people, val_desc_a_i):
    cutoff = [0.4]
    a_c = []
    loss_a_c = []
    c = 0
    loss = 0
    accuracies = []
    losses = []
    count = 0
    #people_a_c = []
    for k in cutoff:
        for i in range(0, n):
            if norm_a_i[i] >= k:
                a_c.append(val_desc_a_i[i])
        #print("Subset that lies in the cutoff of " + str(k))
        #print(a_c)
        for i in range(0, len(a_c)):
            if p_i[a_c[i] - 1] > 1:
                c += 1
        #print("Above " + str(k) + ": " + str(len(a_c)), end = " ")
        #people_a_c.append(len(a_c))
        
        accuracy = (c/total_people)
        #print(str(round(accuracy, 3)), str(c), str(total_people))
        return round(accuracy, 3)
        #print("Accuracy of cutoff " + str(k) + ": " + str(round(accuracy, 3)))
        a_c = []
        c = 0   
        for i in range(0, n):
            if norm_a_i[i] < k:
                loss_a_c.append(val_desc_a_i[i])
        #print("Subset that is loss of " + str(k))
        #print(loss_a_c)
        for i in range(0, len(loss_a_c)):
            if p_i[loss_a_c[i] - 1] > 1:
                loss += 1
        count_loss = loss
        #print("Below " + str(k) + ": " + str(len(loss_a_c)), end = " ")
        loss = (count_loss/total_people)
        #print(str(round(loss, 3)), str(count_loss), str(total_people))
        
        #print("Loss of cutoff " + str(k) + ": " + str(round(loss, 3)))
        loss_a_c = []
        loss = 0
    
    
def precision(val_desc_a_i, p_i, total_people):
    temp = 0
    total = 0
    a = total_people #not necessary
    for i in range(0, len(val_desc_a_i)):
        if p_i[val_desc_a_i[i] - 1] > 1:
            temp = i
    for j in range(0, temp+1):
        if p_i[val_desc_a_i[j] - 1] > 1:
            total += (temp+1) - (j+1)
    sum_total = ((temp+1)*temp)/2
    precision = (total/sum_total)
    #print("Precision: " + str(round(precision, 3)))
    
def total_people_infected(n, p_i, val_desc_a_i):
    m = n
    c = 0
    for i in range(0, m):
        if p_i[val_desc_a_i[i] - 1] > 1:
            c += 1
    return c

def infected_in_range(n, p_i, val_desc_a_i):
    m = n
    c = 0
    for i in range(0, m):
        if p_i[val_desc_a_i[i] - 1] > 1:
            c += 1
    #print("Count of people affected in range(" + str(m) + " out of " + str(n) + "): " + str(c))
    return c

def infected_till_p_max(n, p_i, val_desc_a_i, p_max):
    c = 0
    for i in range(0, int(p_max)):
        if p_i[val_desc_a_i[i] - 1] > 1:
            c += 1
    #print("Count of people affected in range(" + str(m) + " out of " + str(n) + "): " + str(c))
    return (c/int(p_max))

def comparing_two_people(a_i, p_i, people, sample):
    C = 0
    I = 0
    #n = [100, 1000]
    #print("Number of times that will be run: " + str(n))
    #ratio_list = []
    #print(people)
    #print(p_i)
    for count in range(0, sample):
        p = rand.randint(1, people)
        q = rand.randint(1, people)
        #print(p, q)
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

def create_graph(the_people, frac, steps, p_i_values, sample_count, ratio_list):
    SUB = str.maketrans("max", "ₘₐₓ")
    factor = "Jmax/N".translate(SUB)
    
    plt.plot(sample_count, ratio_list)
    plt.title("N: " + str(the_people[0]) + ", T: " + str(steps[0]) + ", M/N: " + str(p_i_values[0]) + ", " + factor + ": " + str(frac[0]))
    plt.xlabel("R")
    plt.ylabel("Accuracy")
    plt.show()
    
def main(n, x, p_i, k, sample_count):
    p_max = int(x * n)#max number of pairs at any time step
    print(p_max)
    #p_i_values = [0.1, 0.15]
    #print(p_max)
    a_i = []
    
    #p_i = []
    #print(np.zeros((6,), dtype=int)

    #Create Scores 
    for i in range(0, n):
        a_i.append(0)
        #p_i.append(0)
    #for a in p_i_values:
        #random_p(p_i, a)
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
    print("a_i length: " + str(len(a_i)))
    #c = infected_in_range(n, p_i, val_desc_a_i)
    #norm_a_i = normalise(desc_a_i, a_i)
    #total_infected = total_people_infected(n, p_i, val_desc_a_i)
    #accuracy(norm_a_i, p_i, total_infected, val_desc_a_i)
    #precision(val_desc_a_i, p_i, total_infected)
    #top_p_max = infected_till_p_max(n, p_i, val_desc_a_i, p_max)
    #print(str(top_p_max))
    #print()
    ratio = comparing_two_people(a_i, p_i, n, sample_count)
    
    return(ratio)
    
def create_range(arr):
    for i in arange(0.05, 0.405, 0.005):
        arr.append(round(i, 3))
    return arr
    
rand.seed(7)
#the_people = [int(str(i)+ "00") for i in range(100, 201)] #number of people
the_people = [100]
frac = [0.1]
#frac = create_range(frac)
steps = [10]
#steps = [i for i in range(5, 100)]
p_i = []
p_i_values = [0.1] # originals
#p_i_values = create_range(p_i_values)
#sample_count = [1000]
sample_count = [int(str(i)+ "00") for i in range(1, 80)]
#people_a_c = []
ratio_list = []
#print("Steps: " + str(steps[0]) + ", Socialisation Factor: " + str(frac[0]) + ", Original Ratio: " + str(p_i_values[0]))
for n in the_people:
    for x in frac:
        for k in steps:
            #print("Data: " + str(n), str(x), str(k))
            for a in p_i_values:
                for sample in sample_count:
                    #Create Originaly affected 
                    for i in range(0, n):
                        p_i.append(0)
                        
                    new_p_i = random_p(p_i, a)
                    print("p_i length: " + str(len(new_p_i)))
                    ratio = main(n, x, new_p_i, k, sample)
                    ratio_list.append(ratio)
                    p_i = []
#print("Steps: " + str(steps[0]) + ", Socialisation Factor: " + str(frac[0]) + ", Original Ratio: " + str(p_i_values[0]))
#print(the_people, ratio_list)
create_graph(the_people, frac, steps, p_i_values, sample_count, ratio_list)
    
    
        #print()
