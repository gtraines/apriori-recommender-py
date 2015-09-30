'''
Graham Traines
CSCI7990 Machine Learning
Semester Project Code
An Offline Shopping Recommendation Engine

''' 
import sklearn 
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from collections import defaultdict
from itertools import chain
import os 

# Association Rules (Agrawal and Srinkat)
# From Brijs, T. Using Association Rules For Product Assortment Decisions
# " Let I = {i[1], ... , i[k]} be a set of literals called Items
#
# Let D be a set of transactions, where each transaction T is a set of items 
# such that T is a subset of I
#
# Associated with each transaction is a unique identifer, TID
#
# We say that a Transaction T contains X
# X = a set of some items in I, if X is a subset of T
#
# An association rule is an implication of the form X => Y, where 
# X is a subset of I, Y is a subset of I, and X intersect Y = null //Graham: They are disjoint
# 
# The rule X => (implies) Y holds in the transaction set D with 
# confidence c if c% of transactions in D that contain D *also contain Y.*
#
# The rule X => (implies) Y has support s in the transaction set D if
# s% of transactions in D contain X union Y.
#
# Given: a set of transactions D, the problem of mining associationm rules is to generate
# all association rules that have: 
# support and confidence > a user-specified minimum support (minsup) AND
# minimum confidence (minconf)
# 
# Generating association rules involves looking for
# so-called "frequent itemsets" in the data.
# Indeed, the support of the rule X => (implies) Y
# equals the frequency of trhe itemset {X, Y}.
#
# Thus, by looking for frequent itemsets, 
# we can determine the support of each rule.

# Definition 1: Frequency of an itemset
# s(X, D) represents the frequency of itemset X in D,
# i.e. the fraction of transactions in D that contain X. 
def get_support(item_set, data_set):
    total_trx = len(data_set)
    X = 0
    for transaction in data_set:
        if item_set.issubset(transaction):
            X += 1

    return float(X) / float(total_trx)

# Definition 2: Frequent itemset
# An itemset X is called frequent in D if s(X, D) > little_sigma with 
# little_sigma the minsup (minimum support)
def is_frequent_itemset(item_set, data_set, little_sigma_min_support):
    if get_support(item_set, data_set) > little_sigma_min_support:
        return True
    else:
        return False

def get_confidence(antecedent_set, consequent_set, data_set):
    confidence = get_support((antecedent_set, consequent_set), data_set) / get_support(antecedent_set, data_set)
    return confidence

def load_transaction_set(file_location, number_trx_to_get):
    with open(file_location) as data_file:
        data_set = [[int(item) for item in next(data_file).strip().split()]
                    for x in xrange(number_trx_to_get)]
    return data_set

def get_item_counts_and_total_from_data_set(data_set):
    item_counts = defaultdict(int)
    total_count = 0
    for item in chain(*data_set):
        item_counts[item] += 1
        total_count += 1
    return item_counts, total_count

def get_candidate_set(item_counts, total_count, little_sigma):
    candidate_set = []
    for item in item_counts.viewitems():
        if (float(item[1])/float(total_count)) > little_sigma:
            candidate_set.append(item[0])
            print float(item[1])/float(total_count)
    return candidate_set

def combine_candidate_sets(candidate_set):
    return

# minimum support
little_sigma = 0.05
#minimum confidence
min_conf = 0.65

data = load_transaction_set('retail.dat', 1000)
item_counts, total_count = get_item_counts_and_total_from_data_set(data)
candidate_set = get_candidate_set(item_counts, total_count, little_sigma)
