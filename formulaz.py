from __future__ import division


import string, re
import itertools
import cProfile




def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    :param f

    ormula:
    :return:
    """
    for f in fill_in(formula):
        if valid(f):
            print f


def fill_in(formula):
    "General all possible fillings-in of letters in formula with digits"

    letters = ''.join(set(re.findall('[A-Z]', formula)))

    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))

        # print formula.translate(table)
        yield formula.translate(table)


def valid(f):
    "Formula f is valid iff it has no numbers with leading zero and evals true."

    try:

        return not re.search(r'\b0[0-9]', f) and eval(f) is True

    except ArithmeticError:
        return False


def compile_word(word):

    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""

    if word.isupper():

        terms = ['%s*%s'%(10**i,d) for i,d in enumerate(word[::-1])]

        return '(' +'+'.join(terms)+')'


    else:

        return word





def solve2(formula):

    f = 0

    return f




if __name__ == '__main__':

    import time

    print compile_word("IOU")

    t0 = time.time()

    solve('IOI+IOI==MEE')

    t1 = time.time()

    print "Problem solved in {:.4f} seconds.".format(t1 - t0)

    # cProfile.run('solve("ODD+ODD==EVEN")')
