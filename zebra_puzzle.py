"""
Zebra Puzzle
1 There are five houses.

2 The Englishman lives in the red house.

3 The Spaniard owns the dog.

4 Coffee is drunk in the green house.

5 The Ukrainian drinks tea.

6 The green house is immediately to the right of the ivory house.

7 The Old Gold smoker owns snails.

8 Kools are smoked in the yellow house.

9 Milk is drunk in the middle house.

10 The Norwegian lives in the first house.

11 The man who smokes Chesterfields lives in the house next to the man with the fox.

12 Kools are smoked in a house next to the house where the horse is kept.

13 The Lucky Strike smoker drinks orange juice.

14 The Japanese smokes Parliaments.

15 The Norwegian lives next to the blue house.

Who drinks water? Who owns the zebra?

Each house is painted a different color, and their inhabitants are of different nationalities, own different pets, drink different beverages and smoke different brands of American cigarettes.

"""
import time


def factorial(x):
    if x <= 1:

        return 1

    else:

        return x * factorial(x - 1)


print factorial(5) ** 5

import itertools


def imright(h1, h2):
    "House h1 is immediately right of h2 if h1-h2 ==1."
    return h1 - h2 == 1


def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1 - h2) == 1


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))

    return next((WATER, ZEBRA)

                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)

                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in c(orderings)
                if (Englishman is red)  # 2
                if Norwegian is first
                if nextto(Norwegian, blue)  # 15

                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog

                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukrainian is tea
                if milk is middle

                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if OldGold is snails
                if Kools is yellow
                if nextto(Chesterfields, fox)  # 11
                if nextto(Kools, horse)  # 12
                if LuckyStrike is oj  # 13
                if Japanese is Parliaments
                )

def c(sequence):

    """
    Generate items in sequence;keeping counts as we go. c.starts is the
    number of sequences started; c.items is number of items generated.

    """

    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item



def instrument_fn(fn, *args):
    c.starts, c.items = 0,0

    result = fn(*args)

    print '%s got %s with %5d iters over %7d items' %(fn.__name__, result,c.starts,c.items )


def timedcall(fn, *args):
    t0 = time.clock()

    result = fn(*args)

    t1 = time.clock()

    return t1 - t0, result


def average(*args):
    return sum(*args) / float(len(*args))


def timedcalls(n, fn, *args):
    """

    :rtype: object
    """
    if isinstance(n, int) :

        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:

        times = []

        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])

    return min(times), average(times), max(times)


if __name__ == "__main__":
    print "Working on zebra puzzle, (WATER, ZEBRA)"

    instrument_fn(zebra_puzzle)

    time, result = timedcall(zebra_puzzle)

   # d = timedcalls(0.5, zebra_puzzle)

    print "Time working on this puzzle is {:.4f} seconds.".format(time)
