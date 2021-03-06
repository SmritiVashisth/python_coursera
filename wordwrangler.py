"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    findex = 0
    finlist = []
    if len(list1) > 0:
        finlist.append(list1[0])
    for index in range(1,len(list1)):
        if finlist[findex] != list1[index]:
            finlist.append(list1[index])
            findex = findex + 1
            
    return finlist


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    len1 = len(list1)
    len2 = len(list2)
    index1 = 0
    index2 = 0
    intersectlist = []
    while index1 < len1 and index2 < len2:
        if list1[index1] == list2[index2]:
            intersectlist.append(list1[index1])
            index1 = index1 + 1
            index2 = index2 + 1
        elif list1[index1] > list2[index2]:
            index2 = index2 + 1
        elif list1[index1] < list2[index2]:
            index1 = index1 + 1
            
    return intersectlist

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in both list1 and list2.

    This function can be iterative.
    """   
    index1 = 0
    index2 = 0
    len1 = len(list1)
    len2 = len(list2)
    finlist = []
    
    while index1 < len1 and index2 < len2:
        
        if list1[index1] > list2[index2]:
            finlist.append(list2[index2])
            index2 += 1
        else:
            finlist.append(list1[index1])
            index1 += 1
            
    finlist = finlist + list1[index1:]
    finlist = finlist + list2[index2:]
    
    return finlist
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    result = []
    if len(list1) < 2:
        return list1
    else:
        mid = len(list1) / 2
        left = merge_sort(list1[:mid])
        right = merge_sort(list1[mid:])
        result = merge(left,right)
        
    return result


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    strings = []
    if len(word) < 1:
        return [word]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = list(gen_all_strings(rest))
        for string in rest_strings:
            strings.append(string)
            for index in range(0,len(string)+1):
                new_word = string[:index] + first + string[index:]
                strings.append(new_word)
                
    return strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    #url = codeskulptor.filetourl(filename)
    #urllib2.urlopen(url)

#def run():
#    words = load_words(WORDFILE)
#    wrangler = provided.WordWrangler(words, remove_duplicates, 
#                                     intersect, merge_sort, 
#                                     gen_all_strings)
#   provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
