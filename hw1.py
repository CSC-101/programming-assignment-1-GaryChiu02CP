import data
from data import Price


# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:
    tally = 0
    for i in word:
        if i.lower() in ['a','e','i','o','u']:
            tally+=1
    return tally

# Part 2
def short_lists(x:list[list[int]]) -> list:
    short = []
    for i in x:
        if len(i) == 2:
            short.append(i)
    return short

# Part 3
def ascending_pairs(x:list[list[int]]) -> list:
    ascending = []
    for i in x:
        if len(i) == 2:
            if i[0]>i[1]:
                ascending.append([i[1],i[0]])
            else:
                ascending.append(i)
        else:
            ascending.append(i)
    return ascending


# Part 4
def add_prices(p1:Price, p2:Price):
    p3 = Price(p1.dollars + p2.dollars, p1.cents + p2.cents)
    p3.dollars += p3.cents // 100
    p3.cents = p3.cents % 100
    return p3

# Part 5


# Part 6


# Part 7


# Part 8


