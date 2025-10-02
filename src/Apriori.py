import itertools

def create_transaction_database(fileName):
    """
Returns a database in list format from a file. 
It is assumed the transactions are seperated by new lines and the items are seperated by spaces.
Parameters:
fileName: The file containing the database
return:
A list that contains transactions. Each transaction is a list that contains integer item values.   
    """
    rawData = open(fileName).read().strip().split('\n')
        #Splitharacter can be set to tab or ' ' depending on what dataset is run
    rows = [row.strip().split('\t') for row in rawData]
    return [{int(item) for item in row} for row in rows]

def find_one_itemsets(database):
    """
Finds canidate one itemsets and their respective counts in one step
It is assumed the database is in a list format
Parameters:
database: The transaction database
return:
A dictonary whose key is the one itemset and the value is the itemset count
    """
    c1_itemsets = {}
    for row in database: #Every transaction
        for val in row: #Every item
            if val in c1_itemsets: #If the item was already found previously
                c1_itemsets[val] += 1 #Increment the count
            else:
                c1_itemsets[val] = 1 #First time the item was found in the database
    return c1_itemsets

def find_two_itemsets(l1):
    """
Finds canidate two itemsets and their respective counts in one step
It is assumed L1 is a list containing tuples that contain the one itemset and its count
Parameters:
l1: The list of one itemsets
return:
A dictonary whose key is the one itemset and the value is the itemset count
    """
    l1_items = []
    c2_itemsets = {}
    #Make a list of one itemsets without their counts
    for item in l1:
        l1_items.append(item[0])
        #Make all possible 2 set combinations from L1
    possible_combinations = itertools.combinations(l1_items, 2)
    #Initialize two itemset counts to 0
    for item_set in possible_combinations:
        c2_itemsets[item_set] = 0
    return c2_itemsets

def find_k_itemsets(lk, k_inc):
    """
Finds k + 1 canidate itemsets from lk
It is assumed L1 is a list containing tuples that contain the itemset tuple and its count
Parameters:
lk: The list used to create k + 1 itemsets
k_inc: k + 1, or the canidate itemsets that you are trying to find
return:
A dictonary whose key is a tuple of the itemset and the value is the itemset count that is set to 0
    """
    #This method walks a list with head and taail pointers index and second_index,
    #  so every transaction is compared
    ck_itemsets = {}
    for index, itemset in enumerate(lk):
        second_index = index + 1 #Index of next item
        while second_index < len(lk) and index < len(lk) - 1:
            first_n_equal = True
            item_count = 0
            #See if the first k - 1 items in Lk  are the same for the joining step
            while item_count < k_inc - 2 and first_n_equal:
                if itemset[0][item_count] != lk[second_index][0][item_count]:
                    first_n_equal = False
                item_count += 1
            #If the first k - 1 items are equal, usde the joining step and add the itemset to ck
            if first_n_equal:
                itemset_list = list(itemset[0])
                itemset_list.append(lk[second_index][0][k_inc - 2])
                ck_itemsets[tuple(itemset_list)] = 0
            second_index = second_index + 1
    return ck_itemsets

def count_itemsets(database, ck, k):
    """
Counts the itemsets in the database, and updates these counts in ck
It is assumed c1 is a list containing tuples that contain the itemset tuple and its count (initially 0)
Parameters:
database: The transaction database
ck: The canidate itemsets that needed to be counted in the database
k: The number of the current canidate set 
return:
A dictonary (ck Param) whose key is a tuple of the itemset and the value is the itemset count
    """
    ck_items = []
    #Make a list of only itemsets withouut counts
    for key, count in ck.items():
        ck_items.append(key)
    for row in database:
        #Make all possible k item combinations in a transaction
        possible_combinations = set(itertools.combinations(row, k))
        for item_set in ck_items:
            #so the subset function can be used on the whole itemset tuple
            item_list = []
            item_list.append(item_set)
            #If an itemset is in a transaction, icrement its count
            if set(item_list).issubset(possible_combinations):
                ck[item_set] += 1 

def find_frequent_itemsets(ck, min_support, num_transactions):
    """
Determines if a ck itemset is frequent and, if so  it gets added to lk
It is assumed c1 is a list containing tuples that contain the itemset tuple and its count (initially 0)
Parameters:
ck: The canidate itemsets that could be in lk
min_support: The minimum support needed to be in lk
num_transactions: The number of transactions in the database
return:
A list whose key is a tuple of the itemset and the value is the itemset count
    """
    frequent_sets = []
    for itemset, count in ck.items():
        if (count / num_transactions) * 100 >= min_support: #If a canidate set appears more than minimum support
            frequent_sets.append((itemset, count)) #Add it to the frequent sets
    return sorted(frequent_sets, key = lambda i: i[0])

def prune_list(prev_list, lk, prev_k):
    """
Determines if all of the subsets of an itemset are in Lk-1. Prunes Lk
It is assumed prev_list and are lists containing tuples that contain the itemset tuple and its count (initially 0)
Parameters:
prev_list: The k - 1 list
lk: The current list
prev_k: the prewvious k value (Used for finding subsets)
return:
A list whose key is a tuple of the itemset and the value is the itemset count
    """
    lk_index = 0
    prev_list_items = []
    #Get only the itemsets from the previous list
    for item in prev_list:
        prev_list_items.append(item[0])
    prev_list_items = set(prev_list_items)
    while lk_index < len(lk):
        #Find all necessary previous item combinations for the set to not be pruned
        necessary_subsets = list(itertools.combinations(lk[lk_index][0], prev_k)) 
        itemset_index = 0 
        #Check that every necessesary subset is in previous list
        for subset in necessary_subsets:
            #so the subset function can be used on the whole itemset tuple
            item_list = []
            item_list.append(subset)
            #if the subset is present, increment count
            if set(item_list).issubset(prev_list_items):
                itemset_index += 1
        #If all of the nessesary subsets were not counted, remove the itemset from the list
        if itemset_index != len(necessary_subsets):
            lk.remove(lk[lk_index])
        else:
            #If all of the subsets are present, keep walking the list
            lk_index = lk_index + 1
        
    return lk