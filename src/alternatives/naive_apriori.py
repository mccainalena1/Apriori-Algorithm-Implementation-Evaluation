import itertools
import csv
import parameters
import time

def load_data(filename, max_attr=100):
    """ 
    Loads data from given
    :param filename Name of data source file
    :param max_attr:  Maximum number of attributes to be considered
    :return: Returns transactions each of which containing no more than
    max_attr
    """
    trans = []
    reader = csv.reader(open(filename, 'r'), delimiter=',')
    for row in reader:
        row = row[0].split(' ')
        trans.append([int(item) for item in row[1:]])
    return trans


def solve(data, support, confidence):
    transactions = len(data)
    T = []
    hashmap = {}
    for row in data:
        for word in row:
            if word not in hashmap.keys():
                hashmap[word] = 1
            else:
                hashmap[word] += 1

    level = []
    for key in hashmap:
        if (100 * hashmap[key] / transactions) >= float(support):
            level.append([key])

    return find_association_rules(level, support, confidence)


def find_subsets(S, m):
    return set(itertools.combinations(S, m))


def has_infrequent_subset(dataset, prev_l, k):
    list = find_subsets(dataset, k)
    for item in list:
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in prev_l:
            return True
    return False


def apply_support(singles, support):
    k = 2
    prev_l = []
    L = []
    for item in singles:
        prev_l.append(item)
    while prev_l:
        current = []
        sets = apriori(prev_l, k - 1)
        for c in sets:
            cnt = 0
            trans = len(data)
            s = set(c)
            for T in data:
                t = set(T)
                if s.issubset(t):
                    cnt += 1
            if (100 * cnt / trans) >= float(support):
                c.sort()
                current.append(c)
        prev_l = []
        for l in current:
            prev_l.append(l)
        k += 1
        if current:
            L.append(current)
    # for item in L:
    #     for x in item:
    #         print x
    return L


def find_association_rules(singles, support, confidence):
    num = 1
    L = apply_support(singles, support)
    result = 0
    for list in L:
        for l in list:
            length = len(l)
            count = 1
            while count < length:
                r = find_subsets(l, count)
                count += 1
                for item in r:
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in data:
                        if set(s).issubset(set(T)):
                            inc1 += 1
                        if set(l).issubset(set(T)):
                            inc2 += 1
                    if 100 * inc2 / inc1 >= float(confidence):
                        for index in l:
                            if index not in s:
                                m.append(index)
                        result += 1
                        num += 1
    return result


def apriori(prev_l, k):
    length = k
    result = []
    for list1 in prev_l:
        for list2 in prev_l:
            count = 0
            c = []
            if list1 != list2:
                while count < length - 1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length - 1] < list2[length - 1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length - 1])
                        if not has_infrequent_subset(c, prev_l, k):
                            result.append(c)
    return result

min_support = 2
while min_support > 0:
    start_time = time.time()
    data = load_data('1000-out1.csv')
    solve(data, min_support, 0)
    end_time = time.time() - start_time
    with open("1000Comp_NoHash.txt",'a') as output:
        output.write(str(min_support) + "," + str(end_time) + "\n")
    output.close()
    if min_support > 1:
        min_support -= .5
    else:
        min_support -= .25
