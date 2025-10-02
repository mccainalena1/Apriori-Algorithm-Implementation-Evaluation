import Apriori
import time
import copy
min_support = 2
while min_support > 0:
    #Mark start time
    start_time = time.time()
    #Make transation database
    transaction_database = Apriori.create_transaction_database("1000-out1No_Commas.txt")
    num_transactions = len(transaction_database)
    #Make L1 and L2 
    print("Minimum Support: " + str(min_support))
    c1 = Apriori.find_one_itemsets(transaction_database)
    l1 = Apriori.find_frequent_itemsets(c1, min_support, num_transactions)
    print("L1:", end =" ")
    for item in l1:
        print(str(item[0]), end =" ")
    print()
    c2 = Apriori.find_two_itemsets(l1)
    Apriori.count_itemsets(transaction_database, c2, 2)
    l2 = Apriori.find_frequent_itemsets(c2, min_support, num_transactions)
    print("L2:", end =" ")
    for itemset in l2:
        print(str(itemset[0]), end =" ")
    print()
    if len(l2) > 1: #The joining step can be done
        #Create L3 
        k = 3
        ck = Apriori.find_k_itemsets(l2, k)
        Apriori.count_itemsets(transaction_database, ck, k)
        lk = Apriori.find_frequent_itemsets(ck, min_support, num_transactions)
        lk = Apriori.prune_list(l2, lk, k - 1)
        print("L" + str(k) + ":", end =" ")
        for itemset in lk:
            print(str(itemset[0]), end =" ")
        print()
        prev_list = copy.deepcopy(lk)
        k += 1 #Strart with creating L4
        while len(lk) > 1: #The joining step can be done
            ck = Apriori.find_k_itemsets(lk, k)
            Apriori.count_itemsets(transaction_database, ck, k)
            lk = Apriori.find_frequent_itemsets(ck, min_support, num_transactions)   
            lk = Apriori.prune_list(prev_list, lk, k - 1)
            print("L" + str(k) + ":", end =" ")
            for itemset in lk:
                print(str(itemset[0]), end =" ")
            print()
            prev_list = copy.deepcopy(lk)
            k = k + 1
    end_time = time.time() - start_time
    #Output data
    with open("1000_comp.txt",'a') as output:
        output.write(str(min_support) + "," + str(end_time) + "\n")
    output.close()
    if min_support > 1:
        min_support -= .5
    else:
        min_support -= .25