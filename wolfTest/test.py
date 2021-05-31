# This file takes the generates string/dict from generate.py and runs it
# through api.py to recieve wolframs' output. It then calculates the supposed
# answer to the question (or looks it up in a db is the answer is static) then
# checks it against the api.py's output

import math, hashlib, zlib
import itertools
from sympy import symbols, solve, factor, diff, simplify
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication,
    convert_xor,
)
from mpmath import mp
############################# WORKING #############################

# Solution generators


def dob_check(name):
    # Dict can be indexes by a string, i.e. the name in this case
    dob_dict = {
        "Harriet Tubman":"March 1822", 
        "Marvin Gaye":"Sunday, April 2, 1939",
        "Charlemagne":"747 AD",
        "Galileo Galilei":"Tuesday, February 15, 1564",
        "Warren Buffett":"Saturday, August 30, 1930",
        "Tom Hanks":"Monday, July 9, 1956",
        "Ferdinand Magellan":"1480",
        "Wiley Post":"Tuesday, November 22, 1898"
    }
    return dob_dict[name]


def quadratic_check(a, b, c):
    x = symbols("x")
    expr = a * x**2 + b * x + c
    return solve(expr)  # example [-1 - sqrt(2)*I, -1 + sqrt()*I], a = 2, b = 4, c = 6

def math_check(a, b, c, d):
    expr = (a + b - c) / d
    return expr         #example 1.0, a = 2, b = 8, c = 6, d = 4

def factor_check(a, b, c, d, e, f):
    x = symbols("x")
    expr = a * x**5 - b * x**4 + c * x**4 - d * x**2 + e * x**3 - f
    return factor(expr)

def hash_check(s):
    # encode string with 3 different has methods. Will return encoded string in hexadecimal form
    s = s.split(' ', 1)
    hash_hex = None
    if s[0] == "SHA1":
        hash_hex = hashlib.sha1(s[1].encode()).hexdigest()
    elif s[0] == "MD5":
        hash_hex = hashlib.md5(s[1].encode()).hexdigest()
    elif s[0] == "CRC32":
        hash_hex = format(zlib.crc32(str.encode(s[1])), 'x')
    else:
        return "Hash method undefined"
    hash_int = int(hash_hex, 16)
    hex_str = ' '.join(hash_hex[i:i+4] for i in range(0,len(hash_hex),4)) # add space every 4 hex digits
    return "integer form | {}\nhexadecimal form | {}".format(hash_int, hex_str)

def derivative_check(a, b, c):
    x = symbols("x")
    expr = a * x**4 + b * x**3 + c * x
    answer = diff(expr, x)
    return answer

def deg2rad_check(degrees):
    radians = degrees * math.pi / 180
    return radians

def pi_check(length):
    mp.dps = length
    return float(str(mp.pi))

def sum_check(a, b):
    return float(a + b)

def volume_food_check(volume, food_unit):
    return ("calories in " + str(volume) + food_unit)

############################# IN PROGRESS #############################

def solve_check(a, b, c, d):
    x = symbols("x")
    eq1 = a * x**2 + b*x - c + d * x**3
    answer = solve(eq1)
    return answer


def truth_table_check(expr, num_letters):
    letters = ['q', 'r', 's', 't', 'u', 'v']  # std array of logic letters
    #assuming sequential variables
    expr = expr.lower()
    # replace names with expressions
    expr = expr.replace("and", "&")
    expr = expr.replace("xor", "^")
    expr = expr.replace("or", "|")
    expr = expr.replace("not", "~")
    expr = parse_expr(expr)
    # create table string for comparison
    table = list(itertools.product([True, False], repeat=num_letters))
    q, r, s, t, u, v = symbols('q,r,s,t,u,v')
    # Go through each combo
    output = ""
    for row in table:
        temp_out = ""
        for index in range(num_letters):
            temp_out += ('T' if row[index] == True else 'F')
        temp_out += 'T' if expr.subs({
            q: False if num_letters < 1 else row[0],
            r: False if num_letters < 2 else row[1],
            s: False if num_letters < 3 else row[2],
            t: False if num_letters < 4 else row[3],
            u: False if num_letters < 5 else row[4],
            v: False if num_letters < 6 else row[5]}) else 'F'
        temp_out = " | ".join(temp_out)
        output += temp_out + "\n"
    return output[:-1] # remove last '\n'

# Formatters


def sympy_list_format(unformatted):
    formatted = []
    for item in unformatted:
        formatted.append(item.replace("i", "I")) # replace i with I because that's how sympy does irrational
    return [ sympy_format(item) for item in formatted ] # run parser

def sympy_format(unformatted):
    formatted = unformatted.replace("^", "**") # replace ^ with python power **
    transformations = standard_transformations + (
        implicit_multiplication,
        convert_xor,
    )  # setup variables for symbpy transformations
    return parse_expr(formatted, transformations=transformations)

def sympy_list_sort(unsorted):
    def key_func(sympy_data):
        return float(simplify(sympy_data).as_real_imag()[0]) + float(simplify(sympy_data).as_real_imag()[1])
    unsorted.sort(key=key_func)
    return unsorted