import data
import math
from data import Price, Point, Rectangle, Circle, Book, Employee

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:
    tally = 0
    for i in word:
        if i.lower() in 'aeiou':
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
def rectangle_area(x:Rectangle) -> int:
    area = (x.bottom_right.x-x.top_left.x)*(x.bottom_right.y-x.top_left.y)
    return area

# Part 6
def books_by_author(name:str, books:list[Book]) -> list[Book]:
    authorsbooks = [i for i in books if name in i.authors]
    return authorsbooks

# Part 7
def circle_bound(rect:Rectangle) -> Circle:
    w = rect.bottom_right.x-rect.top_left.x
    h = rect.bottom_right.y-rect.top_left.y
    center = Point(w/2, h/2)
    radius = math.sqrt((w**2+h**2))/2
    return Circle(center, radius)

# Part 8
def below_pay_average(employees:list[Employee]) -> list[str]:
    avg = 0
    for i in employees:
        avg += i.pay_rate
    avg /= len(employees)
    underpaid = [i for i in employees if i.pay_rate < avg]
    return underpaid