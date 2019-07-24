#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:50:05 2019

@author: shiwanshu
"""
class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRU_Cache(object):


    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.head = None
        pass
    
    def update_value(self, key,value):
        
        cur = self.head
        while cur:
            # case1:
            if cur.value == value and cur == self.head:
                # case1 --> O<--[]-->O
                if not cur.next:
                    cur = None
                    self.head = None
                    self.set(key,value)
                    return
                # case 2 O<--[A]-->[B]-->O; delete A
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    # Update head at last
                    self.head = nxt
                    self.set(key,value)
                    return
                    
                
            elif cur.value == value:
                # case 3: O<--[A]-->[B]-->[C]-->O ; delete B
                if cur.next:
                    nxt = cur.next
                    prv = cur.prev
                    prv.next = nxt
                    nxt.prev = prv
                    cur.next = None
                    cur.prev = None
                    cur = None
                    self.set(key,value)
                    return
                #case 4
                else:
                    # if cur.next is None like : O<--[A]-->[B]-->[C]-->O ; delete C
                    prv = cur.prev
                    prv.next = None
                    cur.next = None
                    cur = None
                    self.set(key,value)
                    return
                    
            cur = cur.next      
        
    def delete(self,key,value):
        cur = self.head
        nxt = cur.next
        cur.next = None
        nxt.prev = None
        cur = None
        # Update head at last
        self.head = nxt
        return

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        
        node = self.head
        while node is not None:
            if node.value == key:
                self.update_value(key, node.value)
                return node.value
            node = node.next
            
        return -1
    
        
    

    def size(self):
        size = 0
        node = self.head
        while node:
            size+=1
            node = node.next
        return size
    
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # append
        if self.size()< self.capacity:
            if self.head is None:
                new_node = LinkedListNode(key,value)
                new_node.prev = None
                self.head = new_node
                return
            else:
                cur = self.head
                while cur.next:
                    cur = cur.next
                new_node = LinkedListNode(key,value)
                cur.next = new_node
                new_node.next = None
                new_node.prev = cur
                return
        else:
            if self.get(key)!=-1:
                self.update_value(key,self.head.value)
            else:
                self.delete(key,self.head.value)
                self.set(key,value)
        pass
    def printLL(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2
print(our_cache.get(9))   # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print('*********')
our_cache.printLL()