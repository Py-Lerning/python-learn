from functools import reduce
import logging


def str2num(s):
    return int(s)


def calc(exp):
    ss = exp.split("+")
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


if __name__ == '__main__':
    r = calc("100 + 200 + 345")
    print("100 + 200 + 345 = ", r)
    try:
        r = calc("99 + 88 + 7.6")
        print("99 + 88 + 7.6")
    except ValueError as e:
        logging.exception(e)