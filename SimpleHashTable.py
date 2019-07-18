#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:13:27 2019

@author: shiwanshu
"""

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        if string is not None:
            if self.table[hash_value] is None:
                
                self.table[hash_value] = [string]
            else:
                self.table[hash_value].append(string)
        else:
            pass
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hv = self.calculate_hash_value(string)
        if hv !=-1:
            if self.table[hv]!=None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if string is not None:
            hash_vlaue = (ord(string[0])*100)+ord(string[1])
            return hash_vlaue
        else: 
            return -1
        

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8372
print (hash_table.calculate_hash_value('SHIV'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('SHIV'))

# Test store
hash_table.store('SHIV')
# Should be 8372
print (hash_table.lookup('SHIV'))

# Test store edge case
hash_table.store('SHIV')
# Should be 8372
print (hash_table.lookup('SHIV'))
